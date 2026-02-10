#!/usr/bin/env python3
"""
Seed the database with starter data: Units, Categories, and basic Ingredients.

This script populates the database with:
- Common measurement units (cup, tablespoon, gram, etc.)
- Standard categories (Breakfast, Lunch, Dinner, Cuisine types, etc.)
- Basic ingredients (salt, pepper, flour, sugar, etc.)

Usage:
    docker compose exec fastapi python seed_data.py
"""

import asyncio
import sys
from pathlib import Path

# Add parent directory to path to enable imports
sys.path.insert(0, str(Path(__file__).parent))

from data.database import AsyncSessionLocal
from data.models import UnitType, Category, Ingredient


# Measurement Units
UNITS = [
    "cup",
    "tablespoon",
    "teaspoon",
    "gram",
    "kilogram",
    "ounce",
    "pound",
    "milliliter",
    "liter",
    "fluid ounce",
    "pint",
    "quart",
    "gallon",
    "piece",
    "slice",
    "clove",
    "pinch",
    "dash",
    "whole",
    "can",
    "package",
]

# Categories (hierarchical structure)
CATEGORIES = [
    # Meal Types
    {"name": "Breakfast", "description": "Morning meals", "parent": None},
    {"name": "Lunch", "description": "Midday meals", "parent": None},
    {"name": "Dinner", "description": "Evening meals", "parent": None},
    {"name": "Snack", "description": "Light meals between main meals", "parent": None},
    {"name": "Dessert", "description": "Sweet treats", "parent": None},

    # Cuisine Types
    {"name": "Italian", "description": "Italian cuisine", "parent": None},
    {"name": "Mexican", "description": "Mexican cuisine", "parent": None},
    {"name": "Chinese", "description": "Chinese cuisine", "parent": None},
    {"name": "Indian", "description": "Indian cuisine", "parent": None},
    {"name": "Japanese", "description": "Japanese cuisine", "parent": None},
    {"name": "Thai", "description": "Thai cuisine", "parent": None},
    {"name": "Mediterranean", "description": "Mediterranean cuisine", "parent": None},
    {"name": "American", "description": "American cuisine", "parent": None},
    {"name": "French", "description": "French cuisine", "parent": None},

    # Dietary Preferences
    {"name": "Vegetarian", "description": "No meat or fish", "parent": None},
    {"name": "Vegan", "description": "No animal products", "parent": None},
    {"name": "Gluten-Free", "description": "No gluten", "parent": None},
    {"name": "Dairy-Free", "description": "No dairy products", "parent": None},
    {"name": "Low-Carb", "description": "Reduced carbohydrates", "parent": None},
    {"name": "Keto", "description": "Very low carb, high fat", "parent": None},

    # Cooking Methods
    {"name": "Baked", "description": "Cooked in oven", "parent": None},
    {"name": "Grilled", "description": "Cooked on grill", "parent": None},
    {"name": "Fried", "description": "Cooked in oil", "parent": None},
    {"name": "Slow Cooker", "description": "Cooked in slow cooker", "parent": None},
    {"name": "Quick & Easy", "description": "Ready in under 30 minutes", "parent": None},
]

