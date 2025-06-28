from flask import Blueprint, current_app, request, jsonify
from flask_cors import CORS, cross_origin
from . import db

bp = Blueprint('main', __name__)

@cross_origin()
@bp.route('/ingredients', methods=['GET'])
def getIngredients():
    limit = request.args.get('limit', type=int)
    name = request.args.get('name')
    description = request.args.get('description')
    return db.getIngredients(limit=limit, name=name, description=description)

@cross_origin()
@bp.route('/ingredients/<int:ingredient_id>', methods=['GET'])
def getIngredient(ingredient_id):
    return db.getIngredient(ingredient_id)

@cross_origin()
@bp.route('/ingredients', methods=['POST'])
def addIngredient():
    ingredient_id = db.addIngredient(request.get_json())
    return jsonify({"message": "Ingredient added successfully", "ingredient_id": ingredient_id}), 201

@cross_origin()
@bp.route('/units', methods=['GET'])
def getUnits():
    return db.getUnits()

@cross_origin()
@bp.route('/units/<int:unit_id>', methods=['GET'])
def getUnit(unit_id):
    return db.getUnit(unit_id)

@cross_origin()
@bp.route('/units', methods=['POST'])
def addUnit():
    unit_id = db.addUnit(request.get_json())
    return jsonify({"message": "Unit added successfully", "unit_id": unit_id}), 201

@cross_origin()
@bp.route('/components', methods=['GET'])
def getComponents():
    limit = request.args.get('limit', type=int)
    name = request.args.get('name')
    description = request.args.get('description')
    return db.getComponents(limit=limit, name=name, description=description)

@cross_origin()
@bp.route('/components/<int:component_id>', methods=['GET'])
def getComponent(component_id):
    return db.getComponent(component_id)

@cross_origin()
@bp.route('/recipes', methods=['GET'])
def getRecipes():
    limit = request.args.get('limit', type=int)
    name = request.args.get('name')
    description = request.args.get('description')
    return db.getRecipes(limit=limit, name=name, description=description)

@cross_origin()
@bp.route('/recipes/<int:recipe_id>', methods=['GET'])
def getRecipe(recipe_id):
    return db.getRecipe(recipe_id)

@cross_origin()
@bp.route('/meals', methods=['GET'])
def getMeals():
    limit = request.args.get('limit', type=int)
    name = request.args.get('name')
    description = request.args.get('description')
    return db.getMeals(limit=limit, name=name, description=description)

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

@cross_origin()
@bp.route('/recipes', methods=['POST'])
def addRecipe():
    recipe_id = db.addRecipe(request.get_json())
    return jsonify({"message": "Recipe added successfully", "recipe_id": recipe_id}), 201

@cross_origin()
@bp.route('/components', methods=['POST'])
def addComponent():
    component_id = db.addComponent(request.get_json())
    return jsonify({"message": "Component added successfully", "component_id": component_id}), 201

@cross_origin()
@bp.route('/meals', methods=['POST'])
def addMeal():
    meal_id = db.addMeal(request.get_json())
    return jsonify({"message": "Meal added successfully", "meal_id": meal_id}), 201

@cross_origin()
@bp.route('/ingredients/<int:ingredient_id>', methods=['PUT'])
def updateIngredient(ingredient_id):
    db.updateIngredient(ingredient_id, request.get_json())
    return jsonify({"message": "Ingredient updated successfully"})

@cross_origin()
@bp.route('/ingredients/<int:ingredient_id>', methods=['DELETE'])
def deleteIngredient(ingredient_id):
    db.deleteIngredient(ingredient_id)
    return jsonify({"message": "Ingredient deleted successfully"})

@cross_origin()
@bp.route('/recipes/<int:recipe_id>', methods=['PUT'])
def updateRecipe(recipe_id):
    db.updateRecipe(recipe_id, request.get_json())
    return jsonify({"message": "Recipe updated successfully"})

@cross_origin()
@bp.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def deleteRecipe(recipe_id):
    db.deleteRecipe(recipe_id)
    return jsonify({"message": "Recipe deleted successfully"})

@cross_origin()
@bp.route('/components/<int:component_id>', methods=['PUT'])
def updateComponent(component_id):
    db.updateComponent(component_id, request.get_json())
    return jsonify({"message": "Component updated successfully"})

@cross_origin()
@bp.route('/components/<int:component_id>', methods=['DELETE'])
def deleteComponent(component_id):
    db.deleteComponent(component_id)
    return jsonify({"message": "Component deleted successfully"})

@cross_origin()
@bp.route('/meals/<int:meal_id>', methods=['PUT'])
def updateMeal(meal_id):
    db.updateMeal(meal_id, request.get_json())
    return jsonify({"message": "Meal updated successfully"})

@cross_origin()
@bp.route('/meals/<int:meal_id>', methods=['DELETE'])
def deleteMeal(meal_id):
    db.deleteMeal(meal_id)
    return jsonify({"message": "Meal deleted successfully"})

@cross_origin()
@bp.route('/units/<int:unit_id>', methods=['PUT'])
def updateUnit(unit_id):
    db.updateUnit(unit_id, request.get_json())
    return jsonify({"message": "Unit updated successfully"})

@cross_origin()
@bp.route('/units/<int:unit_id>', methods=['DELETE'])
def deleteUnit(unit_id):
    db.deleteUnit(unit_id)
    return jsonify({"message": "Unit deleted successfully"})