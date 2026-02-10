# RecipeFirst Docker Deployment Guide

This guide explains how to run RecipeFirst using Docker Compose with a 3-container architecture:
- **PostgreSQL** - Production database
- **FastAPI** - Backend API server
- **Nginx** - Frontend web server serving Vue.js SPA and proxying API requests

## Prerequisites

- Docker Engine 20.10+
- Docker Compose 2.0+

## Quick Start

### 1. Build and Start Containers

```bash
# Build and start all services
docker-compose up --build

# Or run in detached mode (background)
docker-compose up -d --build
```

This will:
1. Start PostgreSQL container with health checks
2. Build and start FastAPI container (waits for PostgreSQL to be healthy)
3. Run Alembic migrations automatically
4. Seed database with starter data (units, categories, ingredients)
5. Start the FastAPI server
6. Build and start Nginx container serving the Vue.js frontend

**First-time startup includes:**
- 21 measurement units (cup, tablespoon, gram, etc.)
- 25 categories (meal types, cuisines, dietary preferences)
- 41 basic ingredients (salt, flour, chicken, etc.)

The database is automatically initialized and ready to use!

### 2. Access the Application

- **Frontend**: http://localhost
- **API**: http://localhost/api (proxied to FastAPI)
- **API Direct**: http://localhost:8000 (FastAPI container, for debugging)

### 3. View Logs

```bash
# View all logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f fastapi
docker-compose logs -f postgres
docker-compose logs -f nginx
```

### 4. Stop Containers

```bash
# Stop containers (keeps data)
docker-compose stop

# Stop and remove containers (keeps volumes/data)
docker-compose down

# Stop and remove everything including volumes (DESTROYS DATA!)
docker-compose down -v
```

### 5. Rebuild and Reset

For development, you can frequently rebuild and get a fresh database:

```bash
# Full reset: destroy everything and rebuild from scratch
docker-compose down -v && docker-compose up --build -d

# Just rebuild containers (keeps database data)
docker-compose up --build -d
```

**Note:** The database seed data is idempotent - it will only add starter data if the database is empty. Rebuilding containers without removing volumes (`-v`) will keep your existing data.

## Data Migration from SQLite

If you have existing SQLite data, follow these steps:

### 1. Start Containers

```bash
docker-compose up -d
```

### 2. Run Migration Script

```bash
# Set the PostgreSQL connection string
export DATABASE_URL="postgresql+asyncpg://recipefirst:recipefirst123@localhost:5432/recipefirst"

# Install dependencies locally (if not already done)
pip install -r requirements.txt

# Run the migration script
python migrate_data.py
```

The script will:
- Copy all data from SQLite to PostgreSQL
- Preserve foreign key relationships
- Verify the migration
- Report any issues

### 3. Verify Migration

Access the application at http://localhost and verify your data is present.

## Container Architecture

```
┌─────────────────────────────────────────────────────┐
│  Nginx (Port 80)                                    │
│  - Serves Vue.js SPA                                │
│  - Proxies /api/* to FastAPI:8000                   │
└─────────────────┬───────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────┐
│  FastAPI (Port 8000)                                │
│  - REST API endpoints                               │
│  - SQLAlchemy ORM + async                           │
│  - Auto-runs Alembic migrations on startup          │
└─────────────────┬───────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────┐
│  PostgreSQL (Port 5432)                             │
│  - Database: recipefirst                            │
│  - User: recipefirst                                │
│  - Password: recipefirst123                         │
│  - Volume: postgres_data                            │
└─────────────────────────────────────────────────────┘
```

## Configuration

### Environment Variables

**FastAPI Container:**
- `DATABASE_URL` - PostgreSQL connection string
- `CORS_ORIGINS` - Allowed CORS origins (JSON array)

**PostgreSQL Container:**
- `POSTGRES_USER` - Database user
- `POSTGRES_PASSWORD` - Database password
- `POSTGRES_DB` - Database name

