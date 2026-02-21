"""
CRUD operations for RecipeFirst application using SQLAlchemy ORM.

This module replaces the raw SQL functions from db.py with SQLAlchemy queries.
All functions use async/await and proper eager loading to prevent N+1 queries.

Organization:
- Recipe operations (5 functions)
- Ingredient operations (5 functions)
- RecipeIngredient junction operations (4 functions)
- Category operations (5 functions)
- FoodItem operations (5 functions)
- Meal operations (5 functions)
- UnitType operations (5 functions)
- Search operations (4 functions)
- Utility operations (2 functions)
"""

from sqlalchemy import select, delete as sql_delete, or_, func
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional, Dict, Any
import logging

from .models import (
    Recipe, Ingredient, FoodItem, Meal, Category, UnitType,
    RecipeIngredient, RecipeInstruction, MealFoodItem,
    RecipeCategory, IngredientCategory, MealCategory
)

logger = logging.getLogger(__name__)


# ============================================================================
# Recipe Operations
# ============================================================================

async def get_all_recipes(db: AsyncSession) -> List[Recipe]:
    """
    Get all recipes with nested ingredients, instructions, and categories.

    Uses selectinload to prevent N+1 queries. This replaces the old implementation
    that executed 1 + (3 * N) queries with just 2-5 queries total.
    """
    stmt = (
        select(Recipe)
        .options(
            # Load ingredients with their related data
            selectinload(Recipe.ingredients)
                .selectinload(RecipeIngredient.ingredient),
            selectinload(Recipe.ingredients)
                .selectinload(RecipeIngredient.fooditem),
            selectinload(Recipe.ingredients)
                .selectinload(RecipeIngredient.unit_type),
            # Load instructions
            selectinload(Recipe.instructions),
            # Load categories
            selectinload(Recipe.categories)
        )
    )
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_recipe_by_id(db: AsyncSession, recipe_id: int) -> Optional[Recipe]:
    """Get a single recipe by ID with all nested data."""
    stmt = (
        select(Recipe)
        .where(Recipe.recipe_id == recipe_id)
        .options(
            selectinload(Recipe.ingredients)
                .selectinload(RecipeIngredient.ingredient),
            selectinload(Recipe.ingredients)
                .selectinload(RecipeIngredient.fooditem),
            selectinload(Recipe.ingredients)
                .selectinload(RecipeIngredient.unit_type),
            selectinload(Recipe.instructions),
            selectinload(Recipe.categories)
        )
    )
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def create_recipe(db: AsyncSession, recipe_data: Dict[str, Any]) -> Recipe:
    """
    Create a new recipe with ingredients, instructions, and categories.

    Args:
        recipe_data: Dictionary containing:
            - recipe_name: str
            - recipe_description: str (optional)
            - recipe_fooditem_id: int
            - ingredients: List[Dict] (optional)
            - instructions: List[Dict] (optional)
            - category_ids: List[int] (optional)
    """
    # Extract nested data
    ingredients_data = recipe_data.pop('ingredients', [])
    instructions_data = recipe_data.pop('instructions', [])
    category_ids = recipe_data.pop('category_ids', [])

    # Create recipe
    recipe = Recipe(**recipe_data)
    db.add(recipe)
    await db.flush()  # Get recipe_id without committing

    # Add categories
    if category_ids:
        for category_id in category_ids:
            recipe_category = RecipeCategory(
                recipe_id=recipe.recipe_id,
                category_id=category_id
            )
            db.add(recipe_category)

    # Add ingredients
    for ing_data in ingredients_data:
        ingredient = RecipeIngredient(
            ri_recipe_id=recipe.recipe_id,
            **ing_data
        )
        db.add(ingredient)

    # Add instructions
    for inst_data in instructions_data:
        instruction = RecipeInstruction(
            recipe_id=recipe.recipe_id,
            **inst_data
        )
        db.add(instruction)

    await db.commit()
    await db.refresh(recipe)

    # Load nested data
    return await get_recipe_by_id(db, recipe.recipe_id)


