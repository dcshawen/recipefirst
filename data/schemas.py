"""
Pydantic schemas for RecipeFirst API request/response validation.

These schemas match the existing API contract to ensure backward compatibility.
Request schemas include validation (including XOR constraint for RecipeIngredient).
Response schemas use from_attributes to convert ORM models to JSON.
"""

from pydantic import BaseModel, ConfigDict, Field, model_validator
from typing import Optional, List
from datetime import datetime


# ============================================================================
# Base Schemas with Timestamps
# ============================================================================

class TimestampSchema(BaseModel):
    """Base schema with timestamp fields."""
    created_at: datetime
    updated_at: datetime


# ============================================================================
# UnitType Schemas
# ============================================================================

class UnitTypeBase(BaseModel):
    """Base UnitType schema."""
    unit_type: str


class UnitTypeCreate(UnitTypeBase):
    """Schema for creating a new unit type."""
    pass


class UnitTypeUpdate(BaseModel):
    """Schema for updating a unit type."""
    unit_type: Optional[str] = None


class UnitTypeResponse(UnitTypeBase, TimestampSchema):
    """Schema for unit type responses."""
    id: int

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# Category Schemas
# ============================================================================

class CategoryBase(BaseModel):
    """Base Category schema."""
    category_name: str
    category_description: Optional[str] = None
    parent_category_id: Optional[int] = None


class CategoryCreate(CategoryBase):
    """Schema for creating a new category."""
    pass


class CategoryUpdate(BaseModel):
    """Schema for updating a category."""
    category_name: Optional[str] = None
    category_description: Optional[str] = None
    parent_category_id: Optional[int] = None


class CategoryResponse(CategoryBase, TimestampSchema):
    """Schema for category responses. Matches current API format."""
    category_id: int

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# Ingredient Schemas
# ============================================================================

class IngredientBase(BaseModel):
    """Base Ingredient schema."""
    ingredient_name: str
    ingredient_description: Optional[str] = None
    ingredient_notes: Optional[str] = None


class IngredientCreate(IngredientBase):
    """Schema for creating a new ingredient."""
    pass


class IngredientUpdate(BaseModel):
    """Schema for updating an ingredient."""
    ingredient_name: Optional[str] = None
    ingredient_description: Optional[str] = None
    ingredient_notes: Optional[str] = None


class IngredientResponse(IngredientBase, TimestampSchema):
    """Schema for ingredient responses."""
    ingredient_id: int

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# FoodItem Schemas
# ============================================================================

class FoodItemBase(BaseModel):
    """Base FoodItem schema."""
    fooditem_name: str
    fooditem_description: Optional[str] = None


class FoodItemCreate(FoodItemBase):
    """Schema for creating a new food item."""
    pass


class FoodItemUpdate(BaseModel):
    """Schema for updating a food item."""
    fooditem_name: Optional[str] = None
    fooditem_description: Optional[str] = None


class FoodItemResponse(FoodItemBase, TimestampSchema):
    """Schema for food item responses."""
    fooditem_id: int

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# RecipeIngredient Schemas (with XOR constraint)
# ============================================================================

class RecipeIngredientBase(BaseModel):
    """Base RecipeIngredient schema."""
    ri_ingredient_id: Optional[int] = None
    ri_fooditem_id: Optional[int] = None
    ri_unit_type_id: int
    ri_quantity: float


class RecipeIngredientCreate(RecipeIngredientBase):
    """
    Schema for creating a new recipe ingredient.

    Enforces XOR constraint: must have EITHER ri_ingredient_id OR ri_fooditem_id.
    """

    @model_validator(mode='after')
    def validate_xor_constraint(self):
        """Validate that exactly one of ingredient_id or fooditem_id is set."""
        has_ingredient = self.ri_ingredient_id is not None
        has_fooditem = self.ri_fooditem_id is not None

        if has_ingredient == has_fooditem:  # Both True or both False
            raise ValueError(
                'Exactly one of ri_ingredient_id or ri_fooditem_id must be set (not both, not neither)'
            )
        return self


class RecipeIngredientUpdate(BaseModel):
    """Schema for updating a recipe ingredient."""
    ri_ingredient_id: Optional[int] = None
    ri_fooditem_id: Optional[int] = None
    ri_unit_type_id: Optional[int] = None
    ri_quantity: Optional[float] = None

    @model_validator(mode='after')
    def validate_xor_if_both_present(self):
        """Validate XOR if both fields are being updated."""
        # Allow partial updates, but if both are specified, enforce XOR
        if self.ri_ingredient_id is not None and self.ri_fooditem_id is not None:
            raise ValueError('Cannot set both ri_ingredient_id and ri_fooditem_id')
        return self


