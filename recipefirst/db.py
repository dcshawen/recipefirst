import sqlite3
from datetime import datetime

import click
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
        # Enable foreign key constraints
        g.db.execute('PRAGMA foreign_keys = ON')
    
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    
    try:
        # Create tables first
        with current_app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf8'))
         
        db.commit()
        click.echo('Database schema created successfully.')
    except Exception as e:
        db.rollback()
        click.echo(f'Error creating database: {e}')
        raise

def patch_db():
    db = get_db()
    
    try:
        with current_app.open_resource('patch.sql') as f:
            db.executescript(f.read().decode('utf8'))
        db.commit()
        click.echo('Database patched successfully.')
    except Exception as e:
        db.rollback()
        click.echo(f'Error patching database: {e}')
        raise


@click.command('db-init')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

@click.command('db-patch')
def patch_db_command():
    """Patch the database."""
    patch_db()
    click.echo('Patch the database.')


sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(patch_db_command)
    
# Data Operations
def getIngredients(limit = 0):
		"""Fetch all ingredients."""
		db = get_db()
		ingredients = db.execute('SELECT * FROM Ingredient').fetchall()
		return [dict(row) for row in ingredients]

def getIngredient(ingredient_id):
		"""Fetch a single ingredient by ID."""
		db = get_db()
		ingredient = db.execute('SELECT * FROM Ingredient WHERE ingredient_id = ?', (ingredient_id,)).fetchone()
		if ingredient is None:
			return "Ingredient not found", 404
		return dict(ingredient)

def getUnits():
    db = get_db()
    rows = db.execute('SELECT * FROM Units').fetchall()
    return [dict(row) for row in rows]

def getUnit(unit_id):
    db = get_db()
    row = db.execute('SELECT * FROM Units WHERE unit_id = ?', (unit_id,)).fetchone()
    return dict(row) if row else None

def getComponents():
    db = get_db()
    rows = db.execute('SELECT * FROM Component').fetchall()
    return [dict(row) for row in rows]

def getComponent(component_id):
    db = get_db()
    row = db.execute('SELECT * FROM Component WHERE component_id = ?', (component_id,)).fetchone()
    return dict(row) if row else None

def getRecipes():
    db = get_db()
    rows = db.execute('SELECT * FROM Recipe').fetchall()
    return [dict(row) for row in rows]

def getRecipe(recipe_id):
    db = get_db()
    row = db.execute('SELECT * FROM Recipe WHERE recipe_id = ?', (recipe_id,)).fetchone()
    return dict(row) if row else None

def getMeals():
    db = get_db()
    rows = db.execute('SELECT * FROM Meal').fetchall()
    return [dict(row) for row in rows]

def getMeal(meal_id):
    db = get_db()
    row = db.execute('SELECT * FROM Meal WHERE meal_id = ?', (meal_id,)).fetchone()
    return dict(row) if row else None

def getRecipeComponents():
    db = get_db()
    rows = db.execute('SELECT * FROM RecipeComponent').fetchall()
    return [dict(row) for row in rows]

def getRecipeComponent(recipe_id, component_id):
    db = get_db()
    row = db.execute(
        'SELECT * FROM RecipeComponent WHERE recipe_id = ? AND component_id = ?', 
        (recipe_id, component_id)
    ).fetchone()
    return dict(row) if row else None

def getComponentIngredients():
    db = get_db()
    rows = db.execute('SELECT * FROM ComponentIngredient').fetchall()
    return [dict(row) for row in rows]

def getComponentIngredient(component_id, ingredient_id):
    db = get_db()
    row = db.execute(
        'SELECT * FROM ComponentIngredient WHERE component_id = ? AND ingredient_id = ?', 
        (component_id, ingredient_id)
    ).fetchone()
    return dict(row) if row else None

def getMealComponents():
    db = get_db()
    rows = db.execute('SELECT * FROM MealComponent').fetchall()
    return [dict(row) for row in rows]

def getMealComponent(meal_id, component_id):
    db = get_db()
    row = db.execute(
        'SELECT * FROM MealComponent WHERE meal_id = ? AND component_id = ?', 
        (meal_id, component_id)
    ).fetchone()
    return dict(row) if row else None

def getPantries():
    db = get_db()
    rows = db.execute('SELECT * FROM Pantry').fetchall()
    return [dict(row) for row in rows]

def getPantry(pantry_id):
    db = get_db()
    row = db.execute('SELECT * FROM Pantry WHERE pantry_id = ?', (pantry_id,)).fetchone()
    return dict(row) if row else None

def getPantryComponents():
    db = get_db()
    rows = db.execute('SELECT * FROM PantryComponent').fetchall()
    return [dict(row) for row in rows]

def getPantryComponent(pantry_id, component_id):
    db = get_db()
    row = db.execute(
        'SELECT * FROM PantryComponent WHERE pantry_id = ? AND component_id = ?', 
        (pantry_id, component_id)
    ).fetchone()
    return dict(row) if row else None

def getNutritions():
    db = get_db()
    rows = db.execute('SELECT * FROM Nutrition').fetchall()
    return [dict(row) for row in rows]

def getNutrition(nutrition_id):
    db = get_db()
    row = db.execute('SELECT * FROM Nutrition WHERE nutrition_id = ?', (nutrition_id,)).fetchone()
    return dict(row) if row else None

def getNutritionIngredients():
    db = get_db()
    rows = db.execute('SELECT * FROM NutritionIngredient').fetchall()
    return [dict(row) for row in rows]

def getNutritionIngredient(ni_id):
    db = get_db()
    row = db.execute('SELECT * FROM NutritionIngredient WHERE ni_id = ?', (ni_id,)).fetchone()
    return dict(row) if row else None

def getNutritionFields():
    db = get_db()
    rows = db.execute('SELECT * FROM NutritionFields').fetchall()
    return [dict(row) for row in rows]

def getNutritionField(nutritionfield_id):
    db = get_db()
    row = db.execute(
        'SELECT * FROM NutritionFields WHERE nutritionfield_id = ?', 
        (nutritionfield_id,)
    ).fetchone()
    return dict(row) if row else None