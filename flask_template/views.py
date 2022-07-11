from flask import Flask, render_template, Blueprint

my_view = Blueprint('my_view', __name__)

@my_view.route('/')
def index():
    return render_template("index.html")

@my_view.route('/home')
def home():
    return '<h1>This is Chantelle\'s app</h1>'

@my_view.route('/about')
def about():
    return '<h1>About Me</h1>'