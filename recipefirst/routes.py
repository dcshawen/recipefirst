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