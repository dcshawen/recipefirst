# Database Schema Documentation: RecipeFirst

This document provides a detailed explanation of the database schema defined in `schema.sql` for the RecipeFirst application. The schema is designed to manage recipes, ingredients, food items, meals, categories, and their relationships.

---

## Table Overview

### Ingredient
Stores basic ingredients.
- `ingredient_id`: Primary key
- `ingredient_name`: Name of the ingredient
- `created_at`, `updated_at`: Timestamps

### FoodItem
Represents prepared food items (can be produced by recipes).
- `fooditem_id`: Primary key
- `fooditem_name`: Name
- `fooditem_description`: Description
- `created_at`, `updated_at`: Timestamps

### Recipe
Represents a recipe that produces a single FoodItem.
- `recipe_id`: Primary key
- `recipe_name`: Name
- `recipe_description`: Description
- `recipe_fooditem_id`: Foreign key to FoodItem (unique, one-to-one)
- `created_at`, `updated_at`: Timestamps

### Meal
Represents a meal (collection of food items).
- `meal_id`: Primary key
- `meal_name`: Name
- `meal_description`: Description
- `created_at`, `updated_at`: Timestamps

### UnitType
Defines units for ingredient quantities (e.g., grams, cups).
- `id`: Primary key
- `unit_type`: Name (unique)
- `created_at`, `updated_at`: Timestamps

### RecipeIngredient
Links a recipe to either a raw ingredient or a food item, with quantity and unit.
- `ri_id`: Primary key
- `ri_recipe_id`: Foreign key to Recipe
- `ri_ingredient_id`: Foreign key to Ingredient (nullable)
- `ri_fooditem_id`: Foreign key to FoodItem (nullable)
- `ri_unit_type_id`: Foreign key to UnitType
- `ri_quantity`: Quantity
- `created_at`, `updated_at`: Timestamps
- **Constraint**: Exactly one of `ri_ingredient_id` or `ri_fooditem_id` must be set

### MealFoodItem
Links a meal to one or more food items.
- `mf_id`: Primary key
- `mf_meal_id`: Foreign key to Meal
- `mf_fooditem_id`: Foreign key to FoodItem
- `created_at`, `updated_at`: Timestamps
- **Unique**: Combination of `mf_meal_id` and `mf_fooditem_id`

### Category
Hierarchical category table for recipes, ingredients, and meals.
- `category_id`: Primary key
- `category_name`: Name
- `category_description`: Description
- `parent_category_id`: Foreign key to Category (self-referencing)
- `created_at`, `updated_at`: Timestamps
- **Index**: On `parent_category_id`

### RecipeInstruction
Step-by-step instructions for recipes.
- `instruction_id`: Primary key
- `recipe_id`: Foreign key to Recipe
- `step_number`: Step order (unique per recipe)
- `instruction_text`: Instruction
- `created_at`, `updated_at`: Timestamps
- **Index**: On `recipe_id`

### Junction Tables (Many-to-Many Relationships)

#### RecipeCategory
Links recipes to categories.
- `recipe_id`, `category_id`: Composite primary key
- `created_at`: Timestamp
- **Index**: On `category_id`

#### IngredientCategory
Links ingredients to categories.
- `ingredient_id`, `category_id`: Composite primary key
- `created_at`: Timestamp
- **Index**: On `category_id`

#### MealCategory
Links meals to categories.
- `meal_id`, `category_id`: Composite primary key
- `created_at`: Timestamp
- **Index**: On `category_id`

---

## Relationships
- **Recipe → FoodItem**: Each recipe produces one food item (one-to-one)
- **RecipeIngredient**: Each entry links a recipe to either an ingredient or a food item, with a unit and quantity
- **MealFoodItem**: Each meal can have multiple food items
- **Category**: Hierarchical, can be used for recipes, ingredients, and meals
- **Junction Tables**: Enable many-to-many relationships between recipes, ingredients, meals, and categories

---

## Triggers
Automatic update of `updated_at` timestamp on modification for:
- Ingredient
- FoodItem
- Recipe
- Meal
- UnitType
- RecipeIngredient
- MealFoodItem
- Category
- RecipeInstruction

Junction tables (`RecipeCategory`, `IngredientCategory`, `MealCategory`) only have `created_at` and do not require triggers.

---

## Indexes
- `Category`: Index on `parent_category_id`
- `RecipeInstruction`: Index on `recipe_id`
- Junction tables: Index on `category_id`

---

## Data Integrity & Constraints
- **Foreign Keys**: Enforced for all relationships
- **Unique Constraints**: Enforced where needed (e.g., one recipe per food item, unique meal-food item pairs)
- **Check Constraints**: Ensure only one source per recipe ingredient (ingredient or food item)

---

## Example Usage
- Add a new recipe: Insert into `Recipe`, link to a `FoodItem`, add ingredients via `RecipeIngredient`, add instructions via `RecipeInstruction`, and assign categories via `RecipeCategory`
- Add a meal: Insert into `Meal`, link food items via `MealFoodItem`, assign categories via `MealCategory`
- Categorize ingredients: Use `IngredientCategory`

---

## Schema Evolution
- Use `patch.sql` for schema updates and migrations

---

## ER Diagram (Textual)
```
Recipe --(1:1)--> FoodItem
Recipe --(1:N)--> RecipeIngredient --(N:1)--> Ingredient
Recipe --(1:N)--> RecipeIngredient --(N:1)--> FoodItem
Recipe --(1:N)--> RecipeInstruction
Meal --(1:N)--> MealFoodItem --(N:1)--> FoodItem
Category --(1:N)--> Category (hierarchy)
Recipe --(N:M)--> RecipeCategory --(M:N)--> Category
Ingredient --(N:M)--> IngredientCategory --(M:N)--> Category
Meal --(N:M)--> MealCategory --(M:N)--> Category
```

---

## Notes
- All timestamps are in UTC
- Foreign key constraints are enforced
- Schema is designed for extensibility and normalization