### Changing Database Credentials

Edit `docker-compose.yml`:

```yaml
postgres:
  environment:
    POSTGRES_USER: your_user
    POSTGRES_PASSWORD: your_password
    POSTGRES_DB: your_database

fastapi:
  environment:
    DATABASE_URL: postgresql+asyncpg://your_user:your_password@postgres:5432/your_database
```

## Development vs Production

### Current Setup (Development-Friendly)

- FastAPI port 8000 exposed for debugging
- Passwords in docker-compose.yml
- Migrations run automatically on startup

### Production Recommendations

1. **Use Docker Secrets or Environment Files**:
   ```bash
   # Create .env file
   echo "POSTGRES_PASSWORD=<strong-random-password>" > .env

   # Update docker-compose.yml to use env_file
   services:
     postgres:
       env_file: .env
   ```

2. **Run Migrations Separately**:
   ```bash
   # Don't auto-run migrations in CMD
   # Instead, run manually:
   docker-compose exec fastapi alembic upgrade head
   ```

3. **Remove Debug Port**:
   Remove `ports: - "8000:8000"` from fastapi service

4. **Use Reverse Proxy**:
   Add Traefik or Caddy for HTTPS and domain routing

5. **Backup Database**:
   ```bash
   # Backup
   docker-compose exec postgres pg_dump -U recipefirst recipefirst > backup.sql

   # Restore
   docker-compose exec -T postgres psql -U recipefirst recipefirst < backup.sql
   ```

## Troubleshooting

### Container Won't Start

```bash
# Check container status
docker-compose ps

# Check logs for errors
docker-compose logs
```

### Database Connection Failed

```bash
# Check PostgreSQL is healthy
docker-compose ps postgres

# Should show "healthy" status
# If not, check logs:
docker-compose logs postgres
```

### Migrations Failed

```bash
# Run migrations manually
docker-compose exec fastapi alembic upgrade head

# Check current migration version
docker-compose exec fastapi alembic current

# View migration history
docker-compose exec fastapi alembic history
```

### Frontend Can't Reach API

1. Check nginx configuration: `nginx.conf`
2. Verify API is running: `curl http://localhost:8000/health`
3. Check nginx logs: `docker-compose logs nginx`

### Reset Everything

```bash
# Stop and remove all containers, volumes, and images
docker-compose down -v --rmi all

# Rebuild from scratch
docker-compose up --build
```

## Scaling

### Horizontal Scaling (Multiple FastAPI Containers)

```bash
# Start 3 FastAPI containers
docker-compose up -d --scale fastapi=3

# Update nginx.conf to use upstream load balancing:
upstream fastapi_backend {
    server fastapi:8000;
}
```

Note: Requires nginx configuration changes for proper load balancing.

## Health Checks

All containers include health checks:

- **PostgreSQL**: `pg_isready` every 10s
- **FastAPI**: `curl http://localhost:8000/health` every 30s
- **Nginx**: Built-in nginx health check

View health status:
```bash
docker-compose ps
```

## Volumes

- **postgres_data**: Persists PostgreSQL database files
- Located at: `/var/lib/docker/volumes/recipefirst_postgres_data`

To backup volume:
```bash
docker run --rm -v recipefirst_postgres_data:/data -v $(pwd):/backup ubuntu tar czf /backup/postgres-backup.tar.gz /data
```

## Next Steps

1. ✅ Containers are running
2. ✅ Database is migrated
3. ✅ Application is accessible at http://localhost

Consider:
- Setting up HTTPS with Let's Encrypt
- Configuring domain name
- Setting up CI/CD pipeline
- Implementing automated backups
- Adding monitoring (Prometheus/Grafana)
- Setting up logging aggregation (ELK stack)

## Support

For issues or questions:
- Check logs: `docker-compose logs`
- Review this guide
- Check Docker/Docker Compose documentation
