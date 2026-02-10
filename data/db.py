"""
Database utility functions for RecipeFirst application.

This module provides database initialization, schema inspection, and patching utilities.
All CRUD operations have been migrated to crud.py using SQLAlchemy ORM.
"""

import sqlite3
import os
from pathlib import Path


def init_db(db_name='recipefirst.db'):
    """
    Initialize a new SQLite database by executing the schema.sql file.

    Args:
        db_name (str): Name of the database file. Default is 'recipefirst.db'.

    Returns:
        str: Path to the created database file.

    Example:
        >>> db_path = init_db('recipefirst.db')
        Database initialized at /path/to/instances/recipefirst.db
    """
    # Get paths
    current_dir = Path(__file__).parent
    instances_dir = current_dir / 'instances'
    os.makedirs(instances_dir, exist_ok=True)

    db_path = instances_dir / db_name
    schema_path = current_dir / 'schema.sql'

    if not schema_path.exists():
        raise FileNotFoundError(f"Schema file not found at {schema_path}")

    # Connect to the database
    with sqlite3.connect(db_path) as conn:
        # Read and execute the schema file
        with open(schema_path, 'r') as f:
            schema_sql = f.read()

        conn.executescript(schema_sql)

        print(f"Database initialized at {db_path}")
        return str(db_path)


def getDBSchema():
    """
    Get the schema of the database.

    Returns a list of SQL statements that define all tables, triggers,
    indices, and views in the database.

    Returns:
        list[str]: List of SQL CREATE statements from sqlite_master.

    Example:
        >>> schema = getDBSchema()
        >>> print(schema[0])  # First table definition
    """
    # Get the project root directory (parent of the data directory)
    root_dir = Path(__file__).parent.parent
    instances_dir = root_dir / 'data' / 'instances'
    db_path = instances_dir / 'recipefirst.db'

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Query the sqlite_master table to get all table creation statements
    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND sql IS NOT NULL")
    schema = cursor.fetchall()

    # Also get triggers, indices, and views
    cursor.execute("SELECT sql FROM sqlite_master WHERE type IN ('trigger', 'index', 'view') AND sql IS NOT NULL")
    schema.extend(cursor.fetchall())

    conn.close()
    return [item[0] for item in schema if item[0] is not None]


def patch_db():
    """
    Apply patches to the database by executing the patch.sql file.

    Useful for adding test data or making schema modifications after
    initial database creation.

    Returns:
        str: Path to the patched database file.

    Raises:
        FileNotFoundError: If database or patch.sql file doesn't exist.

    Example:
        >>> patch_db()
        Database patched successfully at /path/to/instances/recipefirst.db
    """
    # Get paths
    current_dir = Path(__file__).parent
    instances_dir = current_dir / 'instances'
    db_path = instances_dir / 'recipefirst.db'
    patch_path = current_dir / 'patch.sql'

    if not db_path.exists():
        raise FileNotFoundError(f"Database file not found at {db_path}. Please run init_db() first.")

    if not patch_path.exists():
        raise FileNotFoundError(f"Patch file not found at {patch_path}")

    # Connect to the database
    with sqlite3.connect(db_path) as conn:
        # Read and execute the patch file
        with open(patch_path, 'r') as f:
            patch_sql = f.read()

        conn.executescript(patch_sql)

        print(f"Database patched successfully at {db_path}")
        return str(db_path)


def _get_db_path():
    """
    Get the path to the database file.

    Internal helper function to get consistent database path across modules.

    Returns:
        str: Absolute path to the recipefirst.db file.
    """
    current_dir = Path(__file__).parent
    instances_dir = current_dir / 'instances'
    db_path = instances_dir / 'recipefirst.db'
    return str(db_path)


