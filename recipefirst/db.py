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
def getIngredients(limit=None, name=None, description=None):
    """Fetch ingredients with optional filters."""
    db = get_db()
    query = 'SELECT * FROM Ingredient'
    filters = []
    params = []
    if name:
        filters.append('ingredient_name LIKE ?')
        params.append(f'%{name}%')
    if description:
        filters.append('ingredient_description LIKE ?')
        params.append(f'%{description}%')
    if filters:
        query += ' WHERE ' + ' AND '.join(filters)
    query += ' ORDER BY ingredient_id'
    if limit:
        query += ' LIMIT ?'
        params.append(limit)
    ingredients = db.execute(query, params).fetchall()
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

def getComponents(limit=None, name=None, description=None):
    """Fetch components with optional filters."""
    db = get_db()
    query = 'SELECT * FROM Component'
    filters = []
    params = []
    if name:
        filters.append('component_name LIKE ?')
        params.append(f'%{name}%')
    if description:
        filters.append('component_description LIKE ?')
        params.append(f'%{description}%')
    if filters:
        query += ' WHERE ' + ' AND '.join(filters)
    query += ' ORDER BY component_id'
    if limit:
        query += ' LIMIT ?'
        params.append(limit)
    rows = db.execute(query, params).fetchall()
    return [dict(row) for row in rows]

def getComponent(component_id):
    db = get_db()
    row = db.execute('SELECT * FROM Component WHERE component_id = ?', (component_id,)).fetchone()
    return dict(row) if row else None

def getRecipes(limit=None, name=None, description=None):
    """Fetch recipes with optional filters, including ingredients and components."""
    db = get_db()
    query = 'SELECT * FROM Recipe'
    filters = []
    params = []
    if name:
        filters.append('recipe_name LIKE ?')
        params.append(f'%{name}%')
    if description:
        filters.append('recipe_description LIKE ?')
        params.append(f'%{description}%')
    if filters:
        query += ' WHERE ' + ' AND '.join(filters)
    query += ' ORDER BY recipe_id'
    if limit:
        query += ' LIMIT ?'
        params.append(limit)
    rows = db.execute(query, params).fetchall()
    recipes = []
    for row in rows:
        recipe = dict(row)
        # Fetch ingredients for this recipe
        ingredients = db.execute(
            '''
            SELECT ri.*, i.ingredient_name, i.ingredient_description, i.ingredient_notes, i.ingredient_image
            FROM RecipeIngredient ri
            JOIN Ingredient i ON ri.ingredient_id = i.ingredient_id
            WHERE ri.recipe_id = ?
            ''',
            (recipe['recipe_id'],)
        ).fetchall()
        recipe['ingredients'] = [dict(ing) for ing in ingredients]
        # Fetch components for this recipe
        components = db.execute(
            '''
            SELECT rc.*, c.component_name, c.component_description, c.component_notes, c.component_image, c.unit_id
            FROM RecipeComponent rc
            JOIN Component c ON rc.component_id = c.component_id
            WHERE rc.recipe_id = ?
            ''',
            (recipe['recipe_id'],)
        ).fetchall()
        recipe['components'] = [dict(comp) for comp in components]
        recipes.append(recipe)
    return recipes

def getRecipe(recipe_id):
    db = get_db()
    row = db.execute('SELECT * FROM Recipe WHERE recipe_id = ?', (recipe_id,)).fetchone()
    return dict(row) if row else None

def getMeals(limit=None, name=None, description=None):
    """Fetch meals with optional filters."""
    db = get_db()
    query = 'SELECT * FROM Meal'
    filters = []
    params = []
    if name:
        filters.append('meal_name LIKE ?')
        params.append(f'%{name}%')
    if description:
        filters.append('meal_description LIKE ?')
        params.append(f'%{description}%')
    if filters:
        query += ' WHERE ' + ' AND '.join(filters)
    query += ' ORDER BY meal_id'
    if limit:
        query += ' LIMIT ?'
        params.append(limit)
    rows = db.execute(query, params).fetchall()
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

def addIngredient(data):
    """Add a new ingredient. All fields except ingredient_id must be provided."""
    db = get_db()
    ingredient_name = data.get('ingredient_name')
    unit_id = data.get('unit_id')
    if unit_id is not None:
        unit_id = int(unit_id)
    ingredient_description = data.get('ingredient_description')
    ingredient_notes = data.get('ingredient_notes')
    ingredient_image = data.get('ingredient_image')
    cursor = db.execute(
        '''
        INSERT INTO Ingredient (
            ingredient_name, ingredient_description, ingredient_notes, ingredient_image, unit_id
        ) VALUES (?, ?, ?, ?, ?)
        ''',
        (ingredient_name, ingredient_description, ingredient_notes, ingredient_image, unit_id)
    )
    db.commit()
    return cursor.lastrowid

