import streamlit as st
import joblib
import os

# Get current folder path
current_dir = os.path.dirname(__file__)

# Create full model path
model_path = os.path.join(current_dir, "salary_model.pkl")

# Load model
model = joblib.load(model_path)

st.title("Salary Prediction App")

experience = st.number_input(
    "Enter Years of Experience",
    min_value=0.0,
    step=0.1
)

if st.button("Predict Salary"):

    prediction = model.predict([[experience]])

    st.success(
        f"Predicted Salary: {prediction[0]:.2f}"
    )