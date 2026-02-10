"""
SQLAlchemy ORM models for RecipeFirst application.

This module defines all database models matching the existing schema.sql structure.
Models include proper relationships, cascade behaviors, and the XOR constraint
for RecipeIngredient.
"""

from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, CheckConstraint, UniqueConstraint, Index
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.hybrid import hybrid_property
from typing import Optional
from datetime import datetime


class Base(DeclarativeBase):
    """Base class for all ORM models."""
    pass


class TimestampMixin:
    """
    Mixin to add created_at and updated_at timestamps to models.

    Uses SQLAlchemy's onupdate to automatically update timestamps,
    matching the behavior of the existing database triggers.
    """
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)


# ============================================================================
# Core Entity Models
# ============================================================================

class UnitType(Base, TimestampMixin):
    """Measurement units for recipe ingredients (cup, tablespoon, gram, etc.)."""
    __tablename__ = 'UnitType'

    id = Column(Integer, primary_key=True)
    unit_type = Column(Text, nullable=False, unique=True)

    # Relationships
    recipe_ingredients = relationship("RecipeIngredient", back_populates="unit_type")

    def __repr__(self):
        return f"<UnitType(id={self.id}, unit_type='{self.unit_type}')>"


class Category(Base, TimestampMixin):
    """
    Hierarchical category system for organizing recipes, ingredients, and meals.

    Examples: Breakfast, Italian, Vegetarian, Quick & Easy
    Supports parent-child relationships for category hierarchy.
    """
    __tablename__ = 'Category'

    category_id = Column(Integer, primary_key=True)
    category_name = Column(Text, nullable=False)
    category_description = Column(Text)
    parent_category_id = Column(Integer, ForeignKey('Category.category_id', ondelete='SET NULL'))

    # Self-referential relationship for hierarchy
    parent = relationship("Category", remote_side=[category_id], back_populates="children")
    children = relationship("Category", back_populates="parent")

    # Many-to-many relationships via junction tables
    recipes = relationship("Recipe", secondary="RecipeCategory", back_populates="categories")
    ingredients = relationship("Ingredient", secondary="IngredientCategory", back_populates="categories")
    meals = relationship("Meal", secondary="MealCategory", back_populates="categories")

    __table_args__ = (
        Index('idx_category_parent', 'parent_category_id'),
    )

    def __repr__(self):
        return f"<Category(id={self.category_id}, name='{self.category_name}')>"


class Ingredient(Base, TimestampMixin):
    """Raw ingredients used in recipes (salt, pepper, flour, etc.)."""
    __tablename__ = 'Ingredient'

    ingredient_id = Column(Integer, primary_key=True)
    ingredient_name = Column(Text, nullable=False)
    ingredient_description = Column(Text)
    ingredient_notes = Column(Text)

    # Relationships
    recipe_ingredients = relationship(
        "RecipeIngredient",
        back_populates="ingredient",
        cascade="all, delete",  # Cascade deletes to RecipeIngredient
        passive_deletes=True    # Let database handle ON DELETE CASCADE
    )
    categories = relationship("Category", secondary="IngredientCategory", back_populates="ingredients")

    def __repr__(self):
        return f"<Ingredient(id={self.ingredient_id}, name='{self.ingredient_name}')>"


class FoodItem(Base, TimestampMixin):
    """
    Prepared food items that can be produced by recipes.

    Examples: "Spaghetti Carbonara", "Chocolate Chip Cookies"
    Can be used as ingredients in other recipes (compound recipes).
    """
    __tablename__ = 'FoodItem'

    fooditem_id = Column(Integer, primary_key=True)
    fooditem_name = Column(Text, nullable=False)
    fooditem_description = Column(Text)

    # Relationships
    recipes = relationship(
        "Recipe",
        back_populates="food_item",
        cascade="all, delete",  # Cascade deletes to Recipe
        passive_deletes=True    # Let database handle ON DELETE CASCADE
    )
    recipe_ingredients = relationship(
        "RecipeIngredient",
        back_populates="fooditem",
        cascade="all, delete",  # Cascade deletes to RecipeIngredient
        passive_deletes=True    # Let database handle ON DELETE CASCADE
    )
    meal_food_items = relationship(
        "MealFoodItem",
        back_populates="food_item",
        cascade="all, delete",  # Cascade deletes to MealFoodItem
        passive_deletes=True    # Let database handle ON DELETE CASCADE
    )

    def __repr__(self):
        return f"<FoodItem(id={self.fooditem_id}, name='{self.fooditem_name}')>"


