from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import Inventory, User

inventory_routes = Blueprint('inventory', __name__)

# GET all inventory.

@inventory_routes.route('/')
@login_required
def get_inventory():
  """
  Query for all inventory and returns them in a list
  """
  get_inventory = Inventory.query.all()
  return {'inventory': [inventory.to_dict() for inventory in get_inventory]}
