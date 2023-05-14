from flask import Flask, request, render_template
import sqlite3
from sqlite3 import Error


# Flask constructor
app = Flask(__name__)



@app.route('/')
def yes():
   return render_template('index.html')
if __name__ == 'main':
   app.run()

@app.route('/contact')
def feed():
    return render_template('contact.html')


@app.route('/ides')
def search():
    return render_template('ides.html')

@app.route('/languages')
def post():
    return render_template('languages.html')

@app.route('/stacks')
def profile():
    return render_template('stacks.html')


@app.route('/index')
def home():
    return render_template('index.html')

