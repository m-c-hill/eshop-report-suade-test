from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eshop.db'
db = SQLAlchemy(app)

from eshopreport import routes
from eshopreport import generate_data
from eshopreport import models


'''
If the reset_database flag is set to true, the generate_data.main() function is called, which removes all data from the
database and reimports it from the csv files in eshopreport/data. 

This is a testing feature and will be replaced in the production release with a more secure form of data entry.
'''
reset_database = False
if reset_database:
    generate_data.main()