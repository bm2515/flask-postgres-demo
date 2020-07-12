from flask import Flask, redirect, url_for, render_template, request, jsonify, abort, Response, json
from flask_api import status
from flask_inputs import Inputs
from cerberus import Validator
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import time
import json
from models import User, Fitness
from database import db_session
from schema import user_schema, fitness_schema
from input_validation import post_input_validation, get_input_validation

#A Flask REST API Demo which records and retrieves user's daily fitness information
#How to Use Flask REST API:
#Step 1: Register a new user with the system by going to http://0.0.0.0:5000/register and entering user general information
#Step 2: Add Fitness Data by going to http://0.0.0.0:5000/users/username/add and entering user fitness information
#Step 3: Retrieve All User Fitness records by going to http://0.0.0.0:5000/users/username/data


#Initialization of Flask app
app = Flask(__name__)


#API End Point to Register a new user to the System
@app.route("/users/register", methods=["POST"])
def add_user():

    validation_response = post_input_validation(request, user_schema)

    if validation_response != True:
        return validation_response
   
    #All validation checks have been passed

    #Get JSON POST Body
    requestdata = request.get_json()

    #Retrieve newly entered User Information 
    username = requestdata["username"]
    firstname = requestdata["firstname"]
    lastname = requestdata["lastname"]
    age = requestdata["age"]
    sex = requestdata["sex"]
    height = requestdata["height"]
    weight = requestdata["weight"]
    diabetes = requestdata["diabetes"]

    #Create a user instance and add it to the DataBase
    user = User(username, firstname, lastname, age, sex, height, weight, diabetes)
    db_session.add(user)
    db_session.commit()

    return jsonify(requestdata)


#API END Point to add new user Fitness information to the databse
@app.route("/users/<usr>/add", methods=["POST"])
def add_user_data(usr):
    
    validation_response = post_input_validation(request, fitness_schema, username=usr)

    if validation_response != True:
        return validation_response

    #Get POST Request BODY
    requestdata = request.get_json()

    #Retrieve newly entered user's fitness information
    steps = requestdata['steps']
    calories = requestdata['calories']

    #Retrieve user instance from the DataBase
    user = User.query.filter_by(username=usr).first()

    userid = user.id
    
    #Create a User Fitness Instance and add it to the DataBase
    fitnessdata = Fitness(steps, calories, userid)
    db_session.add(fitnessdata)
    db_session.commit()

    return jsonify(requestdata)
                

#API End Point to retrieve User's all fitness data
@app.route("/users/<usr>/data", methods=["GET"])
def get_user_data(usr):

    OUTPUT = []

    #Validate Username Exists In The DataBase

    validation_response = get_input_validation(usr)

    if validation_response != True:
        return validation_response

    #All Validations are complete

    user = User.query.filter_by(username=usr).first()


    #Retrieve all user Fitness Records
    userdata = Fitness.query.filter_by(userid=user.id).all()
    
    #Append each fitness record to the OUTPUT
    for user in userdata:

        #Create an instance of fitness record to be displayed
        data = {
                "steps": user.steps,
                "calories": user.calories,
                "datecreated": user.datecreated
        }

        OUTPUT.append(data)

    return jsonify(OUTPUT)

    

#API End Point to Display User Credentials
@app.route("/users/<usr>", methods=["GET"])
def get_user (usr):

    #Validate Username Exists In The DataBase

    validation_response = get_input_validation(usr)

    if validation_response != True:
        return validation_response

    user = User.query.filter_by(username=usr).first()

    #Retrieve all user information
    firstname = user.firstname
    lastname = user.lastname
    age = user.age
    sex = user.sex
    height = user.height
    weight = user.weight
    diabetes = user.diabetes
    datecreated = user.datecreated

    #Return User Information to the User
    return jsonify({"firstname": firstname,
            "lastname": lastname,
            "age": age,
            "sex": sex,
            "height": height,
            "weight": weight,
            "diabetes": diabetes,
            "datecreated": datecreated
            })

    
    
#RUN THE APP
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')