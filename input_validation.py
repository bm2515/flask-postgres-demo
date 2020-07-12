from flask import Flask, Response
from models import User
from cerberus import Validator

def post_input_validation(request, schema, username=None):
    
    #Validate POST Request Body is NON-EMPTY
    if (request.data):

        #Validate Content-Type for POST Request Body 
        if request.headers['Content-Type'] == 'application/json':

            #Get JSON POST Body
            requestdata = request.get_json()

            #Create an instance, v to validate data entry and type with user_schema
            v = Validator(schema)

            if v.validate(requestdata):

                if username != None:

                    user = User.query.filter_by(username=username).first()

                    if (user != None):

                        return True
                    
                    else:

                        return Response("{'message':'Username entered in URL is not registered with the system. Please proceed to http://0.0.0.0:5000/users/register to add new user'}", status=404)

                return True

            else:
                return Response("{'message':'Incorrect Data Field/Type Entry in the system. Please review User Schema'}", status=403)

        else:
            return Response("{'message':'Incorrect Content Type for post body request. Please enter data in JSON format'}", status=403)

    else:
        return Response("{'message':'Empty POST Request Body. Please review User Schema and enter data in JSON format'}", status=400)  


def get_input_validation(username):

    user = User.query.filter_by(username=username).first()

    if (user != None):

        return True
    
    else:

        return Response("{'message':'Username entered in URL is not registered with the system. Please proceed to http://0.0.0.0:5000/users/register to add new user'}", status=404)
