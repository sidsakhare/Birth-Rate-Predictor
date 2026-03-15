
from flask import Flask, jsonify , request, render_template
import pandas as pd
import pickle
from flask_restx import Api, Resource, fields 
from routes import home, predict, user


from flask import Blueprint

home_bp = Blueprint('home', __name__)



@home_bp.route("/", methods = ["GET"])
def home():
    return render_template("index.html")
