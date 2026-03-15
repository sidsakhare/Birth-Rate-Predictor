from flask import Flask, jsonify , request, render_template
import pandas as pd
import pickle
from flask_restx import Api, Resource, fields 
from routes import home, predict, user

from extensions import cache


app = Flask(__name__)

app.config['CACHE_TYPE'] = 'SimpleCache'
app.config['CACHE_DEFAULT_TIMEOUT'] = 300

cache.init_app(app)

 
api = Api(app, title="Flask API Documentation", doc="/docs", prefix="/api")


pred_ns = api.namespace("prediction", description ="This is prediction model", path = "/predict")


input_model = pred_ns.model("PredictionInput",{
                        "gestation":fields.List(fields.Float, required=True),
                        "parity":fields.List(fields.Integer, required=True),
                        "age":fields.List(fields.Float, required=True),
                        "height":fields.List(fields.Float, required=True),
                        "weight":fields.List(fields.Float, required=True),
                        "smoke": fields.List(fields.Float, required=True)
                        })

@pred_ns.route("/")
class Prediction(Resource):
    @pred_ns.expect(input_model)
    def post(self):
        '''Predicts the baby's birth weight based on input parameters.

                **Request Body Format:**
                - `gestation` (List[int]): Number of gestation days
                - `parity` (List[int]): Parity value
                - `age` (List[int]): Mother's age
                - `height` (List[int]): Mother's height
                -`weight` (List[int]): Mother's bwt
                - `smoke` (List[int]): Smoking status (0 or 1)

                **Returns:**
                - JSON response containing predicted outcome as a float.'''
        
        baby_data =   request.get_json()
        Expected_Coloumns = ['gestation', 'parity', 'age', 'height', 'weight','smoke']
        # baby_data_cleaned = get_cleaned_data(baby_data)

        baby_df = pd.DataFrame(baby_data)
        baby_df = baby_df[Expected_Coloumns]

        with open("model.pkl", "rb") as file:
            model = pickle.load(file)

        prediction = model.predict(baby_df)


        prediction = round(float(prediction[0]),2)

        return {'prediction': prediction}
    
    app.register_blueprint(user.user_bp)
    app.register_blueprint(predict.predict_bp)
    app.register_blueprint(home.home_bp)





if __name__ == "__main__":
     app.run(debug=True)




# @app.route("/", methods = ["GET"])
# def home():
#     return render_template("index.html")


# Expected_Coloumns = ['bwt', 'gestation', 'parity', 'age', 'height', 'smoke']


# def get_cleaned_data(baby_data):
#     bwt = float(baby_data["bwt"])
#     gestation = float(baby_data["gestation"])
#     parity = float(baby_data["parity"])
#     age = float(baby_data["age"])
#     height = float(baby_data["height"])
#     smoke =float(baby_data["smoke"])

#     cleaned_data = { "bwt":[bwt],
#                     "gestation" :[gestation],
#                     "parity":[parity],
#                     "age":[age],
#                     "height":[height],
#                     "smoke":[smoke]}
#     return cleaned_data

# with open("model.pkl", "rb") as file:
#         model = pickle.load(file)
# @app.route("/predict", methods = ["post"])
# def get_prediction():
#     baby_data =   request.get_json()

#     # baby_data_cleaned = get_cleaned_data(baby_data)

#     baby_df = pd.DataFrame([baby_data])
#     baby_df = baby_df[Expected_Coloumns]

#     with open("model.pkl", "rb") as file:
#         model = pickle.load(file)

#     prediction = model.predict(baby_df)

#     prediction = round(float(prediction[0]),2)

#     # return render_template("index.html", prediction = prediction)
#     return {'Response':prediction }

# @app.route('/get_user', methods = ['GET'])
# def get_user():
#      return 'This is the get user request'

# @app.route('/add_user', methods = ['POST'])
# def add_user():
#      return 'This is the add user request'

# @app.route('/get_user', methods = ['PUT'])
# def update_user():
#      return 'This is the update user request'

# @app.route('/delete_user', methods = ['GET'])
# def delete_user():
#      return 'This is the delete user request'