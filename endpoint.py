from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
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



### Api endpoints

class setpin(Resource):
    @app.route('/setpin') ## app route indication
    @auth.login_required ### require authentication
    def post(pin,state):
        pin = request.args.get('pin')
        state = request.args.get('state')
        if pin or state is None:
            return 'Missing details!'
        print("Pin number is "+str(pin))
        payload = 'ok'
        return payload

class getpin(Resource):
    @app.route('/getpin') ## app route indication
    @auth.login_required ### require authentication
    def get(pin):
        pin = request.args.get('pin')
        payload = 'ok'
        return payload

### Api endpointss


### Api resources
api.add_resource(setpin, '/setpin') # Change pin status
api.add_resource(getpin, '/getpin') # read the state of a pin 
### Api resources

### Main entrypoint
app.run(port='5002')