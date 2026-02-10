#!/bin/bash
# RecipeFirst Docker Management Script

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Helper functions
print_header() {
    echo -e "${GREEN}===================================${NC}"
    echo -e "${GREEN}$1${NC}"
    echo -e "${GREEN}===================================${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

# Commands
cmd_build() {
    print_header "Building Docker Images"
    docker-compose build
    print_success "Build complete"
}

cmd_up() {
    print_header "Starting Containers"
    docker-compose up -d
    print_success "Containers started"
    echo ""
    echo "Access the application at:"
    echo "  Frontend: http://localhost"
    echo "  API: http://localhost/api"
    echo "  API Direct: http://localhost:8000"
}

cmd_down() {
    print_header "Stopping Containers"
    docker-compose down
    print_success "Containers stopped"
}

cmd_logs() {
    service=${1:-}
    if [ -z "$service" ]; then
        docker-compose logs -f
    else
        docker-compose logs -f "$service"
    fi
}

cmd_status() {
    print_header "Container Status"
    docker-compose ps
}

cmd_restart() {
    print_header "Restarting Containers"
    docker-compose restart
    print_success "Containers restarted"
}

cmd_clean() {
    print_warning "This will remove all containers and volumes (DATA WILL BE LOST!)"
    read -p "Are you sure? (yes/no): " confirm
    if [ "$confirm" = "yes" ]; then
        print_header "Cleaning Everything"
        docker-compose down -v --rmi all
        print_success "Clean complete"
    else
        print_warning "Clean cancelled"
    fi
}

cmd_migrate() {
    print_header "Running Database Migration"
    export DATABASE_URL="postgresql+asyncpg://recipefirst:recipefirst123@localhost:5432/recipefirst"
    python migrate_data.py
}

cmd_seed() {
    print_header "Seeding Database with Starter Data"
    docker-compose exec fastapi python seed_data.py
}

cmd_shell_fastapi() {
    print_header "Opening FastAPI Shell"
    docker-compose exec fastapi /bin/bash
}

cmd_shell_postgres() {
    print_header "Opening PostgreSQL Shell"
    docker-compose exec postgres psql -U recipefirst -d recipefirst
}

cmd_backup() {
    print_header "Backing Up Database"
    timestamp=$(date +%Y%m%d_%H%M%S)
    filename="backup_${timestamp}.sql"
    docker-compose exec -T postgres pg_dump -U recipefirst recipefirst > "$filename"
    print_success "Backup saved to $filename"
}

cmd_restore() {
    backup_file=$1
    if [ -z "$backup_file" ]; then
        print_error "Usage: $0 restore <backup_file>"
        exit 1
    fi
    print_header "Restoring Database from $backup_file"
    docker-compose exec -T postgres psql -U recipefirst recipefirst < "$backup_file"
    print_success "Database restored"
}

cmd_help() {
    cat << EOF
RecipeFirst Docker Management Script

Usage: $0 <command> [options]

Commands:
  build           Build Docker images
  up              Start all containers
  down            Stop all containers
  restart         Restart all containers
  status          Show container status
  logs [service]  Show logs (optionally for specific service)
  seed            Populate database with starter data (units, categories, ingredients)
  migrate         Migrate data from SQLite to PostgreSQL
  clean           Remove all containers, volumes, and images (DESTRUCTIVE!)

  shell-fastapi   Open bash shell in FastAPI container
  shell-postgres  Open PostgreSQL shell

  backup          Backup PostgreSQL database to file
  restore <file>  Restore PostgreSQL database from backup file

  help            Show this help message

Examples:
  $0 up                    # Start all containers
  $0 seed                  # Add starter data to database
  $0 logs fastapi          # Show FastAPI logs
  $0 backup                # Backup database
  $0 restore backup.sql    # Restore from backup

EOF
}

# Main command router
case "${1:-help}" in
    build)
        cmd_build
        ;;
    up)
        cmd_up
        ;;
    down)
        cmd_down
        ;;
    restart)
        cmd_restart
        ;;
    status)
        cmd_status
        ;;
    logs)
        cmd_logs "$2"
        ;;
    seed)
        cmd_seed
        ;;
    migrate)
        cmd_migrate
        ;;
    clean)
        cmd_clean
        ;;
    shell-fastapi)
        cmd_shell_fastapi
        ;;
    shell-postgres)
        cmd_shell_postgres
        ;;
    backup)
        cmd_backup
        ;;
    restore)
        cmd_restore "$2"
        ;;
    help|--help|-h)
        cmd_help
        ;;
    *)
        print_error "Unknown command: $1"
        echo ""
        cmd_help
        exit 1
        ;;
esac
