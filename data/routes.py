from fastapi import APIRouter, HTTPException, Body, Path, Query
import db

router = APIRouter()

MAX_RECIPES = 1000

@router.get("/")
async def root():
    return {"message": db.getDBSchema()}

# Recipes endpoints
@router.get("/recipes")
async def get_recipes():
    return {"recipes": db.get_all_recipes()}

@router.get("/recipes/{id}")
async def get_recipe(id: int = Path(..., description="The ID of the recipe to retrieve", gt=0)):
    recipe = db.get_recipe_by_id(id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@router.post("/recipes")
async def create_recipe(recipe_data = Body(...)):
    return db.create_recipe(recipe_data)

@router.put("/recipes/{id}")
async def update_recipe(id: int = Path(..., gt=0), recipe_data = Body(...)):
    updated = db.update_recipe(id, recipe_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return {"message": "Recipe updated successfully"}

@router.delete("/recipes/{id}")
async def delete_recipe(id: int = Path(..., gt=0)):
    deleted = db.delete_recipe(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return {"message": "Recipe deleted successfully"}

# Ingredients endpoints
@router.get("/ingredients")
async def get_ingredients():
    return {"ingredients": db.get_all_ingredients()}

@router.get("/ingredients/{id}")
async def get_ingredient(id: int = Path(..., gt=-1)):
    ingredient = db.get_ingredient_by_id(id)
    if ingredient is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return ingredient

@router.post("/ingredients")
async def create_ingredient(ingredient_data = Body(...)):
    return db.create_ingredient(ingredient_data)

@router.put("/ingredients/{id}")
async def update_ingredient(id: int = Path(..., gt=0), ingredient_data = Body(...)):
    updated = db.update_ingredient(id, ingredient_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return {"message": "Ingredient updated successfully"}

@router.delete("/ingredients/{id}")
async def delete_ingredient(id: int = Path(..., gt=0)):
    deleted = db.delete_ingredient(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return {"message": "Ingredient deleted successfully"}

# Recipe Ingredients endpoints
@router.get("/recipes/{id}/ingredients")
async def get_recipe_ingredients(id: int = Path(..., gt=0)):
    recipe = db.get_recipe_by_id(id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return {"ingredients": db.get_recipe_ingredients(id)}

@router.post("/recipes/{id}/ingredients")
async def add_recipe_ingredient(id: int = Path(..., gt=0), ingredient_data = Body(...)):
    recipe = db.get_recipe_by_id(id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db.add_ingredient_to_recipe(id, ingredient_data)

@router.put("/recipes/{id}/ingredients/{ingredient_id}")
async def update_recipe_ingredient(
    id: int = Path(..., gt=0),
    ingredient_id: int = Path(..., gt=0),
    update_data = Body(...)
):
    updated = db.update_recipe_ingredient(id, ingredient_id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Recipe or ingredient not found")
    return {"message": "Recipe ingredient updated successfully"}

@router.delete("/recipes/{id}/ingredients/{ingredient_id}")
async def remove_recipe_ingredient(
    id: int = Path(..., gt=0),
    ingredient_id: int = Path(..., gt=0)
):
    deleted = db.remove_ingredient_from_recipe(id, ingredient_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Recipe or ingredient not found")
    return {"message": "Ingredient removed from recipe successfully"}

# Categories endpoints
@router.get("/categories")
async def get_categories():
    return {"categories": db.get_all_categories()}

@router.get("/categories/{id}")
async def get_category(id: int = Path(..., gt=0)):
    category = db.get_category_by_id(id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.post("/categories")
async def create_category(category_data = Body(...)):
    return db.create_category(category_data)

@router.put("/categories/{id}")
async def update_category(id: int = Path(..., gt=0), category_data = Body(...)):
    updated = db.update_category(id, category_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category updated successfully"}

@router.delete("/categories/{id}")
async def delete_category(id: int = Path(..., gt=0)):
    deleted = db.delete_category(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted successfully"}

# Food Items endpoints
@router.get("/food-items")
async def get_food_items():
    return {"food_items": db.get_all_food_items()}

@router.get("/food-items/{id}")
async def get_food_item(id: int = Path(..., gt=0)):
    food_item = db.get_food_item_by_id(id)
    if food_item is None:
        raise HTTPException(status_code=404, detail="Food item not found")
    return food_item

@router.post("/food-items")
async def create_food_item(food_item_data = Body(...)):
    return db.create_food_item(food_item_data)

@router.put("/food-items/{id}")
async def update_food_item(id: int = Path(..., gt=0), food_item_data = Body(...)):
    updated = db.update_food_item(id, food_item_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Food item not found")
    return {"message": "Food item updated successfully"}

@router.delete("/food-items/{id}")
async def delete_food_item(id: int = Path(..., gt=0)):
    deleted = db.delete_food_item(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Food item not found")
    return {"message": "Food item deleted successfully"}

# Meals endpoints
@router.get("/meals")
async def get_meals():
    return {"meals": db.get_all_meals()}

@router.get("/meals/{id}")
async def get_meal(id: int = Path(..., gt=0)):
    meal = db.get_meal_by_id(id)
    if meal is None:
        raise HTTPException(status_code=404, detail="Meal not found")
    return meal

@router.post("/meals")
async def create_meal(meal_data = Body(...)):
    return db.create_meal(meal_data)

@router.put("/meals/{id}")
async def update_meal(id: int = Path(..., gt=0), meal_data = Body(...)):
    updated = db.update_meal(id, meal_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Meal not found")
    return {"message": "Meal updated successfully"}

@router.delete("/meals/{id}")
async def delete_meal(id: int = Path(..., gt=0)):
    deleted = db.delete_meal(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Meal not found")
    return {"message": "Meal deleted successfully"}

# Utility endpoints
@router.get("/recipes/search")
async def search_recipes(
    q: str = Query(..., description="Search query", min_length=1, max_length=100)
):
    return {"results": db.search_recipes(q)}

@router.get("/recipes/category/{category_id}")
async def get_recipes_by_category(category_id: int = Path(..., gt=0)):
    return {"recipes": db.get_recipes_by_category(category_id)}
