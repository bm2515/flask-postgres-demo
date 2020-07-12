#Define Schema for user general information

user_schema = {'username': {'type': 'string', 'required': True}, 
'firstname': {'type': 'string', 'required': True},
'lastname': {'type': 'string', 'required': True},
'age': {'type': 'string', 'required': True},
'sex': {'type': 'string', 'required': True},
'height': {'type': 'string', 'required': True},
'weight': {'type': 'string', 'required': True}, 
'diabetes': {'type': 'string', 'required': True}}


#Define Schema for User Fitness Information
fitness_schema = {'steps': {'type': 'string', 'required': True}, 
'calories': {'type': 'string', 'required': True}}