# Import flask dependencies
from flask import Blueprint
from ..tasks.tasks import add


# Import the database object from the main app module
# from app import db

# Define the blueprint: 'ui'
mod_ui = Blueprint('ui', __name__, url_prefix='/')


# Set the route and accepted methods
@mod_ui.route('/', methods=['GET'])
def home():
    result = add.delay(1, 1)
    return "Hello World {}".format(result.wait())
    return "Hello World {}"