async def update_recipe(db: AsyncSession, recipe_id: int, recipe_data: Dict[str, Any]) -> Optional[Recipe]:
    """
    Update a recipe.

    Uses the delete/recreate pattern for nested relationships (ingredients, instructions, categories)
    to match the behavior of the original implementation.
    """
    recipe = await get_recipe_by_id(db, recipe_id)
    if not recipe:
        return None

    # Extract nested data
    ingredients_data = recipe_data.pop('ingredients', None)
    instructions_data = recipe_data.pop('instructions', None)
    category_ids = recipe_data.pop('category_ids', None)

    # Update scalar fields
    for key, value in recipe_data.items():
        if hasattr(recipe, key):
            setattr(recipe, key, value)

    # Update categories (delete/recreate pattern)
    if category_ids is not None:
        # Delete existing
        await db.execute(
            sql_delete(RecipeCategory).where(RecipeCategory.recipe_id == recipe_id)
        )
        # Create new
        for category_id in category_ids:
            recipe_category = RecipeCategory(
                recipe_id=recipe_id,
                category_id=category_id
            )
            db.add(recipe_category)

    # Update ingredients (delete/recreate pattern)
    if ingredients_data is not None:
        # Delete existing
        await db.execute(
            sql_delete(RecipeIngredient).where(RecipeIngredient.ri_recipe_id == recipe_id)
        )
        # Create new
        for ing_data in ingredients_data:
            ingredient = RecipeIngredient(
                ri_recipe_id=recipe_id,
                **ing_data
            )
            db.add(ingredient)

    # Update instructions (delete/recreate pattern)
    if instructions_data is not None:
        # Delete existing
        await db.execute(
            sql_delete(RecipeInstruction).where(RecipeInstruction.recipe_id == recipe_id)
        )
        # Create new
        for inst_data in instructions_data:
            instruction = RecipeInstruction(
                recipe_id=recipe_id,
                **inst_data
            )
            db.add(instruction)

    await db.commit()
    await db.refresh(recipe)

    # Reload with nested data
    return await get_recipe_by_id(db, recipe_id)


async def delete_recipe(db: AsyncSession, recipe_id: int) -> bool:
    """
    Delete a recipe.

    CASCADE deletes will automatically remove related RecipeIngredient,
    RecipeInstruction, and RecipeCategory entries.
    """
    recipe = await db.get(Recipe, recipe_id)
    if not recipe:
        return False

    await db.delete(recipe)
    await db.commit()
    return True


# ============================================================================
# Ingredient Operations
# ============================================================================

async def get_all_ingredients(db: AsyncSession) -> List[Ingredient]:
    """Get all ingredients."""
    stmt = select(Ingredient)
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_ingredient_by_id(db: AsyncSession, ingredient_id: int) -> Optional[Ingredient]:
    """Get a single ingredient by ID."""
    return await db.get(Ingredient, ingredient_id)


async def create_ingredient(db: AsyncSession, ingredient_data: Dict[str, Any]) -> Ingredient:
    """Create a new ingredient."""
    ingredient = Ingredient(**ingredient_data)
    db.add(ingredient)
    await db.commit()
    await db.refresh(ingredient)
    return ingredient


async def update_ingredient(db: AsyncSession, ingredient_id: int, ingredient_data: Dict[str, Any]) -> Optional[Ingredient]:
    """Update an ingredient."""
    ingredient = await db.get(Ingredient, ingredient_id)
    if not ingredient:
        return None

    for key, value in ingredient_data.items():
        if hasattr(ingredient, key):
            setattr(ingredient, key, value)

    await db.commit()
    await db.refresh(ingredient)
    return ingredient


async def delete_ingredient(db: AsyncSession, ingredient_id: int) -> bool:
    """Delete an ingredient."""
    ingredient = await db.get(Ingredient, ingredient_id)
    if not ingredient:
        return False

    await db.delete(ingredient)
    await db.commit()
    return True


# ============================================================================
# RecipeIngredient Junction Operations
# ============================================================================

async def get_recipe_ingredients(db: AsyncSession, recipe_id: int) -> List[RecipeIngredient]:
    """Get all ingredients for a specific recipe."""
    stmt = (
        select(RecipeIngredient)
        .where(RecipeIngredient.ri_recipe_id == recipe_id)
        .options(
            selectinload(RecipeIngredient.ingredient),
            selectinload(RecipeIngredient.fooditem),
            selectinload(RecipeIngredient.unit_type)
        )
    )
    result = await db.execute(stmt)
    return result.scalars().all()


