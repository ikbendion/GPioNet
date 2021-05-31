import RPi.GPIO as GPIO
from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

### setup ###
auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)
GPIO.setmode(GPIO.BOARD)

### users, Yes. this SHOULD NOT be hardcoded into the code. will fix this before production use :-)
users = {
    "user": generate_password_hash("password"),
}
### authentication
@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username



### Api endpoints
class setpin(Resource):
    @app.route('/setpin') ## app route indication
    @auth.login_required ### require authentication
    def post(self):
        pin = request.args.get('pin')
        state = request.args.get('state')
        print("pin >> "+str(pin)+'\n'+"State >> "+str(state))
        try:
            print("ok")
            # PI code #
            pin_state = "GPIO."+state
            GPIO.output(pin, pin_state)
        except:
            return 400
        return 200

class getpin(Resource):
    @app.route('/getpin') ## app route indication
    @auth.login_required ### require authentication
    def get():
        pin = request.args.get('pin')
        # pi code #
        GPIO.setup(pin, GPIO.OUT)
        state = GPIO.input(int(pin))
        payload = str(pin)+' = '+str(state)
        return payload

### Api resources
api.add_resource(setpin, '/setpin') # Change pin status
api.add_resource(getpin, '/getpin') # read the state of a pin 

### Main entrypoint
app.run(port='5002',host='10.0.1.169')
