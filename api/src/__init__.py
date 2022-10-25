from flask import Flask
from flaskext.mysql import MySQL

db = MySQL()

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'
    app.config['MYSQL_DATABASE_USER'] = 'webapp'
    app.config['MYSQL_DATABASE_PASSWORD'] = open('/secrets/db_password.txt').readline()
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'classicmodels'

    db.init_app(app)


    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app