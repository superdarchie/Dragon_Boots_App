from flask import Blueprint, request, jsonify, make_response
import json
from src import db


wizards = Blueprint('wizards', __name__)

# Get all wizards from the DB
@wizards.route('/wizards', methods=['GET'])
def get_customers():
    cursor = db.get_db().cursor()
    cursor.execute('select id_numb, name, crystall_ball_number,\
        address, realm, gold_vault_number from Wizards')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get customer detail for wizard with particular userID
@wizards.route('/wizards/<userID>', methods=['GET'])
def get_customer(userID):
    cursor = db.get_db().cursor()
    cursor.execute(f'select * from Wizards where id = {userID}')
    # cursor.execute('select * from customers where id = {0}'.format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@wizards.route('/wizards/<userID>', methods=['DELETE'])
def delete_customer(userID):
    return 'Hello'