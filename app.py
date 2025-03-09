# app.py (Streamlit frontend)
import streamlit as st
import requests

st.title("Body Performance Prediction")

age = st.number_input("Age", min_value=1, max_value=100, step=1)
gender = st.selectbox("Gender", ["Male", "Female"])
gender = 1 if gender == "Male" else 0
weight_kg = st.number_input("Weight (kg)", min_value=20.0, max_value=200.0)
body_fat = st.number_input("Body Fat (%)", min_value=1.0, max_value=50.0)
diastolic = st.number_input("Diastolic Blood Pressure", min_value=40, max_value=150)
sit_and_bend_forward_cm = st.number_input("Sit & Bend Forward (cm)", min_value=-10.0, max_value=50.0)
sit_ups_counts = st.number_input("Sit-ups Count", min_value=0, max_value=200)
broad_jump_cm = st.number_input("Broad Jump (cm)", min_value=50, max_value=300)

if st.button("Predict"):
    data = {
        "age": age,
        "gender": gender,
        "weight_kg": weight_kg,
        "body_fat": body_fat,
        "diastolic": diastolic,
        "sit_and_bend_forward_cm": sit_and_bend_forward_cm,
        "sit_ups_counts": sit_ups_counts,
        "broad_jump_cm": broad_jump_cm,
    }
    response = requests.post("http://fastapi:8000/predict/", json=data)
    st.write("Prediction:", response.json()["prediction"])
