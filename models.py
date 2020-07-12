from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import DateTime
from datetime import datetime
from sqlalchemy.orm import relationship



#Defining our first DataBase Table which records basic health information of the user
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)

    username = Column(String(20), unique=True, nullable=False)
    firstname = Column(String(50))
    lastname = Column(String(50))
    age = Column(String(50))
    sex = Column(String(50))
    height = Column(String(50))
    weight = Column(String(50))
    diabetes = Column(String(50))
    datecreated = Column(DateTime, default= datetime.now)
    
    fitness = relationship('Fitness', backref= 'user', lazy = True)

    #Defining User Table Initilization Function
    def __init__(self, username, firstname, lastname, age, sex, height, weight, diabetes):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.diabetes = diabetes


#Defining our first DataBase Table which records daily fitness information of the user
class Fitness(Base):
    __tablename__ = 'fitness'

    id = Column(Integer, primary_key = True)

    steps = Column(String(50))
    calories = Column(String(50))
    datecreated = Column(DateTime, default= datetime.now)

    userid = Column(Integer, ForeignKey('user.id'), nullable=False)
    
    #Defining Fitness Table Initilization Function
    def __init__(self, steps, calories, userid):

        self.steps = steps
        self.calories = calories
        self.userid = userid
