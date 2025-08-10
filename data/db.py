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
    """
    # Get paths
    current_dir = Path(__file__).parent
    root_dir = current_dir.parent
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
    
    Returns:
        str: The SQL schema of the database.
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
    
    Returns:
        str: Path to the patched database file.
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

# Recipes
def get_all_recipes():
    return []

def get_recipe_by_id(id):
    return {"id": id, "name": "Sample Recipe"}

def create_recipe(recipe_data):
    return {"id": 1, "data": recipe_data}

def update_recipe(id, recipe_data):
    return True

def delete_recipe(id):
    return True

# Ingredients
def get_all_ingredients():
    return []

def get_ingredient_by_id(id):
    return {"id": id, "name": "Sample Ingredient"}

def create_ingredient(ingredient_data):
    return {"id": 1, "data": ingredient_data}

def update_ingredient(id, ingredient_data):
    return True

def delete_ingredient(id):
    return True

# Recipe Ingredients
def get_recipe_ingredients(id):
    return []

def add_ingredient_to_recipe(id, ingredient_data):
    return {"recipe_id": id, "ingredient": ingredient_data}

def update_recipe_ingredient(id, ingredient_id, update_data):
    return True

def remove_ingredient_from_recipe(id, ingredient_id):
    return True

# Categories
def get_all_categories():
    return []

def get_category_by_id(id):
    return {"id": id, "name": "Sample Category"}

def create_category(category_data):
    return {"id": 1, "data": category_data}

def update_category(id, category_data):
    return True

def delete_category(id):
    return True

# Food Items
def get_all_food_items():
    return []

def get_food_item_by_id(id):
    return {"id": id, "name": "Sample Food Item"}

def create_food_item(food_item_data):
    return {"id": 1, "data": food_item_data}

def update_food_item(id, food_item_data):
    return True

def delete_food_item(id):
    return True

# Meals
def get_all_meals():
    return []

def get_meal_by_id(id):
    return {"id": id, "name": "Sample Meal"}

def create_meal(meal_data):
    return {"id": 1, "data": meal_data}

def update_meal(id, meal_data):
    return True

def delete_meal(id):
    return True

# Utility
def search_recipes(q):
    return []

def get_recipes_by_category(category_id):
    return []
