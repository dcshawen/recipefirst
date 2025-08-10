# RecipeFirst

RecipeFirst is a SQLite-backed application for managing recipes, ingredients, food items, meals, and their relationships.

## Overview

`recipefirst` is a Python-based backend application for managing recipes and related data. It provides a RESTful API for interacting with a SQLite database, supporting operations such as creating, reading, updating, and deleting recipes. The project is organized into several modules for database access, routing, and server management.

## Capabilities

- **Database Management**: Uses SQLite for persistent storage of recipes and related data.
- **REST API Endpoints**: Exposes endpoints for CRUD operations on recipes and other entities.
- **Modular Design**: Code is organized into modules for database access (`db.py`), API routing (`routes.py`), and server startup (`server.py`).
- **Schema Management**: Includes SQL schema files for initializing and patching the database.
- **Testing**: Contains HTTP request files for manual endpoint testing.

### Main Modules

- `data/db.py`: Handles database connections and queries.
- `data/routes.py`: Defines API routes and logic for handling requests.
- `data/server.py`: Starts the API server (likely using Flask or FastAPI).
- `data/schema.sql`: SQL schema for initializing the database.
- `data/patch.sql`: SQL patch for updating the database schema.
- `data/recipefirst.db`: SQLite database file.
- `test/rest/endpoints.http`: Example HTTP requests for testing API endpoints.

## Installation Guide

### Prerequisites

- Python 3.10 or newer
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```sh
   git clone https://github.com/dcshawen/recipefirst.git
   cd recipefirst
   ```

2. **Create and activate a virtual environment (recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is missing, install Flask or FastAPI as needed:)*
   ```sh
   pip install flask
   # or
   pip install fastapi uvicorn
   ```

4. **Initialize the database**
   - The database file (`data/recipefirst.db`) may already exist. To initialize a new database, run the SQL in `data/schema.sql` using a SQLite client:
     ```sh
     sqlite3 data/recipefirst.db < data/schema.sql
     ```
   - To apply patches, use:
     ```sh
     sqlite3 data/recipefirst.db < data/patch.sql
     ```

5. **Run the server**
   ```sh
   python data/server.py
   ```
   *(Or use the appropriate command for FastAPI/Uvicorn if applicable:)*
   ```sh
   uvicorn data.server:app --reload
   ```

## Usage Notes

- **API Endpoints**: See `test/rest/endpoints.http` for example requests. You can use tools like [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for VS Code, [Postman](https://www.postman.com/), or `curl` to interact with the API.
- **Database**: The SQLite database is stored at `data/recipefirst.db`. Schema and patch files are provided for setup and migration.
- **Configuration**: Environment variables or configuration files may be used for advanced settings (see code for details).
- **Testing**: Use the provided `.http` files or write your own tests to verify endpoints.

## Project Structure

```
recipefirst/
├── data/
│   ├── db.py
│   ├── patch.sql
│   ├── recipefirst.db
│   ├── routes.py
│   ├── schema.sql
│   ├── server.py
│   └── __pycache__/
├── instances/
│   └── recipefirst.db
├── test/
│   └── rest/
│       └── endpoints.http
├── README.md
└── .gitignore
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

See LICENSE file for details (if available).

- Store and categorize recipes, ingredients, meals, and food items
- Track recipe instructions and ingredient quantities
- Organize items with flexible category tagging
- Supports meal planning and composition

## Project Structure

- `schema.sql` — Database schema definition
- `data/patch.sql` — Test/demo data for development
- `data/db.py` — Database initialization and patching utilities
- `data/instances/` — Folder for SQLite database files

## Quick Start

1. **Install Python 3.8+**
2. **Initialize the database:**
   ```bash
   python data/db.py
   ```
   This creates `data/instances/recipefirst.db` using `schema.sql`.

3. **Load test data:**
   ```python
   from data.db import patch_db
   patch_db()
   ```
   This executes `patch.sql` to populate the database.

## Development

- Edit `schema.sql` to change the database structure.
- Add or modify test data in `data/patch.sql`.
- Use `data/db.py` for database setup and schema inspection.

## License

MIT License (see LICENSE file if present)
