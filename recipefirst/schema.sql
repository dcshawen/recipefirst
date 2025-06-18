-- Disable foreign key checks during schema creation
PRAGMA foreign_keys = OFF;

-- Drop tables in reverse dependency order
DROP TABLE IF EXISTS NutritionFields;
DROP TABLE IF EXISTS NutritionIngredient;
DROP TABLE IF EXISTS Nutrition;
DROP TABLE IF EXISTS PantryComponent;
DROP TABLE IF EXISTS Pantry;
-- DROP TABLE IF EXISTS MealRecipe;
DROP TABLE IF EXISTS MealComponent;
DROP TABLE IF EXISTS ComponentIngredient;
DROP TABLE IF EXISTS RecipeComponent;
DROP TABLE IF EXISTS Meal;
DROP TABLE IF EXISTS Recipe;
DROP TABLE IF EXISTS Component;
DROP TABLE IF EXISTS Ingredient;
DROP TABLE IF EXISTS Units;

CREATE TABLE Units (
    unit_id INTEGER PRIMARY KEY NOT NULL,
    unit_name TEXT NOT NULL
);

/* Insert default units */
INSERT INTO Units (unit_id, unit_name) VALUES
(0, 'piece'), 
(1, 'g'),
(2, 'ml'),
(3, 'oz'),
(4, 'lb'),
(5, 'cup'),
(6, 'tbsp'),
(7, 'tsp'),
(8, 'gal');

CREATE TABLE Ingredient (
    ingredient_id INTEGER PRIMARY KEY NOT NULL,
    ingredient_name TEXT NOT NULL,
    ingredient_description TEXT,
    ingredient_notes TEXT,
    ingredient_image TEXT,
    ingredient_price REAL,
    unit_id INTEGER,
    FOREIGN KEY (unit_id) REFERENCES Units(unit_id)
);

CREATE TABLE Component (
    component_id INTEGER PRIMARY KEY NOT NULL,
    component_name TEXT NOT NULL,
    component_description TEXT,
    component_notes TEXT,
    component_image TEXT,
    component_price REAL,
    unit_id INTEGER,
    FOREIGN KEY (unit_id) REFERENCES Units(unit_id)
);

CREATE TABLE Recipe (
    recipe_id INTEGER PRIMARY KEY NOT NULL,
    recipe_name TEXT NOT NULL,
    recipe_description TEXT,
    recipe_notes TEXT,
		recipe_instructions TEXT,
    recipe_image TEXT
);

CREATE TABLE Meal (
    meal_id INTEGER PRIMARY KEY NOT NULL,
    meal_name TEXT NOT NULL,
    meal_description TEXT,
    meal_notes TEXT,
    meal_image TEXT
);

CREATE TABLE RecipeComponent (
    recipe_id INTEGER NOT NULL,
    component_id INTEGER NOT NULL,
    rc_quantity REAL,
    unit_id INTEGER,
    PRIMARY KEY (recipe_id, component_id),
    FOREIGN KEY (recipe_id) REFERENCES Recipe(recipe_id) ON DELETE CASCADE,
    FOREIGN KEY (component_id) REFERENCES Component(component_id) ON DELETE CASCADE,
    FOREIGN KEY (unit_id) REFERENCES Units(unit_id)
);

CREATE TABLE ComponentIngredient (
    component_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    ci_quantity REAL,
    unit_id INTEGER,
    PRIMARY KEY (component_id, ingredient_id),
    FOREIGN KEY (component_id) REFERENCES Component(component_id) ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES Ingredient(ingredient_id) ON DELETE CASCADE,
    FOREIGN KEY (unit_id) REFERENCES Units(unit_id)
);

/* CREATE TABLE MealRecipe (
    meal_id INTEGER NOT NULL,
    recipe_id INTEGER NOT NULL,
    PRIMARY KEY (meal_id, recipe_id),
    FOREIGN KEY (meal_id) REFERENCES Meal(meal_id) ON DELETE CASCADE,
    FOREIGN KEY (recipe_id) REFERENCES Recipe(recipe_id) ON DELETE CASCADE
);
 */
CREATE TABLE MealComponent (
		meal_id INTEGER NOT NULL,
		component_id INTEGER NOT NULL,
		mc_quantity REAL,
		unit_id INTEGER,
		PRIMARY KEY (meal_id, component_id),
		FOREIGN KEY (meal_id) REFERENCES Meal(meal_id) ON DELETE CASCADE,
		FOREIGN KEY (component_id) REFERENCES Component(component_id) ON DELETE CASCADE,
		FOREIGN KEY (unit_id) REFERENCES Units(unit_id)
);

CREATE TABLE Pantry (
    pantry_id INTEGER PRIMARY KEY NOT NULL,
    pantry_name TEXT NOT NULL,
    pantry_description TEXT,
    pantry_notes TEXT
);

CREATE TABLE PantryComponent (
    pantry_id INTEGER,
    component_id INTEGER,
    pc_quantity REAL,
    unit_id INTEGER,
    PRIMARY KEY (pantry_id, component_id),
    FOREIGN KEY (pantry_id) REFERENCES Pantry(pantry_id) ON DELETE CASCADE,
    FOREIGN KEY (component_id) REFERENCES Component(component_id) ON DELETE CASCADE,
    FOREIGN KEY (unit_id) REFERENCES Units(unit_id)
);

CREATE TABLE Nutrition (
    nutrition_id INTEGER PRIMARY KEY NOT NULL,
    nutrition_calories INTEGER
);

CREATE TABLE NutritionIngredient (
    ni_id INTEGER PRIMARY KEY NOT NULL,
    ingredient_id INTEGER,
    nutrition_id INTEGER,
    FOREIGN KEY (ingredient_id) REFERENCES Ingredient(ingredient_id) ON DELETE CASCADE,
    FOREIGN KEY (nutrition_id) REFERENCES Nutrition(nutrition_id) ON DELETE CASCADE
);

CREATE TABLE NutritionFields (
    nutritionfield_id INTEGER PRIMARY KEY NOT NULL,
    nutritionfield_name TEXT NOT NULL,
    nutritionfield_value TEXT,
    unit_id INTEGER,
    FOREIGN KEY (unit_id) REFERENCES Units(unit_id)
);

-- Re-enable foreign key checks at the end
PRAGMA foreign_keys = ON;

-- Trigger to automatically create a Component when a Recipe is created
CREATE TRIGGER create_component_for_recipe
    AFTER INSERT ON Recipe
    FOR EACH ROW
BEGIN
    INSERT INTO Component (
        component_name,
        component_description,
        component_notes,
        component_image,
        component_price,
        unit_id
    ) VALUES (
        NEW.recipe_name,
        NEW.recipe_description,
        NEW.recipe_notes,
        NEW.recipe_image,
        NULL,  -- Component price starts as NULL
        0      -- Default to 'piece' unit
    );
END;