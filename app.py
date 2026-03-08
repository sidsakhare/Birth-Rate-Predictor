from flask import Flask, jsonify , request, render_template
import pandas as pd
import pickle
app = Flask(__name__)
def get_cleaned_data(baby_data):
    bwt = float(baby_data["bwt"])
    gestation = float(baby_data["gestation"])
    parity = float(baby_data["parity"])
    age = float(baby_data["age"])
    height = float(baby_data["height"])
    smoke =float(baby_data["smoke"])

    cleaned_data = { "bwt":[bwt],
                    "gestation" :[gestation],
                    "parity":[parity],
                    "age":[age],
                    "height":[height],
                    "smoke":[smoke]}
    return cleaned_data

@app.route("/", methods = ["GET"])
def home():
    return render_template("index.html")
@app.route("/predict", methods = ["post"])
def get_prediction():
    baby_data =   request.form

    baby_data_cleaned = get_cleaned_data(baby_data)

    baby_df = pd.DataFrame(baby_data_cleaned)

    with open("model/model.pkl", "rb") as file:
        model = pickle.load(file)

    prediction = model.predict(baby_df)

    prediction = round(float(prediction[0]),2)

    return render_template("index.html", prediction = prediction)

if __name__ == "__main__":
     app.run(debug=True)

