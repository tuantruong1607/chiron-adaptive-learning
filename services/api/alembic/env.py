from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context
from app.config import get_settings

config = context.config
if config.config_file_name:
    fileConfig(config.config_file_name)

settings = get_settings()
migration_url = settings.database_admin_url or settings.database_url
if migration_url:
    if migration_url.startswith("postgresql://"):
        migration_url = migration_url.replace("postgresql://", "postgresql+psycopg://", 1)
    elif migration_url.startswith("postgres://"):
        migration_url = migration_url.replace("postgres://", "postgresql+psycopg://", 1)
    config.set_main_option("sqlalchemy.url", migration_url)

target_metadata = None


def run_migrations_offline() -> None:
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