class Recipe(Base, TimestampMixin):
    """
    Recipe definition that produces exactly one FoodItem.

    Contains ingredients, instructions, and categories.
    Multiple recipes can produce the same food item.
    """
    __tablename__ = 'Recipe'

    recipe_id = Column(Integer, primary_key=True)
    recipe_name = Column(Text, nullable=False)
    recipe_description = Column(Text)
    recipe_fooditem_id = Column(Integer, ForeignKey('FoodItem.fooditem_id', ondelete='CASCADE'), nullable=False)

    # Relationships with eager loading to prevent N+1 queries
    food_item = relationship("FoodItem", back_populates="recipes")

    ingredients = relationship(
        "RecipeIngredient",
        back_populates="recipe",
        lazy="selectin",  # Eager load to avoid N+1
        cascade="all, delete-orphan"
    )

    instructions = relationship(
        "RecipeInstruction",
        back_populates="recipe",
        lazy="selectin",  # Eager load to avoid N+1
        cascade="all, delete-orphan",
        order_by="RecipeInstruction.step_number"
    )

    categories = relationship(
        "Category",
        secondary="RecipeCategory",
        back_populates="recipes",
        lazy="selectin"  # Eager load to avoid N+1
    )

    def __repr__(self):
        return f"<Recipe(id={self.recipe_id}, name='{self.recipe_name}')>"


class RecipeInstruction(Base, TimestampMixin):
    """Step-by-step cooking instructions for a recipe."""
    __tablename__ = 'RecipeInstruction'

    instruction_id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('Recipe.recipe_id', ondelete='CASCADE'), nullable=False)
    step_number = Column(Integer, nullable=False)
    instruction_text = Column(Text, nullable=False)

    # Relationships
    recipe = relationship("Recipe", back_populates="instructions")

    __table_args__ = (
        UniqueConstraint('recipe_id', 'step_number', name='uq_recipe_step'),
        Index('idx_recipe_instruction_recipe_id', 'recipe_id'),
    )

    def __repr__(self):
        return f"<RecipeInstruction(recipe_id={self.recipe_id}, step={self.step_number})>"


class RecipeIngredient(Base, TimestampMixin):
    """
    Junction table linking recipes to ingredients or food items.

    IMPORTANT: Enforces XOR constraint - must have EITHER ri_ingredient_id OR ri_fooditem_id,
    but not both. This allows recipes to use either raw ingredients or prepared food items.
    """
    __tablename__ = 'RecipeIngredient'

    ri_id = Column(Integer, primary_key=True)
    ri_recipe_id = Column(Integer, ForeignKey('Recipe.recipe_id', ondelete='CASCADE'), nullable=False)
    ri_ingredient_id = Column(Integer, ForeignKey('Ingredient.ingredient_id', ondelete='CASCADE'))
    ri_fooditem_id = Column(Integer, ForeignKey('FoodItem.fooditem_id', ondelete='CASCADE'))
    ri_unit_type_id = Column(Integer, ForeignKey('UnitType.id', ondelete='RESTRICT'), nullable=False)
    ri_quantity = Column(Float, nullable=False)

    # Relationships with eager loading for nested queries
    recipe = relationship("Recipe", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="recipe_ingredients", lazy="selectin")
    fooditem = relationship("FoodItem", back_populates="recipe_ingredients", lazy="selectin")
    unit_type = relationship("UnitType", back_populates="recipe_ingredients", lazy="selectin")

    # XOR constraint enforcement at database level
    __table_args__ = (
        CheckConstraint(
            '(ri_ingredient_id IS NOT NULL AND ri_fooditem_id IS NULL) OR '
            '(ri_ingredient_id IS NULL AND ri_fooditem_id IS NOT NULL)',
            name='ck_ri_source'
        ),
    )

    # Note: Removed @validates decorator to prevent interference with cascade deletes.
    # XOR constraint is enforced at database level via CHECK constraint above,
    # and at API level via Pydantic validation in schemas.py

    @hybrid_property
    def source_item(self):
        """
        Convenience property to get either the ingredient or fooditem.

        Returns the ingredient if present, otherwise the fooditem.
        """
        return self.ingredient if self.ingredient else self.fooditem

    @hybrid_property
    def source_name(self) -> Optional[str]:
        """Get the name of the source (ingredient or fooditem)."""
        if self.ingredient:
            return self.ingredient.ingredient_name
        elif self.fooditem:
            return self.fooditem.fooditem_name
        return None

    def __repr__(self):
        source = "Ingredient" if self.ri_ingredient_id else "FoodItem"
        source_id = self.ri_ingredient_id or self.ri_fooditem_id
        return f"<RecipeIngredient(id={self.ri_id}, recipe={self.ri_recipe_id}, {source}={source_id})>"