async def add_ingredient_to_recipe(db: AsyncSession, recipe_id: int, ingredient_data: Dict[str, Any]) -> RecipeIngredient:
    """Add an ingredient to a recipe."""
    recipe_ingredient = RecipeIngredient(
        ri_recipe_id=recipe_id,
        **ingredient_data
    )
    db.add(recipe_ingredient)
    await db.commit()
    await db.refresh(recipe_ingredient)

    # Load related data
    stmt = (
        select(RecipeIngredient)
        .where(RecipeIngredient.ri_id == recipe_ingredient.ri_id)
        .options(
            selectinload(RecipeIngredient.ingredient),
            selectinload(RecipeIngredient.fooditem),
            selectinload(RecipeIngredient.unit_type)
        )
    )
    result = await db.execute(stmt)
    return result.scalar_one()


async def update_recipe_ingredient(db: AsyncSession, recipe_id: int, ingredient_id: int, update_data: Dict[str, Any]) -> Optional[RecipeIngredient]:
    """Update a recipe ingredient."""
    stmt = (
        select(RecipeIngredient)
        .where(
            RecipeIngredient.ri_recipe_id == recipe_id,
            RecipeIngredient.ri_id == ingredient_id
        )
    )
    result = await db.execute(stmt)
    recipe_ingredient = result.scalar_one_or_none()

    if not recipe_ingredient:
        return None

    for key, value in update_data.items():
        if hasattr(recipe_ingredient, key):
            setattr(recipe_ingredient, key, value)

    await db.commit()
    await db.refresh(recipe_ingredient)
    return recipe_ingredient


async def remove_ingredient_from_recipe(db: AsyncSession, recipe_id: int, ingredient_id: int) -> bool:
    """Remove an ingredient from a recipe."""
    result = await db.execute(
        sql_delete(RecipeIngredient).where(
            RecipeIngredient.ri_recipe_id == recipe_id,
            RecipeIngredient.ri_id == ingredient_id
        )
    )
    await db.commit()
    return result.rowcount > 0


# ============================================================================
# Category Operations
# ============================================================================

async def get_all_categories(db: AsyncSession) -> List[Category]:
    """Get all categories."""
    stmt = select(Category)
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_category_by_id(db: AsyncSession, category_id: int) -> Optional[Category]:
    """Get a single category by ID."""
    return await db.get(Category, category_id)


async def create_category(db: AsyncSession, category_data: Dict[str, Any]) -> Category:
    """Create a new category."""
    # Only allow known fields to prevent TypeError from unexpected keys
    allowed_keys = {'category_name', 'category_description', 'parent_category_id'}
    cleaned = {k: v for k, v in category_data.items() if k in allowed_keys}

    # Coerce empty strings to None for nullable foreign keys
    if 'parent_category_id' in cleaned:
        if cleaned['parent_category_id'] in ('', None):
            cleaned['parent_category_id'] = None
        else:
            try:
                cleaned['parent_category_id'] = int(cleaned['parent_category_id'])
            except Exception:
                # If coercion fails, set to None to avoid DB errors
                cleaned['parent_category_id'] = None

    category = Category(**cleaned)
    db.add(category)
    try:
        await db.commit()
        await db.refresh(category)
    except Exception as e:
        await db.rollback()
        logger.error(f"Failed to create category: {e}")
        raise

    return category


async def update_category(db: AsyncSession, category_id: int, category_data: Dict[str, Any]) -> Optional[Category]:
    """Update a category."""
    category = await db.get(Category, category_id)
    if not category:
        return None

    for key, value in category_data.items():
        if hasattr(category, key):
            setattr(category, key, value)

    await db.commit()
    await db.refresh(category)
    return category


async def delete_category(db: AsyncSession, category_id: int) -> bool:
    """Delete a category."""
    category = await db.get(Category, category_id)
    if not category:
        return False

    await db.delete(category)
    await db.commit()
    return True


# ============================================================================
# FoodItem Operations
# ============================================================================

async def get_all_food_items(db: AsyncSession) -> List[FoodItem]:
    """Get all food items with their associated recipes."""
    stmt = (
        select(FoodItem)
        .options(selectinload(FoodItem.recipes))
    )
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_food_item_by_id(db: AsyncSession, fooditem_id: int) -> Optional[FoodItem]:
    """Get a single food item by ID with its recipes."""
    stmt = (
        select(FoodItem)
        .where(FoodItem.fooditem_id == fooditem_id)
        .options(selectinload(FoodItem.recipes))
    )
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def create_food_item(db: AsyncSession, food_item_data: Dict[str, Any]) -> FoodItem:
    """Create a new food item."""
    food_item = FoodItem(**food_item_data)
    db.add(food_item)
    await db.commit()
    await db.refresh(food_item)

    # Reload with relationships to prevent lazy loading issues
    return await get_food_item_by_id(db, food_item.fooditem_id)


