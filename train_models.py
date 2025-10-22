import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# === MODELO DE COSTO DE SEGURO MÉDICO ===
data_ins = pd.read_csv("insurance.csv")

le = LabelEncoder()
data_ins["sex"] = le.fit_transform(data_ins["sex"])
data_ins["smoker"] = le.fit_transform(data_ins["smoker"])
data_ins["region"] = le.fit_transform(data_ins["region"])

X_ins = data_ins.drop("charges", axis=1)
y_ins = data_ins["charges"]

model_ins = LinearRegression()
model_ins.fit(X_ins, y_ins)

pickle.dump(model_ins, open("models/modelo_seguro.pkl", "wb"))

print("✅ Modelo de seguro médico guardado correctamente.")


# === MODELO DE DIABETES ===
data_dia = pd.read_csv("diabetes.csv")

X_dia = data_dia.drop("Outcome", axis=1)
y_dia = data_dia["Outcome"]

scaler = StandardScaler()
X_dia_scaled = scaler.fit_transform(X_dia)

model_dia = LogisticRegression(max_iter=1000)
model_dia.fit(X_dia_scaled, y_dia)

# Guardar modelo y scaler
pickle.dump(model_dia, open("models/modelo_diabetes.pkl", "wb"))
pickle.dump(scaler, open("models/escalador_diabetes.pkl", "wb"))

print("✅ Modelo de diabetes guardado correctamente.")

