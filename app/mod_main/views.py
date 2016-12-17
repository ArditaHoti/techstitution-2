from flask import Blueprint, render_template, request
from bson import json util, ObjectId

mod_main = Blueprint('main', __name__)

from app import mongo

@mod_main.route('/', methods=['GET', 'Post'])
def index():

    db mongo.db.form_data

    if request.method == 'GET':
        return render_template('techstitution1.html')
    elif request.method == 'POST':
        data = request.form.to_dict()
        db.insert(data)
        # db = mongo.db.arkep.insert(request.form.to_dict())
        return render_template('techstitution1.html')
    else:
        return "Bad Request"
