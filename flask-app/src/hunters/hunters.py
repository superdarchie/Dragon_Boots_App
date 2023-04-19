from flask import Blueprint, request, jsonify, make_response, current_app
import json, flask
from src import db

hunters = Blueprint('hunters', __name__)


@hunters.route('/addHunter', methods=['POST'])
def add_new_hunter():
    #gets data  from json
    the_data = request.json
    current_app.logger.info(the_data)
    try:
        h_id = the_data['h_id']
        h_id_number = the_data['id_numb']  # encapsulate in try/catch
        h_hp = the_data['h_hp']
        h_damage = the_data['h_damage']
        h_speed = the_data['h_speed']
        h_defense = the_data['h_defense']


        query = "insert into Hunters (h_id, id_number, hp, damage, speed, defense) values "
        query += f'({h_id},{h_id_number}, {h_hp}, {h_damage},{h_speed},{h_defense})'
        current_app.logger.info(query)
        #pushes info to terminal in docker when "shit" happens 

        cursor = db.get_db().cursor()
        cursor.execute(query)
        #execute the query
        db.get_db().commit()
    except:
        return "ERROR! HUNTER COULD NOT BE ADDED! HUNTER MAY ALREADY BE ADDED"
     
    return "Success!"

@hunters.route('/deleteHunter', methods=['DELETE'])
def delete_hunter():
    the_data = request.json
    h_hunterID = the_data['h_id']
    cursor = db.get_db().cursor()
    try:
        cursor.execute(f'delete from Hunters where h_id = {h_hunterID}')
        db.get_db().commit()
    except:
        return "ERROR: YOU CANNOT DELETE THIS HUNTER! TO IMPORTANT"
    return "Hunter deleated!"

@hunters.route('/hunterInfo', methods =['GET'])
def get_hunter_info():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT * FROM Hunters')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    
    return jsonify(json_data)

@hunters.route('/allDragonsNames', methods=['GET'])
def get_all_dragon_name():
    cursor = db.get_db().cursor()
   
    # use cursor to query the database for a list of products
    try:
        cursor.execute('SELECT name FROM Dragons')
    except:
        return "ERROR! DRAGONS DNE"
    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    
    return jsonify(json_data)

@hunters.route('/dragonInfo', methods=['GET'])
def get_dragon_info():
    the_data = request.json #different from theDATA -> this is what the user gives to find the dragons info in the DB
    h_dragonName = the_data['name']
    
    cursor = db.get_db().cursor()
    # use cursor to query the database for a list of products
    try:
        cursor.execute(f'SELECT * FROM Dragons WHERE name = "{h_dragonName}" ')
    except:
        return "EROR: No Dragon Found WITH NAME!!"
    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall() #actually info of dragon

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    
    return jsonify(json_data)

@hunters.route('/hunterUpdate/<hunterID>', methods=['PUT'])
def updateStats(hunterID):
    the_data = request.json 
    current_app.logger.info(the_data)
    cursor = db.get_db().cursor()

    hp = the_data['hp']
    defense = the_data['defense']
    damage = the_data['damage']
    speed = the_data['speed']
    
    query = f'update Hunters set hp = {hp}, defense ={defense}, damage = {damage}, speed ={speed} WHERE h_id = {hunterID} '
    
    try:
        cursor.execute(query)
        db.get_db().commit()
    except:
        return "EROR: UNABLE TO UPDATE HUNTER"
   
    return "SUCESS! HUNTER UPDATED"

@hunters.route('/quests', methods = ['GET'])
def returnQuest():
    #get a cursor object from the database
    cursor = db.get_db().cursor()

    query = 'SELECT * FROM Quests'
    try:
        cursor.execute(query)
    except:
        return "ERROR! No QUESTS"
    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    
    return jsonify(json_data)


@hunters.route('/tools', methods = ['GET'])
def returnTools():
    #get a cursor object from the database
    cursor = db.get_db().cursor()

    query = 'SELECT * FROM Tools'
    try:
        cursor.execute(query)
    except:
        return "ERROR! No TOOLS"
    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    
    return jsonify(json_data)