class RecipeIngredientResponse(RecipeIngredientBase, TimestampSchema):
    """
    Schema for recipe ingredient responses.

    Matches the current API format which includes joined data from
    Ingredient, FoodItem, and UnitType tables.
    """
    ri_id: int
    ri_recipe_id: int

    # Joined fields from related tables
    ingredient_name: Optional[str] = None
    ingredient_description: Optional[str] = None
    ingredient_notes: Optional[str] = None
    fooditem_name: Optional[str] = None
    fooditem_description: Optional[str] = None
    unit_type: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# RecipeInstruction Schemas
# ============================================================================

class RecipeInstructionBase(BaseModel):
    """Base RecipeInstruction schema."""
    step_number: int
    instruction_text: str


class RecipeInstructionCreate(RecipeInstructionBase):
    """Schema for creating a new recipe instruction."""
    pass


class RecipeInstructionUpdate(BaseModel):
    """Schema for updating a recipe instruction."""
    step_number: Optional[int] = None
    instruction_text: Optional[str] = None


class RecipeInstructionResponse(RecipeInstructionBase):
    """
    Schema for recipe instruction responses.

    Matches current API format (only step_number and instruction_text).
    """
    # Note: Current API only returns step_number and instruction_text
    # Not including instruction_id, recipe_id, or timestamps

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# Recipe Schemas
# ============================================================================

class RecipeBase(BaseModel):
    """Base Recipe schema."""
    recipe_name: str
    recipe_description: Optional[str] = None
    recipe_fooditem_id: int


class RecipeCreate(RecipeBase):
    """
    Schema for creating a new recipe.

    Can include nested ingredients, instructions, and categories.
    """
    ingredients: Optional[List[RecipeIngredientCreate]] = []
    instructions: Optional[List[RecipeInstructionCreate]] = []
    category_ids: Optional[List[int]] = []


class RecipeUpdate(BaseModel):
    """Schema for updating a recipe."""
    recipe_name: Optional[str] = None
    recipe_description: Optional[str] = None
    recipe_fooditem_id: Optional[int] = None
    ingredients: Optional[List[RecipeIngredientCreate]] = None
    instructions: Optional[List[RecipeInstructionCreate]] = None
    category_ids: Optional[List[int]] = None


class RecipeResponse(RecipeBase, TimestampSchema):
    """
    Schema for recipe responses.

    Matches current API format with nested ingredients, instructions, and categories.
    """
    recipe_id: int
    ingredients: List[RecipeIngredientResponse] = []
    instructions: List[RecipeInstructionResponse] = []
    categories: List[CategoryResponse] = []

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# Meal Schemas
# ============================================================================

class MealBase(BaseModel):
    """Base Meal schema."""
    meal_name: str
    meal_description: Optional[str] = None


class MealCreate(MealBase):
    """Schema for creating a new meal."""
    fooditem_ids: Optional[List[int]] = []
    category_ids: Optional[List[int]] = []


class MealUpdate(BaseModel):
    """Schema for updating a meal."""
    meal_name: Optional[str] = None
    meal_description: Optional[str] = None
    fooditem_ids: Optional[List[int]] = None
    category_ids: Optional[List[int]] = None


class MealFoodItemResponse(BaseModel):
    """Schema for meal food item association."""
    fooditem_id: int
    fooditem_name: str
    fooditem_description: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class MealResponse(MealBase, TimestampSchema):
    """
    Schema for meal responses.

    Matches current API format with nested food items and categories.
    """
    meal_id: int
    food_items: List[MealFoodItemResponse] = []
    categories: List[CategoryResponse] = []

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# Search Response Schemas
# ============================================================================

class SearchResultsResponse(BaseModel):
    """Schema for omni-search results across all entity types."""
    recipes: List[RecipeResponse] = []
    ingredients: List[IngredientResponse] = []
    food_items: List[FoodItemResponse] = []
    meals: List[MealResponse] = []

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# List Response Wrappers (matching current API format)
# ============================================================================

class RecipesListResponse(BaseModel):
    """Wrapper for list of recipes. Matches current /recipes endpoint format."""
    recipes: List[RecipeResponse]


class IngredientsListResponse(BaseModel):
    """Wrapper for list of ingredients. Matches current /ingredients endpoint format."""
    ingredients: List[IngredientResponse]


class FoodItemsListResponse(BaseModel):
    """Wrapper for list of food items. Matches current /food-items endpoint format."""
    food_items: List[FoodItemResponse]


class MealsListResponse(BaseModel):
    """Wrapper for list of meals. Matches current /meals endpoint format."""
    meals: List[MealResponse]


class CategoriesListResponse(BaseModel):
    """Wrapper for list of categories. Matches current /categories endpoint format."""
    categories: List[CategoryResponse]


class UnitTypesListResponse(BaseModel):
    """Wrapper for list of unit types. Matches current /unit-types endpoint format."""
    unit_types: List[UnitTypeResponse]


# ============================================================================
# Generic Message Response
# ============================================================================

class MessageResponse(BaseModel):
    """Generic message response for operations like delete, update."""
    message: str