class Meal(Base, TimestampMixin):
    """A meal composed of multiple food items."""
    __tablename__ = 'Meal'

    meal_id = Column(Integer, primary_key=True)
    meal_name = Column(Text, nullable=False)
    meal_description = Column(Text)

    # Relationships with eager loading
    # Note: removed back_populates since this is a viewonly convenience relationship
    # Access food items through meal.meal_food_items[i].food_item or this shortcut
    food_items = relationship(
        "FoodItem",
        secondary="MealFoodItem",
        lazy="selectin",
        viewonly=True  # Use MealFoodItem for modifications
    )

    meal_food_items = relationship(
        "MealFoodItem",
        back_populates="meal",
        lazy="selectin",
        cascade="all, delete-orphan"
    )

    categories = relationship(
        "Category",
        secondary="MealCategory",
        back_populates="meals",
        lazy="selectin"
    )

    def __repr__(self):
        return f"<Meal(id={self.meal_id}, name='{self.meal_name}')>"


class MealFoodItem(Base, TimestampMixin):
    """Junction table linking meals to food items."""
    __tablename__ = 'MealFoodItem'

    mf_id = Column(Integer, primary_key=True)
    mf_meal_id = Column(Integer, ForeignKey('Meal.meal_id', ondelete='CASCADE'), nullable=False)
    mf_fooditem_id = Column(Integer, ForeignKey('FoodItem.fooditem_id', ondelete='CASCADE'), nullable=False)

    # Relationships
    meal = relationship("Meal", back_populates="meal_food_items")
    food_item = relationship("FoodItem", back_populates="meal_food_items")

    __table_args__ = (
        UniqueConstraint('mf_meal_id', 'mf_fooditem_id', name='uq_meal_fooditem'),
    )

    def __repr__(self):
        return f"<MealFoodItem(meal_id={self.mf_meal_id}, fooditem_id={self.mf_fooditem_id})>"


# ============================================================================
# Junction Tables for Many-to-Many Relationships with Categories
# ============================================================================

class RecipeCategory(Base):
    """Junction table for recipe-category many-to-many relationship."""
    __tablename__ = 'RecipeCategory'

    recipe_id = Column(Integer, ForeignKey('Recipe.recipe_id', ondelete='CASCADE'), primary_key=True)
    category_id = Column(Integer, ForeignKey('Category.category_id', ondelete='CASCADE'), primary_key=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    __table_args__ = (
        Index('idx_recipe_category_category_id', 'category_id'),
    )

    def __repr__(self):
        return f"<RecipeCategory(recipe_id={self.recipe_id}, category_id={self.category_id})>"


class IngredientCategory(Base):
    """Junction table for ingredient-category many-to-many relationship."""
    __tablename__ = 'IngredientCategory'

    ingredient_id = Column(Integer, ForeignKey('Ingredient.ingredient_id', ondelete='CASCADE'), primary_key=True)
    category_id = Column(Integer, ForeignKey('Category.category_id', ondelete='CASCADE'), primary_key=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    __table_args__ = (
        Index('idx_ingredient_category_category_id', 'category_id'),
    )

    def __repr__(self):
        return f"<IngredientCategory(ingredient_id={self.ingredient_id}, category_id={self.category_id})>"


class MealCategory(Base):
    """Junction table for meal-category many-to-many relationship."""
    __tablename__ = 'MealCategory'

    meal_id = Column(Integer, ForeignKey('Meal.meal_id', ondelete='CASCADE'), primary_key=True)
    category_id = Column(Integer, ForeignKey('Category.category_id', ondelete='CASCADE'), primary_key=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    __table_args__ = (
        Index('idx_meal_category_category_id', 'category_id'),
    )

    def __repr__(self):
        return f"<MealCategory(meal_id={self.meal_id}, category_id={self.category_id})>"
