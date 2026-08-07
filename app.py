import streamlit as st
import pandas as pd
import joblib as jb

# Load model
model = joblib.load("ridge_house_price_model.pkl")

# Page configuration
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# Title
st.title("🏠 House Price Predictor")
st.write("Enter the house details below to predict its price.")

# Input fields
square_feet = st.number_input(
    "Square Feet",
    min_value=100.0,
    max_value=10000.0,
    value=1000.0,
    step=100.0
)


num_rooms = st.number_input(
    "Number of Rooms",
    min_value=1.0,
    max_value=20.0,
    value=3.0,
    step=1.0
)

age = st.number_input(
    "Age of House (years)",
    min_value=0.0,
    max_value=200.0,
    value=10.0,
    step=1.0
)

distance = st.number_input(
    "Distance to City (km)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.5
)

st.divider()

# Prediction button
if st.button("🔮 Predict House Price", use_container_width=True):
    # Create input DataFrame
    input_data = pd.DataFrame({
        "square_feet": [square_feet],
        "num_rooms": [num_rooms],
        "age": [age],
        "distance_to_city(km)": [distance]
    })

    # Prediction
    prediction = model.predict(input_data)

    predicted_price = prediction[0]

    # Display result
    st.success(
        f"🏠 Predicted House Price: ₹{predicted_price:,.2f}"
    )