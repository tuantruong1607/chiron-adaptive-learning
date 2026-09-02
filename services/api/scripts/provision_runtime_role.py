from __future__ import annotations

import re

from psycopg import sql
from sqlalchemy import create_engine, text

from app.config import get_settings
from app.db import normalize_database_url

ROLE_PATTERN = re.compile(r"^[a-z_][a-z0-9_]{0,62}$")


def quote_identifier(value: str) -> str:
    if not ROLE_PATTERN.fullmatch(value):
        raise ValueError("DATABASE_RUNTIME_USER must be a simple PostgreSQL identifier")
    return f'"{value}"'


def provision() -> dict[str, str | bool]:
    settings = get_settings()
    if not settings.database_admin_url:
        raise RuntimeError("DATABASE_ADMIN_URL is required")
    if not settings.database_runtime_password:
        raise RuntimeError("DATABASE_RUNTIME_PASSWORD is required")
    role = settings.database_runtime_user
    quoted_role = quote_identifier(role)
    engine = create_engine(normalize_database_url(settings.database_admin_url))

    raw_connection = engine.raw_connection()
    try:
        with raw_connection.cursor() as cursor:
            cursor.execute("SELECT 1 FROM pg_roles WHERE rolname = %s", (role,))
            exists = cursor.fetchone() is not None
            action = sql.SQL("ALTER ROLE") if exists else sql.SQL("CREATE ROLE")
            cursor.execute(
                sql.SQL(
                    "{} {} WITH LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE "
                    "NOINHERIT NOBYPASSRLS PASSWORD {}"
                ).format(
                    action,
                    sql.Identifier(role),
                    sql.Literal(settings.database_runtime_password),
                )
            )
        raw_connection.commit()
    finally:
        raw_connection.close()

    with engine.begin() as connection:
        database = connection.scalar(text("SELECT current_database()"))
        if not isinstance(database, str) or not ROLE_PATTERN.fullmatch(database):
            raise RuntimeError("Unexpected database name")
        connection.execute(text(f'GRANT CONNECT ON DATABASE "{database}" TO {quoted_role}'))
        connection.execute(text(f"GRANT USAGE ON SCHEMA public TO {quoted_role}"))
        connection.execute(
            text(
                f"GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public "
                f"TO {quoted_role}"
            )
        )
        connection.execute(
            text(f"GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO {quoted_role}")
        )
        connection.execute(
            text(
                "ALTER DEFAULT PRIVILEGES IN SCHEMA public "
                f"GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO {quoted_role}"
            )
        )
        connection.execute(
            text(
                "ALTER DEFAULT PRIVILEGES IN SCHEMA public "
                f"GRANT USAGE, SELECT ON SEQUENCES TO {quoted_role}"
            )
        )
        flags = (
            connection.execute(
                text(
                    "SELECT rolsuper, rolbypassrls, rolcreatedb, rolcreaterole "
                    "FROM pg_roles WHERE rolname = :role"
                ),
                {"role": role},
            )
            .mappings()
            .one()
        )
    return {
        "role": role,
        "superuser": bool(flags["rolsuper"]),
        "bypass_rls": bool(flags["rolbypassrls"]),
        "createdb": bool(flags["rolcreatedb"]),
        "createrole": bool(flags["rolcreaterole"]),
    }


if __name__ == "__main__":
    print(provision())
