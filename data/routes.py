"""
FastAPI routes for RecipeFirst application.

Updated to use SQLAlchemy ORM instead of raw SQL while maintaining
exact same API response format for backward compatibility.
"""

from fastapi import APIRouter, HTTPException, Body, Path, Query, Depends
from sqlalchemy.ext.asyncio import AsyncSession

# Import old db module for schema operations (keep for now)
import db

# Import new SQLAlchemy infrastructure
from database import get_db
import crud
import serializers

router = APIRouter()

MAX_RECIPES = 1000


@router.get("/")
async def root():
    """Get database schema information."""
    return {"message": db.getDBSchema()}


# ============================================================================
# Recipe Endpoints
# ============================================================================

@router.get("/recipes")
async def get_recipes(session: AsyncSession = Depends(get_db)):
    """Get all recipes with ingredients, instructions, and categories."""
    recipes = await crud.get_all_recipes(session)
    return {"recipes": serializers.serialize_recipes(recipes)}


@router.get("/recipes/{id}")
async def get_recipe(
    id: int = Path(..., description="The ID of the recipe to retrieve", gt=0),
    session: AsyncSession = Depends(get_db)
):
    """Get a single recipe by ID."""
    recipe = await crud.get_recipe_by_id(session, id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return serializers.serialize_recipe(recipe)


@router.post("/recipes")
async def create_recipe(
    recipe_data = Body(...),
    session: AsyncSession = Depends(get_db)
):
    """Create a new recipe."""
    recipe = await crud.create_recipe(session, recipe_data)
    return serializers.serialize_recipe(recipe)


@router.put("/recipes/{id}")
async def update_recipe(
    id: int = Path(..., gt=0),
    recipe_data = Body(...),
    session: AsyncSession = Depends(get_db)
):
    """Update an existing recipe."""
    updated = await crud.update_recipe(session, id, recipe_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return {"message": "Recipe updated successfully"}


@router.delete("/recipes/{id}")
async def delete_recipe(
    id: int = Path(..., gt=0),
    session: AsyncSession = Depends(get_db)
):
    """Delete a recipe."""
    deleted = await crud.delete_recipe(session, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return {"message": "Recipe deleted successfully"}


# ============================================================================
# Ingredient Endpoints
# ============================================================================

@router.get("/ingredients")
async def get_ingredients(session: AsyncSession = Depends(get_db)):
    """Get all ingredients."""
    ingredients = await crud.get_all_ingredients(session)
    return {"ingredients": serializers.serialize_ingredients(ingredients)}


@router.get("/ingredients/{id}")
async def get_ingredient(
    id: int = Path(..., gt=-1),
    session: AsyncSession = Depends(get_db)
):
    """Get a single ingredient by ID."""
    ingredient = await crud.get_ingredient_by_id(session, id)
    if ingredient is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return serializers.serialize_ingredient(ingredient)


@router.post("/ingredients")
async def create_ingredient(
    ingredient_data = Body(...),
    session: AsyncSession = Depends(get_db)
):
    """Create a new ingredient."""
    ingredient = await crud.create_ingredient(session, ingredient_data)
    return serializers.serialize_ingredient(ingredient)


@router.put("/ingredients/{id}")
async def update_ingredient(
    id: int = Path(..., gt=0),
    ingredient_data = Body(...),
    session: AsyncSession = Depends(get_db)
):
    """Update an existing ingredient."""
    updated = await crud.update_ingredient(session, id, ingredient_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return {"message": "Ingredient updated successfully"}


@router.delete("/ingredients/{id}")
async def delete_ingredient(
    id: int = Path(..., gt=0),
    session: AsyncSession = Depends(get_db)
):
    """Delete an ingredient."""
    deleted = await crud.delete_ingredient(session, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return {"message": "Ingredient deleted successfully"}


# ============================================================================
# Recipe-Ingredient Junction Endpoints
# ============================================================================

@router.get("/recipes/{id}/ingredients")
async def get_recipe_ingredients(
    id: int = Path(..., gt=0),
    session: AsyncSession = Depends(get_db)
):
    """Get all ingredients for a specific recipe."""
    recipe = await crud.get_recipe_by_id(session, id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")

    ingredients = await crud.get_recipe_ingredients(session, id)
    return {"ingredients": [serializers.serialize_recipe_ingredient(ri) for ri in ingredients]}


@router.post("/recipes/{id}/ingredients")
async def add_recipe_ingredient(
    id: int = Path(..., gt=0),
    ingredient_data = Body(...),
    session: AsyncSession = Depends(get_db)
):
    """Add an ingredient to a recipe."""
    recipe = await crud.get_recipe_by_id(session, id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")

    recipe_ingredient = await crud.add_ingredient_to_recipe(session, id, ingredient_data)
    return serializers.serialize_recipe_ingredient(recipe_ingredient)


@router.put("/recipes/{id}/ingredients/{ingredient_id}")
async def update_recipe_ingredient(
    id: int = Path(..., gt=0),
    ingredient_id: int = Path(..., gt=0),
    update_data = Body(...),
    session: AsyncSession = Depends(get_db)
):
    """Update a recipe ingredient."""
    updated = await crud.update_recipe_ingredient(session, id, ingredient_id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Recipe or ingredient not found")
    return {"message": "Recipe ingredient updated successfully"}


@router.delete("/recipes/{id}/ingredients/{ingredient_id}")
async def remove_recipe_ingredient(
    id: int = Path(..., gt=0),
    ingredient_id: int = Path(..., gt=0),
    session: AsyncSession = Depends(get_db)
):
    """Remove an ingredient from a recipe."""
    deleted = await crud.remove_ingredient_from_recipe(session, id, ingredient_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Recipe or ingredient not found")
    return {"message": "Ingredient removed from recipe successfully"}


# ============================================================================
# Category Endpoints
# ============================================================================

@router.get("/categories")
async def get_categories(session: AsyncSession = Depends(get_db)):
    """Get all categories."""
    categories = await crud.get_all_categories(session)
    return {"categories": serializers.serialize_categories(categories)}


@router.get("/categories/{id}")
async def get_category(
    id: int = Path(..., gt=0),
    session: AsyncSession = Depends(get_db)
):
    """Get a single category by ID."""
    category = await crud.get_category_by_id(session, id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return serializers.serialize_category(category)


@router.post("/categories")
async def create_category(
    category_data = Body(...),
    session: AsyncSession = Depends(get_db)
):
    """Create a new category."""
    category = await crud.create_category(session, category_data)
    return serializers.serialize_category(category)


@router.put("/categories/{id}")
async def update_category(
    id: int = Path(..., gt=0),
    category_data = Body(...),
    session: AsyncSession = Depends(get_db)
):
    """Update an existing category."""
    updated = await crud.update_category(session, id, category_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category updated successfully"}


@router.delete("/categories/{id}")
async def delete_category(
    id: int = Path(..., gt=0),
    session: AsyncSession = Depends(get_db)
):
    """Delete a category."""
    deleted = await crud.delete_category(session, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted successfully"}


# ============================================================================
# Food Item Endpoints
# ============================================================================

@router.get("/food-items")
async def get_food_items(session: AsyncSession = Depends(get_db)):
    """Get all food items."""
    food_items = await crud.get_all_food_items(session)
    return {"food_items": serializers.serialize_food_items(food_items)}


@router.get("/food-items/{id}/recipes")
async def get_food_item_recipes(
    id: int = Path(..., gt=0),
    session: AsyncSession = Depends(get_db)
):
    """Get all recipes that use this food item as an ingredient."""
    food_item = await crud.get_food_item_by_id(session, id)
    if food_item is None:
        raise HTTPException(status_code=404, detail="Food item not found")

    recipes = await crud.get_recipes_by_food_item_id(session, id)
    return {"recipes": serializers.serialize_recipes(recipes)}


@router.get("/food-items/{id}")
async def get_food_item(
    id: int = Path(..., gt=0),
    session: AsyncSession = Depends(get_db)
):
    """Get a single food item by ID."""
    food_item = await crud.get_food_item_by_id(session, id)
    if food_item is None:
        raise HTTPException(status_code=404, detail="Food item not found")
    return serializers.serialize_food_item(food_item)


@router.post("/food-items")
async def create_food_item(
    food_item_data = Body(...),
    session: AsyncSession = Depends(get_db)
):
    """Create a new food item."""
    food_item = await crud.create_food_item(session, food_item_data)
    return serializers.serialize_food_item(food_item)


@router.put("/food-items/{id}")
async def update_food_item(
    id: int = Path(..., gt=0),
    food_item_data = Body(...),
    session: AsyncSession = Depends(get_db)
):
    """Update an existing food item."""
    updated = await crud.update_food_item(session, id, food_item_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Food item not found")
    return {"message": "Food item updated successfully"}


@router.delete("/food-items/{id}")
async def delete_food_item(
    id: int = Path(..., gt=0),
    session: AsyncSession = Depends(get_db)
):
    """Delete a food item."""
    deleted = await crud.delete_food_item(session, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Food item not found")
    return {"message": "Food item deleted successfully"}


# ============================================================================
# Meal Endpoints
# ============================================================================

@router.get("/meals")
async def get_meals(session: AsyncSession = Depends(get_db)):
    """Get all meals."""
    meals = await crud.get_all_meals(session)
    return {"meals": serializers.serialize_meals(meals)}


@router.get("/meals/{id}")
async def get_meal(
    id: int = Path(..., gt=0),
    session: AsyncSession = Depends(get_db)
):
    """Get a single meal by ID."""
    meal = await crud.get_meal_by_id(session, id)
    if meal is None:
        raise HTTPException(status_code=404, detail="Meal not found")
    return serializers.serialize_meal(meal)


@router.post("/meals")
async def create_meal(
    meal_data = Body(...),
    session: AsyncSession = Depends(get_db)
):
    """Create a new meal."""
    meal = await crud.create_meal(session, meal_data)
    return serializers.serialize_meal(meal)


@router.put("/meals/{id}")
async def update_meal(
    id: int = Path(..., gt=0),
    meal_data = Body(...),
    session: AsyncSession = Depends(get_db)
):
    """Update an existing meal."""
    updated = await crud.update_meal(session, id, meal_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Meal not found")
    return {"message": "Meal updated successfully"}


@router.delete("/meals/{id}")
async def delete_meal(
    id: int = Path(..., gt=0),
    session: AsyncSession = Depends(get_db)
):
    """Delete a meal."""
    deleted = await crud.delete_meal(session, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Meal not found")
    return {"message": "Meal deleted successfully"}


# ============================================================================
# Search & Utility Endpoints
# ============================================================================

@router.get("/recipes/search")
async def search_recipes(
    q: str = Query(..., description="Search query", min_length=1, max_length=100),
    session: AsyncSession = Depends(get_db)
):
    """Search recipes by name."""
    recipes = await crud.search_recipes(session, q)
    return {"results": serializers.serialize_recipes(recipes)}


@router.get("/search")
async def omni_search(
    q: str = Query(..., description="Search query", min_length=1, max_length=100),
    session: AsyncSession = Depends(get_db)
):
    """
    Unified search across all entity types.
    Returns results grouped by type with limit per type.
    """
    recipes = await crud.search_recipes(session, q)
    meals = await crud.search_meals(session, q)
    food_items = await crud.search_food_items(session, q)
    ingredients = await crud.search_ingredients(session, q)

    return {
        "query": q,
        "results": {
            "recipes": serializers.serialize_recipes(recipes[:5]),
            "meals": serializers.serialize_meals(meals[:5]),
            "food_items": serializers.serialize_food_items(food_items[:5]),
            "ingredients": serializers.serialize_ingredients(ingredients[:5])
        }
    }


@router.get("/recipes/category/{category_id}")
async def get_recipes_by_category(
    category_id: int = Path(..., gt=0),
    session: AsyncSession = Depends(get_db)
):
    """Get all recipes in a specific category."""
    recipes = await crud.get_recipes_by_category(session, category_id)
    return {"recipes": serializers.serialize_recipes(recipes)}


# ============================================================================
# Unit Type Endpoints
# ============================================================================

@router.get("/unit-types")
async def get_unit_types(session: AsyncSession = Depends(get_db)):
    """Get all unit types."""
    unit_types = await crud.get_all_unit_types(session)
    return {"unit_types": serializers.serialize_unit_types(unit_types)}


@router.get("/unit-types/{id}")
async def get_unit_type(
    id: int = Path(..., gt=0),
    session: AsyncSession = Depends(get_db)
):
    """Get a single unit type by ID."""
    unit_type = await crud.get_unit_type_by_id(session, id)
    if unit_type is None:
        raise HTTPException(status_code=404, detail="Unit type not found")
    return serializers.serialize_unit_type(unit_type)


@router.post("/unit-types")
async def create_unit_type(
    unit_type_data = Body(...),
    session: AsyncSession = Depends(get_db)
):
    """Create a new unit type."""
    unit_type = await crud.create_unit_type(session, unit_type_data)
    return serializers.serialize_unit_type(unit_type)


@router.put("/unit-types/{id}")
async def update_unit_type(
    id: int = Path(..., gt=0),
    unit_type_data = Body(...),
    session: AsyncSession = Depends(get_db)
):
    """Update an existing unit type."""
    updated = await crud.update_unit_type(session, id, unit_type_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Unit type not found")
    return {"message": "Unit type updated successfully"}


@router.delete("/unit-types/{id}")
async def delete_unit_type(
    id: int = Path(..., gt=0),
    session: AsyncSession = Depends(get_db)
):
    """Delete a unit type."""
    deleted = await crud.delete_unit_type(session, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Unit type not found")
    return {"message": "Unit type deleted successfully"}
