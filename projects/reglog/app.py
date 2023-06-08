from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()

app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
# initialize the app with the extension
db.init_app(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)

with app.app_context():
    db.create_all()


@app.get('/homepage')
def homepage():
    return "This is the homepage!"

@app.get('/test')
def test():
    return "This is a test"

@app.post('/register')
def register():
    email = request.json.get('email')
    password = request.json.get('password')
    
    new_user = User(email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return {"message":"User registration successful!"}

@app.post('/login')
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    # Query the User table 
    # and filter it by email where the email in the 
    # database is same as the email passed by the user from the client
    # get us the first match
    user = User.query.filter_by(email=email).first()
    if user:
        if user.password == password:
            return {'message':'Login successful', 'data':{'email':user.email}}, 200
        else:
            return {'message':'Invalid password'}, 401
    return {'message':'Invalid email'}, 401

@app.patch('/reset-password')
def reset_password():
    email = request.json.get('email')
    new_password = request.json.get('new_password')
    old_password = request.json.get('old_password')

    for user in database:
        if user.get('email') == email:
            if user.get('password') == old_password:
                user['password'] = new_password
                return {'message':'password changed successfully', 'data':user}, 200
            else:
                return {'message':'Invalid old password'}, 401
    return {'message':'Invalid email'}, 401

@app.put('/profile')
def update_profile():
    email = request.json.get('email')
    password = request.json.get('password')
    name = request.json.get('name')
    age = request.json.get('age')

    for user in database:
        if user.get('email') == email:
            if user.get('password') == password:
                user['name'] = name
                user['age'] = age
                return {'message':'Profile updated successfully', 'data':user}, 200
            else:
                return {'message':'Invalid old password'}, 401
    return {'message':'Invalid email'}, 401

@app.delete('/user/<int:index>')
def delete_user(index):
    if len(database) and len(database) >= index:
        database.pop(index)
        return {'message':'User with index {} deleted successfully!'.format(index)}, 200
    return {'message':'There is no user with index {}'.format(index)}, 404