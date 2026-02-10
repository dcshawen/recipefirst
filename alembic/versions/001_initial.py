"""Initial migration

Revision ID: 001_initial
Revises:
Create Date: 2026-02-10 16:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create UnitType table
    op.create_table('UnitType',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('unit_type', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('unit_type')
    )

    # Create Category table
    op.create_table('Category',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.Text(), nullable=False),
    sa.Column('category_description', sa.Text(), nullable=True),
    sa.Column('parent_category_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['parent_category_id'], ['Category.category_id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('category_id')
    )
    op.create_index('idx_category_parent', 'Category', ['parent_category_id'], unique=False)

    # Create Ingredient table
    op.create_table('Ingredient',
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.Column('ingredient_name', sa.Text(), nullable=False),
    sa.Column('ingredient_description', sa.Text(), nullable=True),
    sa.Column('ingredient_notes', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('ingredient_id')
    )

    # Create FoodItem table
    op.create_table('FoodItem',
    sa.Column('fooditem_id', sa.Integer(), nullable=False),
    sa.Column('fooditem_name', sa.Text(), nullable=False),
    sa.Column('fooditem_description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('fooditem_id')
    )

    # Create Meal table
    op.create_table('Meal',
    sa.Column('meal_id', sa.Integer(), nullable=False),
    sa.Column('meal_name', sa.Text(), nullable=False),
    sa.Column('meal_description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('meal_id')
    )

    # Create Recipe table
    op.create_table('Recipe',
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('recipe_name', sa.Text(), nullable=False),
    sa.Column('recipe_description', sa.Text(), nullable=True),
    sa.Column('recipe_fooditem_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['recipe_fooditem_id'], ['FoodItem.fooditem_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('recipe_id')
    )

    # Create RecipeInstruction table
    op.create_table('RecipeInstruction',
    sa.Column('instruction_id', sa.Integer(), nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('step_number', sa.Integer(), nullable=False),
    sa.Column('instruction_text', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['Recipe.recipe_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('instruction_id'),
    sa.UniqueConstraint('recipe_id', 'step_number', name='uq_recipe_step')
    )
    op.create_index('idx_recipe_instruction_recipe_id', 'RecipeInstruction', ['recipe_id'], unique=False)

    # Create RecipeIngredient table
    op.create_table('RecipeIngredient',
    sa.Column('ri_id', sa.Integer(), nullable=False),
    sa.Column('ri_recipe_id', sa.Integer(), nullable=False),
    sa.Column('ri_ingredient_id', sa.Integer(), nullable=True),
    sa.Column('ri_fooditem_id', sa.Integer(), nullable=True),
    sa.Column('ri_unit_type_id', sa.Integer(), nullable=False),
    sa.Column('ri_quantity', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.CheckConstraint('(ri_ingredient_id IS NOT NULL AND ri_fooditem_id IS NULL) OR (ri_ingredient_id IS NULL AND ri_fooditem_id IS NOT NULL)', name='ck_ri_source'),
    sa.ForeignKeyConstraint(['ri_fooditem_id'], ['FoodItem.fooditem_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['ri_ingredient_id'], ['Ingredient.ingredient_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['ri_recipe_id'], ['Recipe.recipe_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['ri_unit_type_id'], ['UnitType.id'], ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('ri_id')
    )

    # Create MealFoodItem table
    op.create_table('MealFoodItem',
    sa.Column('mf_id', sa.Integer(), nullable=False),
    sa.Column('mf_meal_id', sa.Integer(), nullable=False),
    sa.Column('mf_fooditem_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['mf_fooditem_id'], ['FoodItem.fooditem_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['mf_meal_id'], ['Meal.meal_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('mf_id'),
    sa.UniqueConstraint('mf_meal_id', 'mf_fooditem_id', name='uq_meal_fooditem')
    )

    # Create junction tables
    op.create_table('RecipeCategory',
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['Category.category_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['recipe_id'], ['Recipe.recipe_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('recipe_id', 'category_id')
    )
    op.create_index('idx_recipe_category_category_id', 'RecipeCategory', ['category_id'], unique=False)

    op.create_table('IngredientCategory',
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['Category.category_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['ingredient_id'], ['Ingredient.ingredient_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('ingredient_id', 'category_id')
    )
    op.create_index('idx_ingredient_category_category_id', 'IngredientCategory', ['category_id'], unique=False)

    op.create_table('MealCategory',
    sa.Column('meal_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['Category.category_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['meal_id'], ['Meal.meal_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('meal_id', 'category_id')
    )
    op.create_index('idx_meal_category_category_id', 'MealCategory', ['category_id'], unique=False)


def downgrade() -> None:
    op.drop_index('idx_meal_category_category_id', table_name='MealCategory')
    op.drop_table('MealCategory')
    op.drop_index('idx_ingredient_category_category_id', table_name='IngredientCategory')
    op.drop_table('IngredientCategory')
    op.drop_index('idx_recipe_category_category_id', table_name='RecipeCategory')
    op.drop_table('RecipeCategory')
    op.drop_table('MealFoodItem')
    op.drop_table('RecipeIngredient')
    op.drop_index('idx_recipe_instruction_recipe_id', table_name='RecipeInstruction')
    op.drop_table('RecipeInstruction')
    op.drop_table('Recipe')
    op.drop_table('Meal')
    op.drop_table('FoodItem')
    op.drop_table('Ingredient')
    op.drop_index('idx_category_parent', table_name='Category')
    op.drop_table('Category')
    op.drop_table('UnitType')
