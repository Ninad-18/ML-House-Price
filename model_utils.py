import joblib
import os
import pandas as pd


MODEL_PATH = os.path.join("model", "ridge_model.pkl")


def load_model():
    return joblib.load(MODEL_PATH)


def predict_price(square_feet, num_rooms, age, distance_to_city):

    model = load_model()

    input_data = pd.DataFrame([{
        "square_feet": square_feet,
        "num_rooms": num_rooms,
        "age": age,
        "distance_to_city(km)": distance_to_city
    }])

    prediction = model.predict(input_data)

    return float(prediction.ravel()[0])