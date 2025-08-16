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

def _get_db_path():
    current_dir = Path(__file__).parent
    instances_dir = current_dir / 'instances'
    db_path = instances_dir / 'recipefirst.db'
    return str(db_path)

# Recipes
def get_all_recipes():
    db_path = _get_db_path()
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        recipes = conn.execute("SELECT * FROM Recipe").fetchall()
        result = []
        for recipe in recipes:
            recipe_dict = dict(recipe)
            recipe_id = recipe_dict["recipe_id"]
            # Ingredients
            ingredients = conn.execute("""
                SELECT ri.*, 
                       i.ingredient_name, i.ingredient_description, i.ingredient_notes,
                       f.fooditem_name, f.fooditem_description,
                       ut.unit_type
                FROM RecipeIngredient ri
                LEFT JOIN Ingredient i ON ri.ri_ingredient_id = i.ingredient_id
                LEFT JOIN FoodItem f ON ri.ri_fooditem_id = f.fooditem_id
                LEFT JOIN UnitType ut ON ri.ri_unit_type_id = ut.id
                WHERE ri.ri_recipe_id = ?
            """, (recipe_id,)).fetchall()
            recipe_dict["ingredients"] = [dict(row) for row in ingredients]
            # Instructions
            instructions = conn.execute("""
                SELECT step_number, instruction_text
                FROM RecipeInstruction
                WHERE recipe_id = ?
                ORDER BY step_number ASC
            """, (recipe_id,)).fetchall()
            recipe_dict["instructions"] = [dict(row) for row in instructions]
            # Categories
            categories = conn.execute("""
                SELECT c.category_id, c.category_name, c.category_description
                FROM RecipeCategory rc
                JOIN Category c ON rc.category_id = c.category_id
                WHERE rc.recipe_id = ?
            """, (recipe_id,)).fetchall()
            recipe_dict["categories"] = [dict(row) for row in categories]
            result.append(recipe_dict)
        return result

def get_recipe_by_id(recipe_id):
    db_path = _get_db_path()
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        recipe = conn.execute("SELECT * FROM Recipe WHERE recipe_id = ?", (recipe_id,)).fetchone()
        if not recipe:
            return None
        recipe_dict = dict(recipe)
        # Ingredients
        ingredients = conn.execute("""
            SELECT ri.*, 
                   i.ingredient_name, i.ingredient_description, i.ingredient_notes,
                   f.fooditem_name, f.fooditem_description,
                   ut.unit_type
            FROM RecipeIngredient ri
            LEFT JOIN Ingredient i ON ri.ri_ingredient_id = i.ingredient_id
            LEFT JOIN FoodItem f ON ri.ri_fooditem_id = f.fooditem_id
            LEFT JOIN UnitType ut ON ri.ri_unit_type_id = ut.id
            WHERE ri.ri_recipe_id = ?
        """, (recipe_id,)).fetchall()
        recipe_dict["ingredients"] = [dict(row) for row in ingredients]
        # Instructions
        instructions = conn.execute("""
            SELECT step_number, instruction_text
            FROM RecipeInstruction
            WHERE recipe_id = ?
            ORDER BY step_number ASC
        """, (recipe_id,)).fetchall()
        recipe_dict["instructions"] = [dict(row) for row in instructions]
        # Categories
        categories = conn.execute("""
            SELECT c.category_id, c.category_name, c.category_description
            FROM RecipeCategory rc
            JOIN Category c ON rc.category_id = c.category_id
            WHERE rc.recipe_id = ?
        """, (recipe_id,)).fetchall()
        recipe_dict["categories"] = [dict(row) for row in categories]
        return recipe_dict

