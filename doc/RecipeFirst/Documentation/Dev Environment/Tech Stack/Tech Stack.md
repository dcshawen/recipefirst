# Summary

RecipeFirst is built on the following technologies

## Operating System

## AWS

- Linux EC2
- The following options may be mutually exclusive, or at least experience little-to-no benefit from using both
	- Use Lambda / automation scripts to stop instanc.es during off-hours
	- Use spot instances
- Setup proper permissions via IAM Roles

## Data Layer
- FastAPI
- API Endpoints and backend routing
- sqlite3
- Database engine

## Presentation Layer
- VueJS
- Frontend Framework and routing
- TailwindCSS
- It was down to Tailwind or Bootstrap and I think Tailwind is just a better choice for this. I'd rather the deeper configurability than the pre-built components.