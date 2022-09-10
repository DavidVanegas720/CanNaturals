import imp
from Flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template, redirect,session, request, jsonify
from Flask_app import app

from Flask_app.models.users import Users

@app.route('/')
def index():
    return render_template('index.html')