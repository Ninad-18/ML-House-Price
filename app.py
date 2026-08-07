import streamlit as st
from model import predict_price

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠"
)

st.title("🏠 House Price Predictor")

st.write("Enter the details of the house:")

square_feet = st.number_input(
    "Square Feet",
    min_value=100.0,
    value=1000.0
)

num_rooms = st.number_input(
    "Number of Rooms",
    min_value=1,
    value=3
)

age = st.number_input(
    "Age of House (years)",
    min_value=0.0,
    value=10.0
)

distance = st.number_input(
    "Distance to City (km)",
    min_value=0.0,
    value=5.0
)

if st.button("Predict Price"):

    price = predict_price(
        square_feet,
        num_rooms,
        age,
        distance
    )

    st.success(f"Predicted House Price: ₹{price:,.2f}")