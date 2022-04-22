from flask import Flask, jsonify, request, render_template 
from flask_restful import Api
from register import UserRegister, UserLogin

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'abcd'
api = Api(app)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


api.add_resource(UserRegister, '/register_new')
api.add_resource(UserLogin, '/login')



if __name__ == '__main__':
    app.run(debug=True)