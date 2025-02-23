
import streamlit as st
#from streamlit_lottie import st_lottie
import requests
from pickle import load
import numpy as np


model = load(open("/workspaces/Boosting-algoritmos/models/xgbregressor_42.sav", "rb"))


# Configuración de página
st.set_page_config(page_title="Predicción de Diabetes", page_icon="🏥", layout="wide")

with st.container():
    st.title("🏥 Aplicación de Predicción de Diabetes")
    st.write("Esta aplicación predice si un paciente tiene diabetes en base a medidas diagnósticas.")

with st.container():
    st.subheader("🔍 Ingresa los valores de los siguientes parámetros:")

    col1 = st.columns(1)[0]
    with col1:
        Glucose = st.slider("Glucose: Concentración de glucosa en plasma", 0.0, 200.0, 100.0, 1.0)
        SkinThickness = st.slider("SkinThickness: Grosor del pliegue cutáneo del tríceps", 0.0, 99.0, 20.0, 1.0)
        Age = st.slider("Age: Edad del paciente", 21.0, 81.0, 30.0, 1.0)
        Pregnancies = st.slider("Pregnancies: Número de embarazos", 0.0, 17.0, 1.0, 1.0)
        BloodPressure = st.slider("BloodPressure: Presión arterial diastólica", 0.0, 122.0, 70.0, 1.0)
        Insulin = st.slider("Insulin: Insulina sérica de 2 horas", 0.0, 846.0, 79.0, 1.0)
        BMI = st.slider("BMI: Índice de Masa Corporal", 0.0, 67.0, 25.0, 0.1)
        DiabetesPedigreeFunction = st.slider("DiabetesPedigreeFunction: Función de pedigrí de diabetes", 0.08, 2.42, 0.5, 0.01)

with st.container():
    st.markdown("---")
    if st.button("✨ Predecir Diabetes"):
        input_data = np.array([[Glucose, SkinThickness, Age, Pregnancies, BloodPressure, Insulin, BMI, DiabetesPedigreeFunction]])
        prediction = model.predict(input_data)[0]

        # Mostrar resultado corregido
        st.success(f"🏥 Resultado: {'Sí tiene diabetes' if prediction == 1 else 'No tiene diabetes'}")

st.markdown("---")