def addRecipe(data):
    """Add a new recipe. All fields except recipe_id must be provided."""
    db = get_db()
    recipe_name = data.get('recipe_name')
    recipe_description = data.get('recipe_description')
    recipe_notes = data.get('recipe_notes')
    recipe_instructions = data.get('recipe_instructions')
    recipe_servings = data.get('recipe_servings')
    recipe_image = data.get('recipe_image')
    cursor = db.execute(
        '''
        INSERT INTO Recipe (
            recipe_name, recipe_description, recipe_notes, recipe_instructions, recipe_servings, recipe_image
        ) VALUES (?, ?, ?, ?, ?, ?)
        ''',
        (recipe_name, recipe_description, recipe_notes, recipe_instructions, recipe_servings, recipe_image)
    )
    db.commit()
    return cursor.lastrowid

def addComponent(data):
    """Add a new component. All fields except component_id must be provided."""
    db = get_db()
    component_name = data.get('component_name')
    component_description = data.get('component_description')
    component_notes = data.get('component_notes')
    component_image = data.get('component_image')
    unit_id = data.get('unit_id')
    if unit_id is not None:
        unit_id = int(unit_id)
    cursor = db.execute(
        '''
        INSERT INTO Component (
            component_name, component_description, component_notes, component_image, unit_id
        ) VALUES (?, ?, ?, ?, ?)
        ''',
        (component_name, component_description, component_notes, component_image, unit_id)
    )
    db.commit()
    return cursor.lastrowid

def addMeal(data):
    """Add a new meal. All fields except meal_id must be provided."""
    db = get_db()
    meal_name = data.get('meal_name')
    meal_description = data.get('meal_description')
    meal_notes = data.get('meal_notes')
    meal_image = data.get('meal_image')
    cursor = db.execute(
        '''
        INSERT INTO Meal (
            meal_name, meal_description, meal_notes, meal_image
        ) VALUES (?, ?, ?, ?)
        ''',
        (meal_name, meal_description, meal_notes, meal_image)
    )
    db.commit()
    return cursor.lastrowid

def addUnit(data):
    """Add a new unit. All fields except unit_id must be provided."""
    db = get_db()
    unit_name = data.get('unit_name')
    cursor = db.execute(
        '''
        INSERT INTO Units (
            unit_name
        ) VALUES (?
        ''',
        (unit_name,)
    )
    db.commit()
    return cursor.lastrowid

def updateIngredient(ingredient_id, data):
    db = get_db()
    db.execute(
        '''
        UPDATE Ingredient
        SET ingredient_name = ?, ingredient_description = ?, ingredient_notes = ?, ingredient_image = ?, unit_id = ?
        WHERE ingredient_id = ?
        ''',
        (
            data.get('ingredient_name'),
            data.get('ingredient_description'),
            data.get('ingredient_notes'),
            data.get('ingredient_image'),
            int(data.get('unit_id')) if data.get('unit_id') is not None else None,
            ingredient_id
        )
    )
    db.commit()

def deleteIngredient(ingredient_id):
    db = get_db()
    db.execute('DELETE FROM Ingredient WHERE ingredient_id = ?', (ingredient_id,))
    db.commit()

def updateRecipe(recipe_id, data):
    db = get_db()
    db.execute(
        '''
        UPDATE Recipe
        SET recipe_name = ?, recipe_description = ?, recipe_notes = ?, recipe_instructions = ?, recipe_servings = ?, recipe_image = ?
        WHERE recipe_id = ?
        ''',
        (
            data.get('recipe_name'),
            data.get('recipe_description'),
            data.get('recipe_notes'),
            data.get('recipe_instructions'),
            data.get('recipe_servings'),
            data.get('recipe_image'),
            recipe_id
        )
    )
    db.commit()

def deleteRecipe(recipe_id):
    db = get_db()
    db.execute('DELETE FROM Recipe WHERE recipe_id = ?', (recipe_id,))
    db.commit()

def updateComponent(component_id, data):
    db = get_db()
    db.execute(
        '''
        UPDATE Component
        SET component_name = ?, component_description = ?, component_notes = ?, component_image = ?, unit_id = ?
        WHERE component_id = ?
        ''',
        (
            data.get('component_name'),
            data.get('component_description'),
            data.get('component_notes'),
            data.get('component_image'),
            int(data.get('unit_id')) if data.get('unit_id') is not None else None,
            component_id
        )
    )
    db.commit()

def deleteComponent(component_id):
    db = get_db()
    db.execute('DELETE FROM Component WHERE component_id = ?', (component_id,))
    db.commit()

def updateMeal(meal_id, data):
    db = get_db()
    db.execute(
        '''
        UPDATE Meal
        SET meal_name = ?, meal_description = ?, meal_notes = ?, meal_image = ?
        WHERE meal_id = ?
        ''',
        (
            data.get('meal_name'),
            data.get('meal_description'),
            data.get('meal_notes'),
            data.get('meal_image'),
            meal_id
        )
    )
    db.commit()

def deleteMeal(meal_id):
    db = get_db()
    db.execute('DELETE FROM Meal WHERE meal_id = ?', (meal_id,))
    db.commit()

def updateUnit(unit_id, data):
    db = get_db()
    db.execute(
        '''
        UPDATE Units
        SET unit_name = ?
        WHERE unit_id = ?
        ''',
        (
            data.get('unit_name'),
            unit_id
        )
    )
    db.commit()

def deleteUnit(unit_id):
    db = get_db()
    db.execute('DELETE FROM Units WHERE unit_id = ?', (unit_id,))
    db.commit()