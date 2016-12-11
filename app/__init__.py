from flask import *
from models import db, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/flaskapi"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.config.from_object('config') #tells flask to read & use the config file

from app import routes

'''If you are wondering why the import statement is at the end and not at the beginning of the script as it is always done, the reason is to avoid circular references, because you are going to see that the routes module needs to import the app variable defined in this script. Putting the import at the end avoids the circular import error.'''
