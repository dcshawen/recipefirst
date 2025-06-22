from flask import Blueprint, current_app
from flask_cors import CORS, cross_origin
from . import db

bp = Blueprint('main', __name__)

@cross_origin()
@bp.route('/ingredients', methods=['GET'])
def getIngredients():
    return db.getIngredients()

@cross_origin()
@bp.route('/ingredients/<int:ingredient_id>', methods=['GET'])
def getIngredient(ingredient_id):
    return db.getIngredient(ingredient_id)

@cross_origin()
@bp.route('/units', methods=['GET'])
def getUnits():
    return db.getUnits()

@cross_origin()
@bp.route('/units/<int:unit_id>', methods=['GET'])
def getUnit(unit_id):
    return db.getUnit(unit_id)

@cross_origin()
@bp.route('/components', methods=['GET'])
def getComponents():
    return db.getComponents()

@cross_origin()
@bp.route('/components/<int:component_id>', methods=['GET'])
def getComponent(component_id):
    return db.getComponent(component_id)

@cross_origin()
@bp.route('/recipes', methods=['GET'])
def getRecipes():
    return db.getRecipes()

@cross_origin()
@bp.route('/recipes/<int:recipe_id>', methods=['GET'])
def getRecipe(recipe_id):
    return db.getRecipe(recipe_id)

@cross_origin()
@bp.route('/meals', methods=['GET'])
def getMeals():
    return db.getMeals()

@cross_origin()
@bp.route('/meals/<int:meal_id>', methods=['GET'])
def getMeal(meal_id):
    return db.getMeal(meal_id)

@cross_origin()
@bp.route('/recipecomponents', methods=['GET'])
def getRecipeComponents():
    return db.getRecipeComponents()

@cross_origin()
@bp.route('/recipecomponents/<int:recipe_id>/<int:component_id>', methods=['GET'])
def getRecipeComponent(recipe_id, component_id):
    return db.getRecipeComponent(recipe_id, component_id)

@cross_origin()
@bp.route('/componentingredients', methods=['GET'])
def getComponentIngredients():
    return db.getComponentIngredients()

@cross_origin()
@bp.route('/componentingredients/<int:component_id>/<int:ingredient_id>', methods=['GET'])
def getComponentIngredient(component_id, ingredient_id):
    return db.getComponentIngredient(component_id, ingredient_id)

@cross_origin()
@bp.route('/mealcomponents', methods=['GET'])
def getMealComponents():
    return db.getMealComponents()

@cross_origin()
@bp.route('/mealcomponents/<int:meal_id>/<int:component_id>', methods=['GET'])
def getMealComponent(meal_id, component_id):
    return db.getMealComponent(meal_id, component_id)

@cross_origin()
@bp.route('/pantries', methods=['GET'])
def getPantries():
    return db.getPantries()

@cross_origin()
@bp.route('/pantries/<int:pantry_id>', methods=['GET'])
def getPantry(pantry_id):
    return db.getPantry(pantry_id)

@cross_origin()
@bp.route('/pantrycomponents', methods=['GET'])
def getPantryComponents():
    return db.getPantryComponents()

@cross_origin()
@bp.route('/pantrycomponents/<int:pantry_id>/<int:component_id>', methods=['GET'])
def getPantryComponent(pantry_id, component_id):
    return db.getPantryComponent(pantry_id, component_id)

@cross_origin()
@bp.route('/nutritions', methods=['GET'])
def getNutritions():
    return db.getNutritions()

@cross_origin()
@bp.route('/nutritions/<int:nutrition_id>', methods=['GET'])
def getNutrition(nutrition_id):
    return db.getNutrition(nutrition_id)

@cross_origin()
@bp.route('/nutritioningredients', methods=['GET'])
def getNutritionIngredients():
    return db.getNutritionIngredients()

@cross_origin()
@bp.route('/nutritioningredients/<int:ni_id>', methods=['GET'])
def getNutritionIngredient(ni_id):
    return db.getNutritionIngredient(ni_id)

@cross_origin()
@bp.route('/nutritionfields', methods=['GET'])
def getNutritionFields():
    return db.getNutritionFields()

@cross_origin()
@bp.route('/nutritionfields/<int:nutritionfield_id>', methods=['GET'])
def getNutritionField(nutritionfield_id):
    return db.getNutritionField(nutritionfield_id)