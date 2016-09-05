from flask import Flask
from flask_bootstrap import Bootstrap
from flask_heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)

Bootstrap(app=app)

from app import views
from app import api
