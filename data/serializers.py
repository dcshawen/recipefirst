"""
Serialization helpers to convert SQLAlchemy ORM objects to API response format.

These helpers ensure the new SQLAlchemy implementation returns the exact same
JSON structure as the original raw SQL implementation for backward compatibility.
"""

from typing import Dict, Any, List
from datetime import datetime

from .models import (
    Recipe, Ingredient, FoodItem, Meal, Category, UnitType,
    RecipeIngredient, RecipeInstruction, MealFoodItem
)


def serialize_datetime(dt: datetime) -> str:
    """Serialize datetime to ISO format string."""
    return dt.isoformat() if dt else None


def serialize_recipe_ingredient(ri: RecipeIngredient) -> Dict[str, Any]:
    """
    Serialize RecipeIngredient with flattened joined data.

    Matches the format from the original SQL:
    SELECT ri.*, i.ingredient_name, f.fooditem_name, ut.unit_type ...
    """
    return {
        "ri_id": ri.ri_id,
        "ri_recipe_id": ri.ri_recipe_id,
        "ri_ingredient_id": ri.ri_ingredient_id,
        "ri_fooditem_id": ri.ri_fooditem_id,
        "ri_unit_type_id": ri.ri_unit_type_id,
        "ri_quantity": ri.ri_quantity,
        "created_at": serialize_datetime(ri.created_at),
        "updated_at": serialize_datetime(ri.updated_at),
        # Joined fields
        "ingredient_name": ri.ingredient.ingredient_name if ri.ingredient else None,
        "ingredient_description": ri.ingredient.ingredient_description if ri.ingredient else None,
        "ingredient_notes": ri.ingredient.ingredient_notes if ri.ingredient else None,
        "fooditem_name": ri.fooditem.fooditem_name if ri.fooditem else None,
        "fooditem_description": ri.fooditem.fooditem_description if ri.fooditem else None,
        "unit_type": ri.unit_type.unit_type if ri.unit_type else None,
    }


def serialize_recipe_instruction(inst: RecipeInstruction) -> Dict[str, Any]:
    """
    Serialize RecipeInstruction.

    Original format only includes step_number and instruction_text.
    """
    return {
        "step_number": inst.step_number,
        "instruction_text": inst.instruction_text,
    }


def serialize_category(cat: Category) -> Dict[str, Any]:
    """Serialize Category."""
    return {
        "category_id": cat.category_id,
        "category_name": cat.category_name,
        "category_description": cat.category_description,
        "parent_category_id": cat.parent_category_id,
        "created_at": serialize_datetime(cat.created_at),
        "updated_at": serialize_datetime(cat.updated_at),
    }


def serialize_recipe(recipe: Recipe) -> Dict[str, Any]:
    """
    Serialize Recipe with all nested data.

    Matches the format from get_all_recipes() / get_recipe_by_id().
    """
    return {
        "recipe_id": recipe.recipe_id,
        "recipe_name": recipe.recipe_name,
        "recipe_description": recipe.recipe_description,
        "recipe_fooditem_id": recipe.recipe_fooditem_id,
        "created_at": serialize_datetime(recipe.created_at),
        "updated_at": serialize_datetime(recipe.updated_at),
        "ingredients": [serialize_recipe_ingredient(ri) for ri in recipe.ingredients],
        "instructions": [serialize_recipe_instruction(inst) for inst in recipe.instructions],
        "categories": [serialize_category(cat) for cat in recipe.categories],
    }


def serialize_ingredient(ingredient: Ingredient) -> Dict[str, Any]:
    """Serialize Ingredient."""
    return {
        "ingredient_id": ingredient.ingredient_id,
        "ingredient_name": ingredient.ingredient_name,
        "ingredient_description": ingredient.ingredient_description,
        "ingredient_notes": ingredient.ingredient_notes,
        "created_at": serialize_datetime(ingredient.created_at),
        "updated_at": serialize_datetime(ingredient.updated_at),
    }


def serialize_food_item(food_item: FoodItem) -> Dict[str, Any]:
    """
    Serialize FoodItem with associated recipes.

    Includes all recipes that produce this food item.
    """
    return {
        "fooditem_id": food_item.fooditem_id,
        "fooditem_name": food_item.fooditem_name,
        "fooditem_description": food_item.fooditem_description,
        "created_at": serialize_datetime(food_item.created_at),
        "updated_at": serialize_datetime(food_item.updated_at),
        # Include recipes that produce this food item (basic info only)
        "recipes": [
            {
                "recipe_id": recipe.recipe_id,
                "recipe_name": recipe.recipe_name,
                "recipe_description": recipe.recipe_description,
                "recipe_fooditem_id": recipe.recipe_fooditem_id,
                "created_at": serialize_datetime(recipe.created_at),
                "updated_at": serialize_datetime(recipe.updated_at),
            }
            for recipe in food_item.recipes
        ] if food_item.recipes else []
    }


def serialize_meal_food_item(mfi: MealFoodItem) -> Dict[str, Any]:
    """Serialize MealFoodItem with joined FoodItem data."""
    return {
        "fooditem_id": mfi.food_item.fooditem_id,
        "fooditem_name": mfi.food_item.fooditem_name,
        "fooditem_description": mfi.food_item.fooditem_description,
    }


def serialize_meal(meal: Meal) -> Dict[str, Any]:
    """Serialize Meal with nested food items and categories."""
    return {
        "meal_id": meal.meal_id,
        "meal_name": meal.meal_name,
        "meal_description": meal.meal_description,
        "created_at": serialize_datetime(meal.created_at),
        "updated_at": serialize_datetime(meal.updated_at),
        "food_items": [serialize_meal_food_item(mfi) for mfi in meal.meal_food_items],
        "categories": [serialize_category(cat) for cat in meal.categories],
    }


def serialize_unit_type(unit_type: UnitType) -> Dict[str, Any]:
    """Serialize UnitType."""
    return {
        "id": unit_type.id,
        "unit_type": unit_type.unit_type,
        "created_at": serialize_datetime(unit_type.created_at),
        "updated_at": serialize_datetime(unit_type.updated_at),
    }


# Collection serializers

def serialize_recipes(recipes: List[Recipe]) -> List[Dict[str, Any]]:
    """Serialize a list of recipes."""
    return [serialize_recipe(r) for r in recipes]


def serialize_ingredients(ingredients: List[Ingredient]) -> List[Dict[str, Any]]:
    """Serialize a list of ingredients."""
    return [serialize_ingredient(i) for i in ingredients]


def serialize_food_items(food_items: List[FoodItem]) -> List[Dict[str, Any]]:
    """Serialize a list of food items."""
    return [serialize_food_item(fi) for fi in food_items]


def serialize_meals(meals: List[Meal]) -> List[Dict[str, Any]]:
    """Serialize a list of meals."""
    return [serialize_meal(m) for m in meals]


def serialize_categories(categories: List[Category]) -> List[Dict[str, Any]]:
    """Serialize a list of categories."""
    return [serialize_category(c) for c in categories]


def serialize_unit_types(unit_types: List[UnitType]) -> List[Dict[str, Any]]:
    """Serialize a list of unit types."""
    return [serialize_unit_type(ut) for ut in unit_types]
