# Import flask dependencies
from flask import Blueprint
from ..tasks.tasks import add_sync, add_async
from app import db

# Define the blueprint: 'ui'
mod_ui = Blueprint('mod_ui', __name__)

@mod_ui.route('/async/', methods=['GET', 'POST'])
def async():
    add_async.delay(1,2)
    return "async"


@mod_ui.route('/sync/', methods=['GET', 'POST'])
def sync():
    add_sync(1,2)
    return "sync"
