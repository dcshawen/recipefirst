# RecipeFirst Docker Development Guide

This guide explains how to run RecipeFirst using Docker Compose with a 3-container architecture:
- **PostgreSQL** - Development database
- **FastAPI** - Backend API server with hot-reload
- **Frontend** - Vite dev server with hot-reload (HMR)

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
5. Start the FastAPI server with hot-reload
6. Build and start frontend container with Vite dev server (hot-reload enabled)

**First-time startup includes:**
- 21 measurement units (cup, tablespoon, gram, etc.)
- 25 categories (meal types, cuisines, dietary preferences)
- 41 basic ingredients (salt, flour, chicken, etc.)

The database is automatically initialized and ready to use!

### 2. Access the Application

- **Frontend**: http://localhost:5173 (Vite dev server with hot-reload)
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

### 3. View Logs

```bash
# View all logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f frontend
docker-compose logs -f fastapi
docker-compose logs -f postgres
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

## Hot Reload Development

Both the backend and frontend support hot-reload for rapid development:

### Frontend (Vite)
- Edit files in `www/src/`
- Browser automatically updates thanks to Vite's Hot Module Replacement (HMR)
- Source files are mounted as volumes, so changes reflect immediately

### Backend (FastAPI)
- Edit files in `data/`
- FastAPI automatically restarts when Python files change
- Source files are mounted as volumes

### Clearing Browser Cache

If you see old content after stopping containers (this indicates browser cache, not actual running services):
1. Hard refresh: `Ctrl+Shift+R` (Windows/Linux) or `Cmd+Shift+R` (Mac)
2. Clear cache in browser dev tools (F12 → Application → Clear storage)
3. Or use incognito/private browsing mode

**To verify nothing is running:**
```bash
# Check Docker containers
docker ps -a

# Check ports (should show nothing on 5173 or 8000)
netstat -an | grep -E ":(5173|8000)" | grep LISTEN
```

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
│  Frontend (Port 5173)                               │
│  - Vite dev server with HMR                         │
│  - Proxies /api/* to FastAPI:8000                   │
│  - Source mounted for hot-reload                    │
└─────────────────┬───────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────┐
│  FastAPI (Port 8000)                                │
│  - REST API endpoints                               │
│  - SQLAlchemy ORM + async                           │
│  - Auto-runs Alembic migrations on startup          │
│  - Source mounted for hot-reload                    │
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

1. Check Vite proxy configuration in `www/vite.config.js`
2. Verify API is running: `curl http://localhost:8000/health`
3. Check frontend logs: `docker-compose logs frontend`
4. Ensure containers are on same network: `docker network inspect recipefirst_recipefirst`

### Reset Everything

```bash
# Stop and remove all containers, volumes, and images
docker-compose down -v --rmi all

# Rebuild from scratch
docker-compose up --build
```

## Production Deployment

This setup is for **development only**. For production:

- Use `Dockerfile.frontend` (builds static files served by nginx)
- Create a separate `docker-compose.prod.yml`  
- Remove volume mounts for source code
- Disable hot-reload on backend (`RELOAD: "false"`)
- Set appropriate CORS origins
- Enable HTTPS/SSL
- Use environment-specific configuration

Production would use a multi-stage build that compiles Vue.js to static files and serves them via nginx on port 80.

## Health Checks

Containers include health checks:

- **PostgreSQL**: `pg_isready` every 10s
- **FastAPI**: Application startup validation
- **Frontend**: Vite dev server (auto-restarts on failure)

View container status:

- **PostgreSQL**: `pg_isready` every 10s
- **FastAPI**: Application health endpoint
- **Frontend**: Vite dev server (no health check needed in dev)

View container status:
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
