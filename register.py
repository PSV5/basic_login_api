import sqlite3
from datetime import datetime
from flask_restful import reqparse, Resource

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        
        connection.close()
        return user

class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type = str,
        required = True,
        help = "This field cannot be left blank!"
    )
    parser.add_argument(
        'password',
        type = str,
        required = True,
        help = "This field cannot be left blank!"
    )
    def get(self):
        data = UserRegister.parser.parse_args()
        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()
        data = UserRegister.parser.parse_args()
        print(data['username'])
        if User.find_by_username(data['username']):
            return {'message': 'User logged in!'}
        else:
            return {"message": "User doesn't exist."}



class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type = str,
        required = True,
        help = "This field cannot be left blank!"
    )
    parser.add_argument(
        'password',
        type = str,
        required = True,
        help = "This field cannot be left blank!"
    )
    def post(self):
        data = UserRegister.parser.parse_args()
        
        if User.find_by_username(data['username']):
            return {'message': 'A user with that username already exists!'}, 400
        
        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()
        current_date = datetime.now()
        data['date'] = current_date.strftime("%D")
        query = "INSERT INTO users VALUES (?, ?, ?)"
        cursor.execute(query, (data['username'], data['password'], data['date']))
        
        cursor = connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201
