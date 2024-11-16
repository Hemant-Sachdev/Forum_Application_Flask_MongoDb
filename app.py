from flask import Flask, render_template, redirect, session
from functools import wraps
import pymongo
app = Flask(__name__)
app.secret_key = 'add_your_unique_key_here'
# Database
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system

#Decorators
def login_require(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session : 
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap

# Routes
from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')
