# 🏠 House Price Prediction

A Machine Learning project that predicts house prices based on property-related features using **Ridge Regression** and provides an interactive web interface using **Streamlit**.

## 📌 Project Overview

The goal of this project is to predict the price of a house using features such as:

* Square Feet
* Number of Rooms
* Age of the House
* Distance from City

Several regression algorithms were trained and evaluated, and **Ridge Regression** was selected as the final model based on its performance on the test dataset.

## 🧠 Machine Learning Models Tested

The following regression algorithms were evaluated:

* Linear Regression
* Lasso Regression
* Ridge Regression
* ElasticNet Regression
* Random Forest Regressor
* Extra Trees Regressor
* AdaBoost Regressor
* Gradient Boosting Regressor
* XGBoost Regressor
* CatBoost Regressor
* SGD Regressor

### 🏆 Selected Model

**Ridge Regression** was selected as the final model because it achieved the best overall performance among the tested models based primarily on **MAE**.

The approximate results were:

| Model                |           MAE |           MSE |
| -------------------- | ------------: | ------------: |
| Linear Regression    |     15,596.12 |   386,443,817 |
| Lasso Regression     |     15,596.06 |   386,443,453 |
| **Ridge Regression** | **15,595.83** |   386,445,864 |
| ElasticNet           |     30,289.69 | 1,444,245,287 |
| Random Forest        |     18,013.93 |   508,887,992 |
| Extra Trees          |     17,862.80 |   500,782,303 |
| AdaBoost             |     24,256.94 |   929,132,751 |
| Gradient Boosting    |     16,628.49 |   436,777,367 |
| XGBoost              |     16,935.03 |   455,901,789 |
| CatBoost             |     16,182.47 |   415,408,632 |
| SGD                  |     15,603.22 |   386,475,054 |

## 📊 Evaluation Metrics

### MAE — Mean Absolute Error

Measures the average absolute difference between actual and predicted house prices.

**Lower MAE = Better model**

### MSE — Mean Squared Error

Measures the average squared difference between actual and predicted values.

**Lower MSE = Better model**

For this project, Ridge Regression provided the lowest MAE among the evaluated models.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Plotly
* Joblib
* Streamlit
* Jupyter Notebook

## 📂 Project Structure

```text
House-Price-Prediction/
│
├── app.py
├── model.py
├── ridge_model.pkl
├── house_price.ipynb
├── requirements.txt
└── README.md
```

### `house_price.ipynb`

Contains:

* Data loading
* Exploratory Data Analysis
* Data preprocessing
* Train-test split
* Model training
* Model comparison
* Evaluation
* Saving the final Ridge model

### `model.py`

Contains the code responsible for loading the trained model and making predictions.

### `app.py`

Contains the Streamlit user interface.

### `ridge_model.pkl`

Serialized Ridge Regression model created using Joblib.

## 🚀 Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/Ninad-18/ML-House-Price
cd ML-HOUSE PRICE
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🖥️ Streamlit Application

The application allows the user to enter:

```text
Square Feet
Number of Rooms
Age
Distance to City
```

and generates the predicted house price using the trained Ridge Regression model.

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Train Multiple Regression Models
   ↓
Evaluate Models
   ↓
Select Best Model
   ↓
Save Model using Joblib
   ↓
Streamlit UI
   ↓
House Price Prediction
```

## 📈 Future Improvements

* Add feature scaling and preprocessing using a Pipeline
* Improve model hyperparameter tuning
* Add additional house-related features
* Add prediction confidence/range
* Improve Streamlit UI
* Deploy the application online
* Add visualizations to the Streamlit dashboard

## 👨‍💻 Author

**Ninad Patil**

## 📄 License

This project is licensed under the MIT License.
