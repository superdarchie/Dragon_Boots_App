from flask import Blueprint, request, jsonify, make_response, current_app
import json, flask
from src import db

hunters = Blueprint('hunters', __name__)

#Returns the list of hunter and what quest they are on
@hunters.route('/addHunter/<id_number>', methods=['POST'])
def add_new_hunter(id_number):
    #gets data  from json
    the_data = request.json
    cursor = db.get_db().cursor()
    #extra data -> go to app smith to get the name of the variables
    #Hunters Table Info
    h_hp = the_data['h_hp']
    h_damage = the_data['h_damage']
    h_speed = the_data['speed']
    h_defense = the_data['defense']


    the_Hunters_query = "insert into Hunters (id_number, hp, damage, speed, defense) "
    the_Hunters_query += "values ('" + id_number +  "','" + h_hp +  "', '" + h_damage + "', " + h_speed + ", '" + h_defense + "')"

    current_app.loger.info(the_Hunters_query)
    #pushes info to terminal in docker when "shit" happens 
    try:
        cursor.exectue(the_Hunters_query)
         #execute the query
        db.get_db().commit()
    except:
        return "ERROR! HUNTER COULD NOT BE ADDED"
     
    return "Success!"

@hunters.route('/deleteHunter', methods=['DELETE'])
def delete_hunter():
    the_data = request.json
    h_hunterID = the_data['h_id']
    cursor = db.get_db().cursor()
    db.get_db().commit()
    try:
        cursor.execute('delete from Hunters where h_id = hunter_ID')
    except:
        return "ERROR: THERES NO HUNTER TO DELETE!"
    return "Hunter deleated!"

@hunters.route('/hunterInfo', methods =['GET'])
def get_hunter_info():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT h_id, id_numb, hp, damage, speed, defense, quest_id, quest_date FROM Hunters')

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

@hunters.route('/AllDragonsNames', methods=['GET'])
def get_all_dragon_name():
    cursor = db.get_db().cursor()
   
    # use cursor to query the database for a list of products
    try:
        cursor.execute('SELECT name FROM Dragons')
    except:
        return "ERROR! DRAGON DNE"
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

@hunters.route('/DragonInfo', methods=['GET'])
def get_dragon_info():
    the_data = request.json #different from theDATA -> this is what the user gives to find the dragons info in the DB
    h_dragonName = the_data['name']
    
    cursor = db.get_db().cursor()
    # use cursor to query the database for a list of products
    try:
        cursor.execute('SELECT * FROM Dragons WHERE name = h_dragonName ')
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

@hunters.route('/hunter/<hunterID>', methods=['PUT'])
def updateStats(hunterID):
    the_data = request.json 
    hp = the_data['hp']
    defense = the_data['defense']
    attack = the_data['attack']
    speed = the_data['speed']
    
    query = f'update Hunters set hp = {hp}, defense ={defense}, attack = {attack}, speed ={speed} WHERE h_id = {hunterID} '
    cursor = db.get_db().cursor()
    try:
        cursor.execute(query)
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