def create_recipe(recipe_data):
    db_path = _get_db_path()
    # Map incoming keys to DB columns
    mapped_data = {}
    category_ids = None
    # recipe_fooditem_id is required and must be unique
    for k, v in recipe_data.items():
        if k == "name":
            mapped_data["recipe_name"] = v
        elif k == "description":
            mapped_data["recipe_description"] = v
        elif k == "fooditem_id":
            mapped_data["recipe_fooditem_id"] = v
        elif k == "category_id":
            category_ids = v
        else:
            mapped_data[k] = v
    # Ensure required fields are present
    if "recipe_name" not in mapped_data or "recipe_fooditem_id" not in mapped_data:
        raise ValueError("Missing required fields: recipe_name and recipe_fooditem_id")
    with sqlite3.connect(db_path) as conn:
        columns = ', '.join(mapped_data.keys())
        placeholders = ', '.join(['?'] * len(mapped_data))
        sql = f"INSERT INTO Recipe ({columns}) VALUES ({placeholders})"
        cur = conn.execute(sql, tuple(mapped_data.values()))
        conn.commit()
        recipe_id = cur.lastrowid
        # Handle category_id(s)
        if category_ids is not None:
            if isinstance(category_ids, (list, tuple)):
                ids = category_ids
            else:
                ids = [category_ids]
            for cid in ids:
                conn.execute(
                    "INSERT INTO RecipeCategory (recipe_id, category_id) VALUES (?, ?)",
                    (recipe_id, cid)
                )
            conn.commit()
        return get_recipe_by_id(recipe_id)

def update_recipe(recipe_id, recipe_data):
    db_path = _get_db_path()
    mapped_data = {}
    for k, v in recipe_data.items():
        if k == "name":
            mapped_data["recipe_name"] = v
        elif k == "description":
            mapped_data["recipe_description"] = v
        elif k == "fooditem_id":
            mapped_data["recipe_fooditem_id"] = v
        else:
            mapped_data[k] = v
    # Only update fields that exist in the schema
    allowed_fields = {"recipe_name", "recipe_description", "recipe_fooditem_id"}
    mapped_data = {k: v for k, v in mapped_data.items() if k in allowed_fields}
    if not mapped_data:
        return False
    with sqlite3.connect(db_path) as conn:
        sets = ', '.join([f"{k}=?" for k in mapped_data.keys()])
        sql = f"UPDATE Recipe SET {sets} WHERE recipe_id=?"
        cur = conn.execute(sql, tuple(mapped_data.values()) + (recipe_id,))
        conn.commit()
        return cur.rowcount > 0

def delete_recipe(recipe_id):
    db_path = _get_db_path()
    with sqlite3.connect(db_path) as conn:
        cur = conn.execute("DELETE FROM Recipe WHERE recipe_id=?", (recipe_id,))
        conn.commit()
        return cur.rowcount > 0

# Ingredients
def get_all_ingredients():
    db_path = _get_db_path()
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT * FROM Ingredient").fetchall()
        return [dict(row) for row in rows]

def get_ingredient_by_id(ingredient_id):
    db_path = _get_db_path()
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute("SELECT * FROM Ingredient WHERE ingredient_id = ?", (ingredient_id,)).fetchone()
        return dict(row) if row else None

def create_ingredient(ingredient_data):
    db_path = _get_db_path()
    # ingredient_name is required and must be unique
    if "ingredient_name" not in ingredient_data:
        raise ValueError("Missing required field: ingredient_name")
    with sqlite3.connect(db_path) as conn:
        columns = ', '.join(ingredient_data.keys())
        placeholders = ', '.join(['?'] * len(ingredient_data))
        sql = f"INSERT INTO Ingredient ({columns}) VALUES ({placeholders})"
        cur = conn.execute(sql, tuple(ingredient_data.values()))
        conn.commit()
        return get_ingredient_by_id(cur.lastrowid)

def update_ingredient(ingredient_id, ingredient_data):
    db_path = _get_db_path()
    allowed_fields = {"ingredient_name"}
    ingredient_data = {k: v for k, v in ingredient_data.items() if k in allowed_fields}
    if not ingredient_data:
        return False
    with sqlite3.connect(db_path) as conn:
        sets = ', '.join([f"{k}=?" for k in ingredient_data.keys()])
        sql = f"UPDATE Ingredient SET {sets} WHERE ingredient_id=?"
        cur = conn.execute(sql, tuple(ingredient_data.values()) + (ingredient_id,))
        conn.commit()
        return cur.rowcount > 0

def delete_ingredient(ingredient_id):
    db_path = _get_db_path()
    with sqlite3.connect(db_path) as conn:
        cur = conn.execute("DELETE FROM Ingredient WHERE ingredient_id=?", (ingredient_id,))
        conn.commit()
        return cur.rowcount > 0