async def update_food_item(db: AsyncSession, fooditem_id: int, food_item_data: Dict[str, Any]) -> Optional[FoodItem]:
    """Update a food item."""
    food_item = await db.get(FoodItem, fooditem_id)
    if not food_item:
        return None

    for key, value in food_item_data.items():
        if hasattr(food_item, key):
            setattr(food_item, key, value)

    await db.commit()
    await db.refresh(food_item)

    # Reload with relationships to prevent lazy loading issues
    return await get_food_item_by_id(db, fooditem_id)


async def delete_food_item(db: AsyncSession, fooditem_id: int) -> bool:
    """Delete a food item."""
    food_item = await db.get(FoodItem, fooditem_id)
    if not food_item:
        return False

    await db.delete(food_item)
    await db.commit()
    return True


# ============================================================================
# Meal Operations
# ============================================================================

async def get_all_meals(db: AsyncSession) -> List[Meal]:
    """Get all meals with nested food items and categories."""
    stmt = (
        select(Meal)
        .options(
            selectinload(Meal.meal_food_items).selectinload(MealFoodItem.food_item),
            selectinload(Meal.categories)
        )
    )
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_meal_by_id(db: AsyncSession, meal_id: int) -> Optional[Meal]:
    """Get a single meal by ID with nested data."""
    stmt = (
        select(Meal)
        .where(Meal.meal_id == meal_id)
        .options(
            selectinload(Meal.meal_food_items).selectinload(MealFoodItem.food_item),
            selectinload(Meal.categories)
        )
    )
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def create_meal(db: AsyncSession, meal_data: Dict[str, Any]) -> Meal:
    """Create a new meal with food items and categories."""
    # Extract nested data
    fooditem_ids = meal_data.pop('fooditem_ids', [])
    category_ids = meal_data.pop('category_ids', [])

    # Create meal
    meal = Meal(**meal_data)
    db.add(meal)
    await db.flush()  # Get meal_id

    # Add food items
    for fooditem_id in fooditem_ids:
        meal_food_item = MealFoodItem(
            mf_meal_id=meal.meal_id,
            mf_fooditem_id=fooditem_id
        )
        db.add(meal_food_item)

    # Add categories
    for category_id in category_ids:
        meal_category = MealCategory(
            meal_id=meal.meal_id,
            category_id=category_id
        )
        db.add(meal_category)

    await db.commit()
    await db.refresh(meal)

    # Reload with nested data
    return await get_meal_by_id(db, meal.meal_id)


async def update_meal(db: AsyncSession, meal_id: int, meal_data: Dict[str, Any]) -> Optional[Meal]:
    """Update a meal."""
    meal = await get_meal_by_id(db, meal_id)
    if not meal:
        return None

    # Extract nested data
    fooditem_ids = meal_data.pop('fooditem_ids', None)
    category_ids = meal_data.pop('category_ids', None)

    # Update scalar fields
    for key, value in meal_data.items():
        if hasattr(meal, key):
            setattr(meal, key, value)

    # Update food items (delete/recreate pattern)
    if fooditem_ids is not None:
        await db.execute(
            sql_delete(MealFoodItem).where(MealFoodItem.mf_meal_id == meal_id)
        )
        for fooditem_id in fooditem_ids:
            meal_food_item = MealFoodItem(
                mf_meal_id=meal_id,
                mf_fooditem_id=fooditem_id
            )
            db.add(meal_food_item)

    # Update categories (delete/recreate pattern)
    if category_ids is not None:
        await db.execute(
            sql_delete(MealCategory).where(MealCategory.meal_id == meal_id)
        )
        for category_id in category_ids:
            meal_category = MealCategory(
                meal_id=meal_id,
                category_id=category_id
            )
            db.add(meal_category)

    await db.commit()
    await db.refresh(meal)

    # Reload with nested data
    return await get_meal_by_id(db, meal_id)


async def delete_meal(db: AsyncSession, meal_id: int) -> bool:
    """Delete a meal."""
    meal = await db.get(Meal, meal_id)
    if not meal:
        return False

    await db.delete(meal)
    await db.commit()
    return True


