import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

# ===========================
# Cargar modelos entrenados
# ===========================
modelo_seguro = pickle.load(open("models/modelo_seguro.pkl", "rb"))
modelo_diabetes = pickle.load(open("models/modelo_diabetes.pkl", "rb"))

# ===========================
# Configuración de la app
# ===========================
st.set_page_config(page_title="Predicciones de Salud", page_icon="💡", layout="centered")
st.title("🧠 Predicciones de Modelos de Salud")
st.write("Esta aplicación permite realizar dos tipos de predicciones:")
st.write("1️⃣ Costos de seguro médico.")
st.write("2️⃣ Riesgo de diabetes.")
st.markdown("---")

# ===========================
# Menú lateral
# ===========================
opcion = st.sidebar.selectbox(
    "Selecciona el modelo a utilizar:",
    ("Predicción de Seguro Médico", "Predicción de Diabetes")
)

# ===========================
# MODELO 1: SEGURO MÉDICO
# ===========================
if opcion == "Predicción de Seguro Médico":
    st.header("💰 Predicción de Costos de Seguro Médico")

    # Entradas de usuario
    age = st.number_input("Edad", min_value=0, max_value=100, value=30)
    sex = st.selectbox("Sexo", ["Masculino", "Femenino","Otro"])
    bmi = st.number_input("Índice de Masa Corporal (BMI)", min_value=10.0, max_value=50.0, value=25.0)
    children = st.number_input("Número de hijos", min_value=0, max_value=10, value=1)
    smoker = st.selectbox("¿Es usted fumador?", ["si", "no"])
    region = st.selectbox("Región", ["Estados Unidos", "Chile", "Japon", "Israel"])

    # Codificación igual al entrenamiento
    sex = 1 if sex == "Masculino" else 0
    smoker = 1 if smoker == "si" else 0
    region_map = {"Estados Unidos": 0, "Chile": 1, "Japon": 2, "Israel": 3}
    region = region_map[region]

    if st.button("Predecir Costo"):
        entrada = pd.DataFrame([[age, sex, bmi, children, smoker, region]],
                               columns=["age", "sex", "bmi", "children", "smoker", "region"])
        prediccion = modelo_seguro.predict(entrada)[0]
        st.success(f"💵 El costo estimado del seguro médico es: **${prediccion:,.2f} Pesos**")

# ===========================
# MODELO 2: DIABETES
# ===========================
elif opcion == "Predicción de Diabetes":
    st.header("🩺 Predicción de Riesgo de Diabetes")

    Pregnancies = st.number_input("Número de embarazos", min_value=0, max_value=20, value=1)
    Glucose = st.number_input("Nivel de Glucosa", min_value=0, max_value=300, value=100)
    BloodPressure = st.number_input("Presión arterial", min_value=0, max_value=200, value=70)
    SkinThickness = st.number_input("Espesor de piel (mm)", min_value=0, max_value=100, value=20)
    Insulin = st.number_input("Nivel de insulina", min_value=0, max_value=900, value=80)
    BMI = st.number_input("Índice de masa corporal (BMI)", min_value=0.0, max_value=70.0, value=25.0)
    DiabetesPedigreeFunction = st.number_input("Función de Pedigrí de Diabetes", min_value=0.0, max_value=3.0, value=0.5)
    Age = st.number_input("Edad", min_value=0, max_value=120, value=30)

    if st.button("Predecir Riesgo"):
        entrada = pd.DataFrame([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]],
                               columns=["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"])
        scaler = pickle.load(open("models/escalador_diabetes.pkl", "rb"))
        entrada = scaler.transform(entrada)

        prediccion = modelo_diabetes.predict(entrada)[0]
        prob = modelo_diabetes.predict_proba(entrada)[0][1]

        if prediccion == 1:
            st.error(f"⚠️ Posible riesgo de diabetes. Probabilidad: {prob*100:.2f}%")
        else:
            st.success(f"✅ Bajo riesgo de diabetes. Probabilidad: {prob*100:.2f}%")

# ===========================
# Footer
# ===========================
st.markdown("---")
st.caption("Desarrollado por Luis Gipoulou © 2025")
