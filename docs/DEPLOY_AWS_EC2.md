# Deploy Chiron on AWS EC2

This profile keeps the current PostgreSQL, Redis, API, worker and web modules in
Docker Compose. Qdrant runs on Qdrant Cloud Free, and Qdrant Cloud Inference
keeps the large local embedding model out of the EC2 worker.

## Target topology

- EC2 ARM64: `t4g.small` for a pilot after the local model is removed; use a
  larger instance if indexing or grading load is sustained.
- PostgreSQL and Redis: local Compose volumes on the EC2 host.
- Qdrant: external Qdrant Cloud endpoint and API key.
- Five containers: `postgres`, `redis`, `api`, `worker` (worker + beat), `web`.
- Only port 80 should be public. Keep PostgreSQL, Redis, API and worker metrics
  private.

## First setup

1. Create an Ubuntu ARM64 EC2 instance and attach an EBS volume large enough for
   PostgreSQL data and backups. Restrict SSH to your IP and allow HTTP/HTTPS.
2. Install Docker Engine and the Compose plugin.
3. Create a Qdrant Cloud cluster with Cloud Inference enabled. Use a new
   collection name because the AWS profile has a different embedding model.
4. Copy `deploy/aws.env.example` to `deploy/aws.env`, then fill in the
   production secrets and the live OIDC callback URL.
5. Copy the repository to the EC2 host and run:

   ```bash
   chmod +x deploy/aws/*.sh
   ./deploy/aws/deploy.sh
   ```

The script starts data services, applies Alembic migrations, then starts the
API, worker and web services. The worker uses `--pool=solo` and `--beat` to
avoid a separate scheduler container.

## Backup and rollback

Run `./deploy/aws/backup.sh` before migrations or releases. Copy the generated
dump to S3 or another host; the local `backups/` directory is not a backup
until it is copied off the instance.

For rollback, deploy the previous repository revision, restore the last known
good PostgreSQL dump into a separate database first, run the smoke checks, and
then switch the service back to that revision. Qdrant Cloud snapshots are
managed separately in its console/API.

## Free-profile gates

- `GRAPH_LITE_ENABLED=false` until the new Qdrant Cloud collection passes the
  graph evaluation. The existing local embedding evaluation does not validate
  the new Cloud Inference model.
- Do not index private/sensitive documents unless the Qdrant Cloud data policy
  has been approved. `QDRANT_CLOUD_DOCUMENT_INFERENCE_ALLOWED=true` is an
  explicit acknowledgement for approved pilot content.
- Set a billing alert and usage limit in AWS before starting sustained traffic.
