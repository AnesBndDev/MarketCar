from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
#from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
mar = Marshmallow(app)
bcrypt = Bcrypt(app)
from market import routes
