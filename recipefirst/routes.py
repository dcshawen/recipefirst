from flask import Blueprint, current_app
from . import db

bp = Blueprint('main', __name__)

@bp.route('/ingredients', methods=['GET'])
def get_ingredients():
    return db.getIngredients()