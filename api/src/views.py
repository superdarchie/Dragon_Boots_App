from flask import Blueprint, request, jsonify, make_response
import json
import pymysql.cursors

from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    cursor = db.get_db().cursor()
    cursor.execute('select customerNumber, customerName from customers')
    theData = cursor.fetchall()

    return jsonify(theData)
    # return ('<h1>Hello from your web app!!</h1>')


@views.route('/test')
def tester():
    return "<h1>this is a test!</h1>"