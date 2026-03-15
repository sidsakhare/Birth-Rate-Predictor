from flask import Flask, jsonify , request, render_template
import pandas as pd
import pickle
from flask import Blueprint
from extensions import cache

predict_bp =Blueprint('predict', __name__)
Expected_Coloumns = ['gestation', 'parity', 'age', 'height','weight', 'smoke']
def get_cleaned_data(baby_data):
    gestation = float(baby_data["gestation"])
    parity = float(baby_data["parity"])
    age = float(baby_data["age"])
    height = float(baby_data["height"])
    weight = float(baby_data["weight"])
    smoke =float(baby_data["smoke"])

    cleaned_data = {
                    "gestation" :[gestation],
                    "parity":[parity],
                    "age":[age],
                    "height":[height],
                    "weight":[weight],
                    "smoke":[smoke]}
    return cleaned_data

with open("model.pkl", "rb") as file:
        model = pickle.load(file)
@predict_bp.route("/predict", methods = ["post"])
@cache.cached(timeout=5, query_string=True)
def get_prediction():
    baby_data =   request.form

    baby_data_cleaned = get_cleaned_data(baby_data)

    baby_df = pd.DataFrame(baby_data_cleaned)
    #baby_df = baby_df[baby_data_cleaned]

    with open("model.pkl", "rb") as file:
        model = pickle.load(file)

    prediction = model.predict(baby_df)

    prediction = round(float(prediction[0]),2)

    return render_template("index.html", prediction = prediction)
    # return {'Response':prediction }