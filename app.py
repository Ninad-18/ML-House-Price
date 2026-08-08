import streamlit as st
from model_utils import predict_price


# Page configuration
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)


# Title
st.title("🏠 House Price Predictor")

st.write(
    "Enter the details of the house to predict its estimated price."
)


# Input fields
st.subheader("House Details")

square_feet = st.number_input(
    "Square Feet",
    min_value=100.0,
    max_value=10000.0,
    value=1000.0,
    step=50.0
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

distance_to_city = st.number_input(
    "Distance to City (km)",
    min_value=0.0,
    max_value=200.0,
    value=10.0,
    step=1.0
)


# Prediction button
if st.button("Predict House Price"):

    prediction = predict_price(
        square_feet,
        num_rooms,
        age,
        distance_to_city
    )

    st.success("Prediction completed!")

    st.metric(
        label="Estimated House Price",
        value=f"₹{prediction:,.2f}"
    )