# Basic Ingredients (organized by category)
INGREDIENTS = [
    # Spices & Seasonings
    {"name": "Salt", "description": "Table salt or sea salt", "notes": "Essential seasoning"},
    {"name": "Black Pepper", "description": "Ground black pepper", "notes": "Common spice"},
    {"name": "Garlic Powder", "description": "Dried ground garlic", "notes": "Seasoning"},
    {"name": "Onion Powder", "description": "Dried ground onion", "notes": "Seasoning"},
    {"name": "Paprika", "description": "Ground dried peppers", "notes": "Adds color and mild flavor"},
    {"name": "Cumin", "description": "Ground cumin seeds", "notes": "Earthy, warm flavor"},
    {"name": "Oregano", "description": "Dried oregano leaves", "notes": "Mediterranean herb"},
    {"name": "Basil", "description": "Dried basil leaves", "notes": "Sweet herb"},
    {"name": "Thyme", "description": "Dried thyme leaves", "notes": "Savory herb"},
    {"name": "Rosemary", "description": "Dried rosemary leaves", "notes": "Pine-like flavor"},
    {"name": "Cinnamon", "description": "Ground cinnamon", "notes": "Sweet spice"},
    {"name": "Chili Powder", "description": "Ground chili peppers", "notes": "Adds heat"},

    # Baking Essentials
    {"name": "All-Purpose Flour", "description": "White wheat flour", "notes": "Basic baking ingredient"},
    {"name": "Sugar", "description": "White granulated sugar", "notes": "Sweetener"},
    {"name": "Brown Sugar", "description": "Brown granulated sugar", "notes": "Molasses flavor"},
    {"name": "Baking Powder", "description": "Leavening agent", "notes": "For baking"},
    {"name": "Baking Soda", "description": "Sodium bicarbonate", "notes": "Leavening agent"},
    {"name": "Vanilla Extract", "description": "Pure vanilla extract", "notes": "Flavoring"},

    # Oils & Fats
    {"name": "Olive Oil", "description": "Extra virgin olive oil", "notes": "Cooking and dressing"},
    {"name": "Vegetable Oil", "description": "Neutral cooking oil", "notes": "High smoke point"},
    {"name": "Butter", "description": "Unsalted butter", "notes": "Cooking and baking"},
    {"name": "Coconut Oil", "description": "Refined or unrefined", "notes": "High heat cooking"},

    # Liquids & Sauces
    {"name": "Water", "description": "Filtered water", "notes": "Essential liquid"},
    {"name": "Milk", "description": "Whole milk", "notes": "Dairy product"},
    {"name": "Chicken Broth", "description": "Chicken stock", "notes": "Cooking liquid"},
    {"name": "Vegetable Broth", "description": "Vegetable stock", "notes": "Vegetarian cooking liquid"},
    {"name": "Soy Sauce", "description": "Fermented soy sauce", "notes": "Salty umami flavor"},
    {"name": "Vinegar", "description": "White or apple cider vinegar", "notes": "Acid for cooking"},

    # Fresh Produce (Common)
    {"name": "Garlic", "description": "Fresh garlic cloves", "notes": "Aromatic vegetable"},
    {"name": "Onion", "description": "Yellow or white onion", "notes": "Aromatic vegetable"},
    {"name": "Tomato", "description": "Fresh tomatoes", "notes": "Fruit vegetable"},
    {"name": "Potato", "description": "White or Russet potato", "notes": "Starchy vegetable"},
    {"name": "Carrot", "description": "Fresh carrots", "notes": "Root vegetable"},
    {"name": "Bell Pepper", "description": "Green, red, or yellow pepper", "notes": "Sweet pepper"},
    {"name": "Lemon", "description": "Fresh lemon", "notes": "Citrus fruit"},

    # Proteins
    {"name": "Eggs", "description": "Large chicken eggs", "notes": "Versatile protein"},
    {"name": "Chicken Breast", "description": "Boneless, skinless chicken breast", "notes": "Lean protein"},
    {"name": "Ground Beef", "description": "Ground beef (80/20)", "notes": "Versatile meat"},

    # Grains & Pasta
    {"name": "Rice", "description": "White or brown rice", "notes": "Grain staple"},
    {"name": "Pasta", "description": "Dried pasta (spaghetti, penne, etc.)", "notes": "Italian staple"},
    {"name": "Bread", "description": "Sliced bread", "notes": "Baked staple"},

    # Canned Goods
    {"name": "Canned Tomatoes", "description": "Diced or crushed tomatoes", "notes": "Cooking base"},
    {"name": "Tomato Paste", "description": "Concentrated tomato paste", "notes": "Thickener and flavor"},
]


async def seed_database():
    """Populate database with starter data."""
    async with AsyncSessionLocal() as session:
        print("\n" + "="*60)
        print("Seeding Database with Starter Data")
        print("="*60 + "\n")

        # 1. Add Unit Types
        print("Adding measurement units...")
        existing_units = set()

        for unit_name in UNITS:
            unit = UnitType(unit_type=unit_name)
            session.add(unit)
            existing_units.add(unit_name)

        await session.commit()
        print(f"✓ Added {len(UNITS)} measurement units\n")

        # 2. Add Categories
        print("Adding categories...")
        category_map = {}

        for cat_data in CATEGORIES:
            category = Category(
                category_name=cat_data["name"],
                category_description=cat_data["description"],
                parent_category_id=None  # Flat structure for now
            )
            session.add(category)
            category_map[cat_data["name"]] = category

        await session.commit()
        print(f"✓ Added {len(CATEGORIES)} categories\n")

        # 3. Add Ingredients
        print("Adding basic ingredients...")

        for ing_data in INGREDIENTS:
            ingredient = Ingredient(
                ingredient_name=ing_data["name"],
                ingredient_description=ing_data["description"],
                ingredient_notes=ing_data["notes"]
            )
            session.add(ingredient)

        await session.commit()
        print(f"✓ Added {len(INGREDIENTS)} ingredients\n")

        print("="*60)
        print("Database seeding complete!")
        print("="*60)
        print(f"\nSummary:")
        print(f"  - {len(UNITS)} Unit Types")
        print(f"  - {len(CATEGORIES)} Categories")
        print(f"  - {len(INGREDIENTS)} Ingredients")
        print(f"\nYou can now start creating recipes and meals!\n")


async def main():
    """Main entry point."""
    try:
        # Check if data already exists
        async with AsyncSessionLocal() as session:
            from sqlalchemy import select, func

            # Count existing units
            result = await session.execute(select(func.count(UnitType.id)))
            unit_count = result.scalar()

            if unit_count > 0:
                print(f"\n⚠️  Database already contains {unit_count} unit types.")
                print("Skipping seed (data already exists).\n")
                return

        await seed_database()

    except Exception as e:
        print(f"\n✗ Error seeding database: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
