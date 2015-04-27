import os
from flask import Flask
from flask.ext import restful
from flask.ext.restful import reqparse, Api
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.httpauth import HTTPBasicAuth


app = Flask(__name__, static_url_path='')
app.config.from_object('config')


db = SQLAlchemy(app)

api = restful.Api(app)

flask_bcrypt = Bcrypt(app)

auth = HTTPBasicAuth()


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

import views.views
from app.routes import index

