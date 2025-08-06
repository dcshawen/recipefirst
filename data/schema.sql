PRAGMA foreign_keys = ON;

-- Schema for RecipeFirst application
-- This schema defines the structure for storing recipes, ingredients, food items, meals, and their relationships.
DROP TABLE IF EXISTS RecipeIngredient;
DROP TABLE IF EXISTS MealFoodItem;
DROP TABLE IF EXISTS Meal;
DROP TABLE IF EXISTS Recipe;
DROP TABLE IF EXISTS FoodItem;
DROP TABLE IF EXISTS Ingredient;
DROP TABLE IF EXISTS UnitType;
DROP TABLE IF EXISTS RecipeCategory;
DROP TABLE IF EXISTS IngredientCategory;
DROP TABLE IF EXISTS MealCategory;
DROP TABLE IF EXISTS RecipeInstruction;
DROP TABLE IF EXISTS Category;

-- Table: Ingredient
CREATE TABLE Ingredient (
  ingredient_id   INTEGER PRIMARY KEY,
  ingredient_name TEXT    NOT NULL UNIQUE,
  created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: FoodItem
CREATE TABLE FoodItem (
  fooditem_id          INTEGER PRIMARY KEY,
  fooditem_name        TEXT    NOT NULL,
  fooditem_description TEXT,
  created_at           TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at           TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: Recipe
-- Each recipe produces exactly one FoodItem
CREATE TABLE Recipe (
  recipe_id           INTEGER PRIMARY KEY,
  recipe_name         TEXT    NOT NULL,
  recipe_description  TEXT,
  recipe_fooditem_id  INTEGER NOT NULL UNIQUE,
  created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(recipe_fooditem_id)
    REFERENCES FoodItem(fooditem_id)
      ON DELETE CASCADE
);

-- Table: Meal
CREATE TABLE Meal (
  meal_id          INTEGER PRIMARY KEY,
  meal_name        TEXT    NOT NULL,
  meal_description TEXT,
  created_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: UnitType
CREATE TABLE UnitType (
  id               INTEGER PRIMARY KEY,
  unit_type        TEXT    NOT NULL UNIQUE,
  created_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: RecipeIngredient
-- Links a Recipe to either a raw Ingredient or an existing FoodItem
CREATE TABLE RecipeIngredient (
  ri_id             INTEGER PRIMARY KEY,
  ri_recipe_id      INTEGER NOT NULL,
  ri_ingredient_id  INTEGER,
  ri_fooditem_id    INTEGER,
  ri_unit_type_id   INTEGER NOT NULL,
  ri_quantity       REAL    NOT NULL,
  created_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  -- ensure exactly one of ri_ingredient_id or ri_fooditem_id is set
  CONSTRAINT ck_ri_source CHECK (
    (ri_ingredient_id IS NOT NULL AND ri_fooditem_id IS NULL)
    OR
    (ri_ingredient_id IS NULL     AND ri_fooditem_id IS NOT NULL)
  ),

  FOREIGN KEY(ri_recipe_id)
    REFERENCES Recipe(recipe_id)
      ON DELETE CASCADE,
  FOREIGN KEY(ri_ingredient_id)
    REFERENCES Ingredient(ingredient_id)
      ON DELETE CASCADE,
  FOREIGN KEY(ri_fooditem_id)
    REFERENCES FoodItem(fooditem_id)
      ON DELETE CASCADE,
  FOREIGN KEY(ri_unit_type_id)
    REFERENCES UnitType(id)
      ON DELETE RESTRICT
);

-- Table: MealFoodItem
-- Links a Meal to one or more FoodItems
CREATE TABLE MealFoodItem (
  mf_id           INTEGER PRIMARY KEY,
  mf_meal_id      INTEGER NOT NULL,
  mf_fooditem_id  INTEGER NOT NULL,
  created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  FOREIGN KEY(mf_meal_id)
    REFERENCES Meal(meal_id)
      ON DELETE CASCADE,
  FOREIGN KEY(mf_fooditem_id)
    REFERENCES FoodItem(fooditem_id)
      ON DELETE CASCADE,

  UNIQUE(mf_meal_id, mf_fooditem_id)
);

-- Table: Category
-- Base category table that can be used for recipes, ingredients, and meals
CREATE TABLE Category (
  category_id          INTEGER PRIMARY KEY,
  category_name        TEXT NOT NULL UNIQUE,
  category_description TEXT,
  parent_category_id   INTEGER,
  created_at           TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at           TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  FOREIGN KEY(parent_category_id)
    REFERENCES Category(category_id)
      ON DELETE SET NULL
);
CREATE INDEX idx_category_parent ON Category(parent_category_id);

-- Table: RecipeInstruction
-- Stores step-by-step instructions for recipes
CREATE TABLE RecipeInstruction (
  instruction_id       INTEGER PRIMARY KEY,
  recipe_id            INTEGER NOT NULL,
  step_number          INTEGER NOT NULL,
  instruction_text     TEXT NOT NULL,
  created_at           TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at           TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  FOREIGN KEY(recipe_id)
    REFERENCES Recipe(recipe_id)
      ON DELETE CASCADE,
      
  UNIQUE(recipe_id, step_number)
);
CREATE INDEX idx_recipe_instruction_recipe_id ON RecipeInstruction(recipe_id);

-- Junction tables for many-to-many relationships with categories

-- Table: RecipeCategory
CREATE TABLE RecipeCategory (
  recipe_id            INTEGER NOT NULL,
  category_id          INTEGER NOT NULL,
  created_at           TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  PRIMARY KEY(recipe_id, category_id),
  
  FOREIGN KEY(recipe_id)
    REFERENCES Recipe(recipe_id)
      ON DELETE CASCADE,
  FOREIGN KEY(category_id)
    REFERENCES Category(category_id)
      ON DELETE CASCADE
);
CREATE INDEX idx_recipe_category_category_id ON RecipeCategory(category_id);

-- Table: IngredientCategory
CREATE TABLE IngredientCategory (
  ingredient_id        INTEGER NOT NULL,
  category_id          INTEGER NOT NULL,
  created_at           TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  PRIMARY KEY(ingredient_id, category_id),
  
  FOREIGN KEY(ingredient_id)
    REFERENCES Ingredient(ingredient_id)
      ON DELETE CASCADE,
  FOREIGN KEY(category_id)
    REFERENCES Category(category_id)
      ON DELETE CASCADE
);
CREATE INDEX idx_ingredient_category_category_id ON IngredientCategory(category_id);

-- Table: MealCategory
CREATE TABLE MealCategory (
  meal_id              INTEGER NOT NULL,
  category_id          INTEGER NOT NULL,
  created_at           TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  PRIMARY KEY(meal_id, category_id),
  
  FOREIGN KEY(meal_id)
    REFERENCES Meal(meal_id)
      ON DELETE CASCADE,
  FOREIGN KEY(category_id)
    REFERENCES Category(category_id)
      ON DELETE CASCADE
);
CREATE INDEX idx_meal_category_category_id ON MealCategory(category_id);

-- Triggers for automatically updating updated_at columns

-- Ingredient table trigger
CREATE TRIGGER update_ingredient_timestamp 
AFTER UPDATE ON Ingredient
BEGIN
  UPDATE Ingredient SET updated_at = CURRENT_TIMESTAMP WHERE ingredient_id = NEW.ingredient_id;
END;

-- FoodItem table trigger
CREATE TRIGGER update_fooditem_timestamp 
AFTER UPDATE ON FoodItem
BEGIN
  UPDATE FoodItem SET updated_at = CURRENT_TIMESTAMP WHERE fooditem_id = NEW.fooditem_id;
END;

-- Recipe table trigger
CREATE TRIGGER update_recipe_timestamp 
AFTER UPDATE ON Recipe
BEGIN
  UPDATE Recipe SET updated_at = CURRENT_TIMESTAMP WHERE recipe_id = NEW.recipe_id;
END;

-- Meal table trigger
CREATE TRIGGER update_meal_timestamp 
AFTER UPDATE ON Meal
BEGIN
  UPDATE Meal SET updated_at = CURRENT_TIMESTAMP WHERE meal_id = NEW.meal_id;
END;

-- UnitType table trigger
CREATE TRIGGER update_unittype_timestamp 
AFTER UPDATE ON UnitType
BEGIN
  UPDATE UnitType SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;

-- RecipeIngredient table trigger
CREATE TRIGGER update_recipeingredient_timestamp 
AFTER UPDATE ON RecipeIngredient
BEGIN
  UPDATE RecipeIngredient SET updated_at = CURRENT_TIMESTAMP WHERE ri_id = NEW.ri_id;
END;

-- MealFoodItem table trigger
CREATE TRIGGER update_mealfooditem_timestamp 
AFTER UPDATE ON MealFoodItem
BEGIN
  UPDATE MealFoodItem SET updated_at = CURRENT_TIMESTAMP WHERE mf_id = NEW.mf_id;
END;

-- Category table trigger
CREATE TRIGGER update_category_timestamp 
AFTER UPDATE ON Category
BEGIN
  UPDATE Category SET updated_at = CURRENT_TIMESTAMP WHERE category_id = NEW.category_id;
END;

-- RecipeInstruction table trigger
CREATE TRIGGER update_recipeinstruction_timestamp 
AFTER UPDATE ON RecipeInstruction
BEGIN
  UPDATE RecipeInstruction SET updated_at = CURRENT_TIMESTAMP WHERE instruction_id = NEW.instruction_id;
END;

-- No triggers needed for junction tables with only created_at timestamps:
-- RecipeCategory, IngredientCategory, MealCategory