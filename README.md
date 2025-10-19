# Heart Disease Prediction App

A **web application** that predicts the likelihood of a patient having **heart disease** using a Logistic Regression machine learning model. Built with **Python** and **Streamlit**, users can input 13 health parameters and get predictions instantly.

---

## Features
- Predicts heart disease risk based on 13 medical attributes:
  - Age
  - Sex
  - Chest Pain Type
  - Resting Blood Pressure
  - Serum Cholesterol
  - Fasting Blood Sugar
  - Resting ECG
  - Maximum Heart Rate Achieved
  - Exercise Induced Angina
  - ST Depression
  - Slope of Peak Exercise ST Segment
  - Number of Major Vessels Colored by Fluoroscopy
  - Thalassemia
- Interactive and easy-to-use web interface
- Quick predictions for healthcare awareness

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Lahari-4306/HeartDisease-Detection.git
```
2.Go to the Project Folder
```bash
cd HeartDisease-Detection
```
3.Install required libraries:
```bash
pip install -r requirements.txt
```

## Run the app:
```bash
streamlit run app.py
```
## Dependencies

- streamlit
- numpy
- pandas
- scikit-learn
- joblib

## Repository Contents

- app.py — Streamlit web app code
- heart_disease_model.pkl — Trained Logistic Regression model
- requirements.txt — Python dependencies
## Author
- Lahari Puppala
- laharipuppala6@gmail.com
