
from flask import Flask, jsonify, request
from flask_restful import Resource, Api



app = Flask(__name__)

# Get the connection info ready for MySQL
db_user = 'webapp'
# this is not the most secure way of handling software secrets.  It will be fine 
# for our purposes because you'll be stopping the docker containers when not in use.
# But, don't do this in production. 
db_pw = open('/secrets/db_password.txt').readline()

@app.route("/")
def hello_world():
    return "<h1>Hello, From A Flask App!!!!!!!</h1>"

if __name__== "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)