import streamlit as st
import joblib

# Load model
model = joblib.load('heart_disease_model.pkl')

st.title("Heart Disease Prediction")

# Collect user input
age = st.number_input("Age")
sex = st.selectbox("Sex (0=Female, 1=Male)", [0,1])
# Add all remaining 11 features similarly
# For example:
cp = st.number_input("Chest Pain Type (0-3)")
trestbps = st.number_input("Resting Blood Pressure")
# ... collect all 13 features

features = [age, sex, cp, trestbps, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]  # replace values with inputs

if st.button("Predict"):
    prediction = model.predict([features])
    if prediction[0] == 1:
        st.error("Prediction: Heart Disease")
    else:
        st.success("Prediction: No Heart Disease")
