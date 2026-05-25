# app.py

import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("salary_model.pkl")

st.title("Salary Prediction App")

# User Input
experience = st.number_input(
    "Enter Years of Experience",
    min_value=0.0,
    step=0.1
)

# Prediction
if st.button("Predict Salary"):

    prediction = model.predict([[experience]])

    st.success(
        f"Predicted Salary: {prediction[0]:.2f}"
    )