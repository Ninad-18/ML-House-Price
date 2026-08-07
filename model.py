import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge

# Load dataset
df = pd.read_csv("house_price.csv")

# Features
X = df[
    [
        "square_feet",
        "num_rooms",
        "age",
        "distance_to_city(km)"
    ]
]

# Target
y = df["price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create and train model
model = Ridge()

model.fit(X_train, y_train)


def predict_price(square_feet, num_rooms, age, distance):
    input_data = pd.DataFrame({
        "square_feet": [square_feet],
        "num_rooms": [num_rooms],
        "age": [age],
        "distance_to_city(km)": [distance]
    })

    prediction = model.predict(input_data)

    return prediction[0]