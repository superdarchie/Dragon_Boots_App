from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


wizards = Blueprint('wizards', __name__)

@wizards.route('/wizard', methods=['POST'])
def add_new_wizard():
    the_data = request.json
    current_app.logger.info(the_data)
    try:
        w_id = the_data['id_numb']  # encapsulate in try/catch
        w_name = the_data['w_name']
        w_crystal = the_data['crystal_ball_number']
        w_gold = the_data['gold_vault_number']

        query = "insert into Wizards (id_numb, name, crystal_ball_number, gold_vault_number) values "
        query += f'({w_id}, "{w_name}", "{w_crystal}", "{w_gold}")'
        current_app.logger.info(query)

        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
    except:
        return "Unable to create the new wizard."
    return "Succesfully created the new wizard."
    

# Get all wizards from the DB
@wizards.route('/wizards', methods=['GET'])
def get_customers():
    cursor = db.get_db().cursor()
    cursor.execute('select * from Wizards')
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
def get_wizard(userID):
    cursor = db.get_db().cursor()
    cursor.execute(f'select * from Wizards where id_numb = {userID}')
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
def delete_wizard(userID):
    cursor = db.get_db().cursor()
    try:
        cursor.execute(f'delete from Wizards where id_numb = {userID}')
    except:
        return "Wizard does not exist."
    db.get_db().commit()
    return 'Wizard successfully deleted from the db.'

@wizards.route('/wizards/<userID>', methods=['PUT'])
def update_wizard(userID):
    the_data = request.json
    current_app.logger.info(the_data)
    cursor = db.get_db().cursor()

    w_address = the_data['address']
    w_realm = the_data['realm']
    query = f'update Wizards set address = "{w_address}", realm = "{w_realm}" where id_numb = {userID}'

    try:
        cursor.execute(query)
        db.get_db().commit()
    except:
        return "Unable to update the supplied wizard."
    
    return 'Wizard successfully updated in the db'

@wizards.route('/orders/<userID>', methods=['GET'])
def get_wizard_orders(userID):
    cursor = db.get_db().cursor()
    try:
        cursor.execute(f'select * from Orders where wizard_id = {userID}')
    except:
        return "Wizard does not exist."
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@wizards.route('/boots', methods=['GET'])
def get_boots():
    cursor = db.get_db().cursor()
    cursor.execute(f'select * from Boots')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
    
@wizards.route('/orders', methods=['POST'])
def add_new_boot_order():
    the_data = request.json
    current_app.logger.info(the_data)

    o_order = the_data['order_number']
    o_boot = the_data['boot_id']
    o_forge = the_data['forge_id']
    o_quant = the_data['quantity']
    o_price = the_data['unit_price']

    query = "insert into Boot_Orders values "
    query += f'({o_order}, {o_boot}, {o_forge}, {o_quant}, {o_price})'
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    # try:
    cursor.execute(query)
    db.get_db().commit()
    # except:
    # return "Unable to process the boot order."
    return "Successfully added the boot order"