import psycopg2
from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
import json
from datetime import datetime
import psutil
import socket
import shutil
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
### setup ###
auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)
### setup ###

### users ###
users = {
    "user": generate_password_hash("password"),
}
### authentication ###
@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username
### authentication ###



### Api resources


class systemdata(Resource):
    @app.route('/systemdata') ## app route indication
    @auth.login_required ### require authentication
    def get():
        payload = 'ok'
        return payload

### Api resources
api.add_resource(systemdata, '/systemdata') # Route_1
### Api resources

### Main entrypoint
app.run(port='5002')