# ============================================================================
# NOTE: All CRUD operations have been migrated to SQLAlchemy ORM
# ============================================================================
#
# The following functions have been replaced and are now in crud.py:
#
# Recipe Operations:
#   - get_all_recipes() → crud.get_all_recipes(session)
#   - get_recipe_by_id(id) → crud.get_recipe_by_id(session, id)
#   - create_recipe(data) → crud.create_recipe(session, data)
#   - update_recipe(id, data) → crud.update_recipe(session, id, data)
#   - delete_recipe(id) → crud.delete_recipe(session, id)
#
# Ingredient Operations:
#   - get_all_ingredients() → crud.get_all_ingredients(session)
#   - get_ingredient_by_id(id) → crud.get_ingredient_by_id(session, id)
#   - create_ingredient(data) → crud.create_ingredient(session, data)
#   - update_ingredient(id, data) → crud.update_ingredient(session, id, data)
#   - delete_ingredient(id) → crud.delete_ingredient(session, id)
#
# RecipeIngredient Operations:
#   - get_recipe_ingredients(id) → crud.get_recipe_ingredients(session, id)
#   - add_ingredient_to_recipe(id, data) → crud.add_ingredient_to_recipe(session, id, data)
#   - update_recipe_ingredient(id, ing_id, data) → crud.update_recipe_ingredient(session, id, ing_id, data)
#   - remove_ingredient_from_recipe(id, ing_id) → crud.remove_ingredient_from_recipe(session, id, ing_id)
#
# Category Operations:
#   - get_all_categories() → crud.get_all_categories(session)
#   - get_category_by_id(id) → crud.get_category_by_id(session, id)
#   - create_category(data) → crud.create_category(session, data)
#   - update_category(id, data) → crud.update_category(session, id, data)
#   - delete_category(id) → crud.delete_category(session, id)
#
# FoodItem Operations:
#   - get_all_food_items() → crud.get_all_food_items(session)
#   - get_food_item_by_id(id) → crud.get_food_item_by_id(session, id)
#   - create_food_item(data) → crud.create_food_item(session, data)
#   - update_food_item(id, data) → crud.update_food_item(session, id, data)
#   - delete_food_item(id) → crud.delete_food_item(session, id)
#
# Meal Operations:
#   - get_all_meals() → crud.get_all_meals(session)
#   - get_meal_by_id(id) → crud.get_meal_by_id(session, id)
#   - create_meal(data) → crud.create_meal(session, data)
#   - update_meal(id, data) → crud.update_meal(session, id, data)
#   - delete_meal(id) → crud.delete_meal(session, id)
#
# UnitType Operations:
#   - get_all_unit_types() → crud.get_all_unit_types(session)
#   - get_unit_type_by_id(id) → crud.get_unit_type_by_id(session, id)
#   - create_unit_type(data) → crud.create_unit_type(session, data)
#   - update_unit_type(id, data) → crud.update_unit_type(session, id, data)
#   - delete_unit_type(id) → crud.delete_unit_type(session, id)
#
# Search Operations:
#   - search_recipes(query) → crud.search_recipes(session, query)
#   - search_meals(query) → crud.search_meals(session, query)
#   - search_food_items(query) → crud.search_food_items(session, query)
#   - search_ingredients(query) → crud.search_ingredients(session, query)
#
# Utility Operations:
#   - get_recipes_by_category(id) → crud.get_recipes_by_category(session, id)
#   - get_recipes_by_food_item_id(id) → crud.get_recipes_by_food_item_id(session, id)
#
# Benefits of SQLAlchemy ORM:
#   ✓ Type safety with IDE autocomplete
#   ✓ Automatic relationship management
#   ✓ N+1 query prevention with eager loading (301 queries → 5 queries)
#   ✓ Better maintainability and extensibility
#   ✓ Transaction management with automatic rollback
#   ✓ Database-agnostic queries (easily switch from SQLite to PostgreSQL)
#
# For more information, see:
#   - data/models.py - ORM model definitions
#   - data/crud.py - All database operations
#   - data/database.py - Engine and session configuration
#   - data/routes.py - API endpoints using SQLAlchemy
#
# ============================================================================