# ============================================================================
# UnitType Operations
# ============================================================================

async def get_all_unit_types(db: AsyncSession) -> List[UnitType]:
    """Get all unit types."""
    stmt = select(UnitType)
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_unit_type_by_id(db: AsyncSession, unit_type_id: int) -> Optional[UnitType]:
    """Get a single unit type by ID."""
    return await db.get(UnitType, unit_type_id)


async def create_unit_type(db: AsyncSession, unit_type_data: Dict[str, Any]) -> UnitType:
    """Create a new unit type."""
    unit_type = UnitType(**unit_type_data)
    db.add(unit_type)
    await db.commit()
    await db.refresh(unit_type)
    return unit_type


async def update_unit_type(db: AsyncSession, unit_type_id: int, unit_type_data: Dict[str, Any]) -> Optional[UnitType]:
    """Update a unit type."""
    unit_type = await db.get(UnitType, unit_type_id)
    if not unit_type:
        return None

    for key, value in unit_type_data.items():
        if hasattr(unit_type, key):
            setattr(unit_type, key, value)

    await db.commit()
    await db.refresh(unit_type)
    return unit_type


async def delete_unit_type(db: AsyncSession, unit_type_id: int) -> bool:
    """Delete a unit type."""
    unit_type = await db.get(UnitType, unit_type_id)
    if not unit_type:
        return False

    await db.delete(unit_type)
    await db.commit()
    return True


# ============================================================================
# Search Operations
# ============================================================================

async def search_recipes(db: AsyncSession, q: str) -> List[Recipe]:
    """Search recipes by name."""
    stmt = (
        select(Recipe)
        .where(Recipe.recipe_name.like(f"%{q}%"))
        .options(
            selectinload(Recipe.ingredients),
            selectinload(Recipe.instructions),
            selectinload(Recipe.categories)
        )
    )
    result = await db.execute(stmt)
    return result.scalars().all()


async def search_meals(db: AsyncSession, q: str) -> List[Meal]:
    """Search meals by name or description."""
    stmt = (
        select(Meal)
        .where(
            or_(
                Meal.meal_name.like(f"%{q}%"),
                Meal.meal_description.like(f"%{q}%")
            )
        )
        .options(
            selectinload(Meal.meal_food_items).selectinload(MealFoodItem.food_item),
            selectinload(Meal.categories)
        )
    )
    result = await db.execute(stmt)
    return result.scalars().all()


async def search_food_items(db: AsyncSession, q: str) -> List[FoodItem]:
    """Search food items by name or description."""
    stmt = (
        select(FoodItem)
        .where(
            or_(
                FoodItem.fooditem_name.like(f"%{q}%"),
                FoodItem.fooditem_description.like(f"%{q}%")
            )
        )
        .options(selectinload(FoodItem.recipes))
    )
    result = await db.execute(stmt)
    return result.scalars().all()


async def search_ingredients(db: AsyncSession, q: str) -> List[Ingredient]:
    """Search ingredients by name or description."""
    stmt = (
        select(Ingredient)
        .where(
            or_(
                Ingredient.ingredient_name.like(f"%{q}%"),
                Ingredient.ingredient_description.like(f"%{q}%")
            )
        )
    )
    result = await db.execute(stmt)
    return result.scalars().all()


# ============================================================================
# Utility Operations
# ============================================================================

async def get_recipes_by_category(db: AsyncSession, category_id: int) -> List[Recipe]:
    """Get all recipes in a specific category."""
    stmt = (
        select(Recipe)
        .join(RecipeCategory)
        .where(RecipeCategory.category_id == category_id)
        .options(
            selectinload(Recipe.ingredients),
            selectinload(Recipe.instructions),
            selectinload(Recipe.categories)
        )
    )
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_recipes_by_food_item_id(db: AsyncSession, food_item_id: int) -> List[Recipe]:
    """Get all recipes that use a specific food item as an ingredient."""
    stmt = (
        select(Recipe)
        .join(RecipeIngredient)
        .where(RecipeIngredient.ri_fooditem_id == food_item_id)
        .distinct()
        .options(
            selectinload(Recipe.ingredients),
            selectinload(Recipe.instructions),
            selectinload(Recipe.categories)
        )
    )
    result = await db.execute(stmt)
    return result.scalars().all()
