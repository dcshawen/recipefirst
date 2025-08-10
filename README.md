# RecipeFirst

RecipeFirst is a SQLite-backed application for managing recipes, ingredients, food items, meals, and their relationships.

## Features

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
