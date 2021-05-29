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
    "dion": generate_password_hash("password"),
    "node1": generate_password_hash("passwordnode1")
}
### authentication ###
@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username
@app.route('/')
@auth.login_required
def index():
    return "User, {} Sucsessfully authenticated".format(auth.current_user())
### authentication ###



### Api resources


class systemdata(Resource):
    @app.route('/systemdata')
    @auth.login_required
    def get(self):
        total, used, free = shutil.disk_usage("/")
        hdd = free//(2**30)
        payload = json.dumps({'system-name': socket.gethostname(), 'cpu': psutil.cpu_percent(), 'mem': psutil.virtual_memory().percent, 'disk': hdd })
        return payload

### Api resources
api.add_resource(systemdata, '/systemdata') # Route_1
### Api resources

### Main entrypoint
app.run(port='5002')