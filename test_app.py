from app import app

def test_hello_route_success():
    tester = app.test_client()
    response = tester.get("/hello")

    assert response.status_code == 200

# def test_hello_route_fail():
#     tester = app.test_client()
#     response = tester.get("/Hello")

#     assert response.status_code == 500


# def test_predict_route_success():
#     tester = app.test_client()
#     data = {
#         "bwt":179,
#         "gestation":279,
#         "parity":1,
#         "age":25,
#         "height":190,
#         "smoke":1
#     }
#     response = tester.post("/predict", json = data)

#     assert  response.status_code == 200


def test_predict_route_invalid_data():
    tester = app.test_client()
    data = {
         "bwt":10,
         "gestation":279,
         "parity":1,
         
    }
    response = tester.post("/predict", json = data)

    assert  response.status_code == 500

def test_predict_route_failed_route():
     tester = app.test_client()
     data = {
        "bwt":179,
         "gestation":279,
         "parity":1,
         "age":25,
         "height":190,
         "smoke":1
     }
     response = tester.post("/0predict", json = data)

     assert  response.status_code == 404

def test_predict_route_failed_method():
     tester = app.test_client()
     data = {
        "bwt":179,
         "gestation":279,
         "parity":1,
         "age":25,
         "height":190,
         "smoke":1
     }
     response = tester.get("/predict", json = data)

     assert  response.status_code == 405