# Recipe Ingredients
def get_recipe_ingredients(recipe_id):
    db_path = _get_db_path()
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT * FROM RecipeIngredient WHERE ri_recipe_id = ?",
            (recipe_id,)
        ).fetchall()
        return [dict(row) for row in rows]

def add_ingredient_to_recipe(recipe_id, ingredient_data):
    db_path = _get_db_path()
    # Required: ri_recipe_id, ri_unit_type_id, ri_quantity, and exactly one of ri_ingredient_id or ri_fooditem_id
    required = {"ri_unit_type_id", "ri_quantity"}
    if not any(k in ingredient_data for k in ("ri_ingredient_id", "ri_fooditem_id")):
        raise ValueError("Must provide either ri_ingredient_id or ri_fooditem_id")
    if not all(k in ingredient_data for k in required):
        raise ValueError("Missing required fields for RecipeIngredient")
    columns = ['ri_recipe_id'] + list(ingredient_data.keys())
    placeholders = ', '.join(['?'] * len(columns))
    sql = f"INSERT INTO RecipeIngredient ({', '.join(columns)}) VALUES ({placeholders})"
    values = (recipe_id,) + tuple(ingredient_data.values())
    with sqlite3.connect(db_path) as conn:
        cur = conn.execute(sql, values)
        conn.commit()
        return get_recipe_ingredients(recipe_id)

def update_recipe_ingredient(recipe_id, ingredient_id, update_data):
    db_path = _get_db_path()
    allowed_fields = {"ri_unit_type_id", "ri_quantity"}
    update_data = {k: v for k, v in update_data.items() if k in allowed_fields}
    if not update_data:
        return False
    with sqlite3.connect(db_path) as conn:
        sets = ', '.join([f"{k}=?" for k in update_data.keys()])
        sql = f"UPDATE RecipeIngredient SET {sets} WHERE ri_recipe_id=? AND ri_ingredient_id=?"
        cur = conn.execute(sql, tuple(update_data.values()) + (recipe_id, ingredient_id))
        conn.commit()
        return cur.rowcount > 0

def remove_ingredient_from_recipe(recipe_id, ingredient_id):
    db_path = _get_db_path()
    with sqlite3.connect(db_path) as conn:
        cur = conn.execute("DELETE FROM RecipeIngredient WHERE ri_recipe_id=? AND ri_ingredient_id=?", (recipe_id, ingredient_id))
        conn.commit()
        return cur.rowcount > 0

# Categories
def get_all_categories():
    db_path = _get_db_path()
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT * FROM Category").fetchall()
        return [dict(row) for row in rows]

def get_category_by_id(category_id):
    db_path = _get_db_path()
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute("SELECT * FROM Category WHERE category_id = ?", (category_id,)).fetchone()
        return dict(row) if row else None

def create_category(category_data):
    db_path = _get_db_path()
    # category_name is required and must be unique
    if "category_name" not in category_data:
        raise ValueError("Missing required field: category_name")
    with sqlite3.connect(db_path) as conn:
        columns = ', '.join(category_data.keys())
        placeholders = ', '.join(['?'] * len(category_data))
        sql = f"INSERT INTO Category ({columns}) VALUES ({placeholders})"
        cur = conn.execute(sql, tuple(category_data.values()))
        conn.commit()
        return get_category_by_id(cur.lastrowid)

def update_category(category_id, category_data):
    db_path = _get_db_path()
    allowed_fields = {"category_name", "category_description", "parent_category_id"}
    category_data = {k: v for k, v in category_data.items() if k in allowed_fields}
    if not category_data:
        return False
    with sqlite3.connect(db_path) as conn:
        sets = ', '.join([f"{k}=?" for k in category_data.keys()])
        sql = f"UPDATE Category SET {sets} WHERE category_id=?"
        cur = conn.execute(sql, tuple(category_data.values()) + (category_id,))
        conn.commit()
        return cur.rowcount > 0

def delete_category(category_id):
    db_path = _get_db_path()
    with sqlite3.connect(db_path) as conn:
        cur = conn.execute("DELETE FROM Category WHERE category_id=?", (category_id,))
        conn.commit()
        return cur.rowcount > 0

