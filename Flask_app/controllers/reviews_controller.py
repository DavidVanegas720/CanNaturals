from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template, redirect,session, request, jsonify
from flask_app import app