# Food Items
def get_all_food_items():
    db_path = _get_db_path()
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT * FROM FoodItem").fetchall()
        return [dict(row) for row in rows]

def get_food_item_by_id(fooditem_id):
    db_path = _get_db_path()
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute("SELECT * FROM FoodItem WHERE fooditem_id = ?", (fooditem_id,)).fetchone()
        return dict(row) if row else None

def create_food_item(food_item_data):
    db_path = _get_db_path()
    # fooditem_name is required
    if "fooditem_name" not in food_item_data:
        raise ValueError("Missing required field: fooditem_name")
    with sqlite3.connect(db_path) as conn:
        columns = ', '.join(food_item_data.keys())
        placeholders = ', '.join(['?'] * len(food_item_data))
        sql = f"INSERT INTO FoodItem ({columns}) VALUES ({placeholders})"
        cur = conn.execute(sql, tuple(food_item_data.values()))
        conn.commit()
        return get_food_item_by_id(cur.lastrowid)

def update_food_item(fooditem_id, food_item_data):
    db_path = _get_db_path()
    allowed_fields = {"fooditem_name", "fooditem_description"}
    food_item_data = {k: v for k, v in food_item_data.items() if k in allowed_fields}
    if not food_item_data:
        return False
    with sqlite3.connect(db_path) as conn:
        sets = ', '.join([f"{k}=?" for k in food_item_data.keys()])
        sql = f"UPDATE FoodItem SET {sets} WHERE fooditem_id=?"
        cur = conn.execute(sql, tuple(food_item_data.values()) + (fooditem_id,))
        conn.commit()
        return cur.rowcount > 0

def delete_food_item(fooditem_id):
    db_path = _get_db_path()
    with sqlite3.connect(db_path) as conn:
        cur = conn.execute("DELETE FROM FoodItem WHERE fooditem_id=?", (fooditem_id,))
        conn.commit()
        return cur.rowcount > 0

# Meals
def get_all_meals():
    db_path = _get_db_path()
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT * FROM Meal").fetchall()
        return [dict(row) for row in rows]

def get_meal_by_id(meal_id):
    db_path = _get_db_path()
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute("SELECT * FROM Meal WHERE meal_id = ?", (meal_id,)).fetchone()
        return dict(row) if row else None

def create_meal(meal_data):
    db_path = _get_db_path()
    # meal_name is required
    if "meal_name" not in meal_data:
        raise ValueError("Missing required field: meal_name")
    with sqlite3.connect(db_path) as conn:
        columns = ', '.join(meal_data.keys())
        placeholders = ', '.join(['?'] * len(meal_data))
        sql = f"INSERT INTO Meal ({columns}) VALUES ({placeholders})"
        cur = conn.execute(sql, tuple(meal_data.values()))
        conn.commit()
        return get_meal_by_id(cur.lastrowid)

def update_meal(meal_id, meal_data):
    db_path = _get_db_path()
    allowed_fields = {"meal_name", "meal_description"}
    meal_data = {k: v for k, v in meal_data.items() if k in allowed_fields}
    if not meal_data:
        return False
    with sqlite3.connect(db_path) as conn:
        sets = ', '.join([f"{k}=?" for k in meal_data.keys()])
        sql = f"UPDATE Meal SET {sets} WHERE meal_id=?"
        cur = conn.execute(sql, tuple(meal_data.values()) + (meal_id,))
        conn.commit()
        return cur.rowcount > 0

def delete_meal(meal_id):
    db_path = _get_db_path()
    with sqlite3.connect(db_path) as conn:
        cur = conn.execute("DELETE FROM Meal WHERE meal_id=?", (meal_id,))
        conn.commit()
        return cur.rowcount > 0

# Utility
def search_recipes(q):
    db_path = _get_db_path()
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT * FROM Recipe WHERE recipe_name LIKE ?", (f"%{q}%",)).fetchall()
        return [dict(row) for row in rows]

def get_recipes_by_category(category_id):
    db_path = _get_db_path()
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("""
            SELECT r.* FROM Recipe r
            JOIN RecipeCategory rc ON r.recipe_id = rc.recipe_id
            WHERE rc.category_id = ?
        """, (category_id,)).fetchall()
        return [dict(row) for row in rows]
