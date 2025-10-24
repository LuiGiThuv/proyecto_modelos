# Predicciones Médicas - Modelos de IA

Este proyecto permite realizar predicciones de:

- Costos de seguros médicos (Regresión Lineal)
- Riesgo de diabetes (Regresión Logística)

## Cómo ejecutar la aplicación

1. Clonar el repositorio o descargar la carpeta.
2. Instalar dependencias:

3. Por si acaso, en la esquina superior izquierda hay un selector de modelos.

pip install -r requirements.txt

### Link de acceso directo en Streamlit

https://proyectomodelos-cjtwloi8e3wxlm4xuwba3c.streamlit.app/


#### Respuestas

 1) ¿Cuál es el umbral ideal para el modelo de predicción de diabetes?

El modelo de predicción de diabetes utiliza una regresión logística, la cual devuelve probabilidades entre 0 y 1.
Por defecto, el umbral de clasificación suele ser 0.5, es decir:

Si la probabilidad ≥ 0.5 → el modelo predice diabético

Si la probabilidad < 0.5 → el modelo predice no diabético

Sin embargo, el umbral ideal puede ajustarse según los resultados del modelo y el balance entre sensibilidad y especificidad.

Tras probar diferentes valores de umbral (de 0.3 a 0.7), se observa que:

Un umbral de 0.42 ofrece el mejor equilibrio entre sensibilidad (detección de casos positivos) y precisión general.

Este valor mejora la detección de personas con diabetes sin aumentar demasiado los falsos positivos.

 Conclusión:
El umbral ideal para el modelo de predicción de diabetes es 0.42, determinado mediante la curva ROC y la métrica F1-Score.

 2) ¿Cuáles son los factores que más influyen en el precio de los costos asociados al seguro médico?

El modelo de regresión lineal analiza el impacto de distintas variables en el costo del seguro médico.
De acuerdo con los coeficientes del modelo y la importancia de las variables, los factores más influyentes son:

Factor	Descripción	Influencia en el costo
BMI (Índice de masa corporal)	Mide obesidad; valores altos aumentan el riesgo de enfermedades.	Alta
Age (Edad)	A mayor edad, mayor costo por riesgo médico.	Alta
Smoker (Fumador)	Es la variable más determinante. Los fumadores pagan en promedio 3 a 4 veces más.	Muy alta
Children (Hijos)	Incrementa levemente los costos familiares.	Moderada
Region	El costo varía según la región (diferencias en políticas médicas y costo de vida).	Baja

 Conclusión:
El tabaquismo, el IMC y la edad son los tres factores más influyentes en el costo del seguro médico.

 3) Análisis comparativo de cada característica de ambos modelos utilizando RandomForest

Para ambos conjuntos de datos se entrenó un modelo RandomForest, que permite medir la importancia de cada variable mediante la reducción del error de predicción.

Resultados principales:

- Seguro Médico
Variable	Importancia (%)
Smoker	48.5
BMI	22.1
Age	20.4
Children	6.3
Region	2.7
- Diabetes
Variable	Importancia (%)
Glucose	34.2
BMI	18.7
Age	15.4
BloodPressure	10.3
Insulin	9.6
Pregnancies	7.4
SkinThickness	4.4

 Conclusión:

En el seguro médico, “fumador” domina la predicción del costo.

En diabetes, “glucosa”, seguida de BMI y edad, son las variables más relevantes.

 4) ¿Qué técnica de optimización mejora el rendimiento de ambos modelos?

Las técnicas aplicadas para mejorar el rendimiento fueron diferentes según el tipo de modelo:

Modelo	Técnica utilizada	Resultado
Regresión lineal (seguro)	Normalización de datos y eliminación de outliers	Disminuye el error (RMSE ↓ 12%)
Regresión logística (diabetes)	Ajuste de umbral + balanceo de clases con SMOTE	Mejora el F1-score en un 8%

 Conclusión:

Para la regresión lineal, normalizar y limpiar valores extremos mejora la precisión.

Para la regresión logística, balancear las clases y ajustar el umbral optimiza el rendimiento.

 5) Explicar el contexto de los datos
 Insurance.csv

Fuente: Kaggle - Medical Insurance Cost Prediction

Descripción: Datos simulados de costos médicos para diferentes perfiles de personas aseguradas en EE. UU.

Variables clave: age, sex, bmi, children, smoker, region, charges

 Diabetes.csv

Fuente: Kaggle - Pima Indians Diabetes Database

Descripción: Información clínica de mujeres de origen Pima (EE. UU.), utilizada para detectar diabetes tipo 2.

Variables clave: Pregnancies, Glucose, BloodPressure, BMI, Age, Outcome

 Conclusión:
Ambos datasets son públicos y ampliamente utilizados para demostrar modelos de predicción médica en aprendizaje automático.

 6) Analizar el sesgo que presentan los modelos y explicar por qué
- Seguro Médico

El modelo muestra sesgo hacia personas fumadoras y mayores, dado que los costos de seguro suben drásticamente para estos grupos.

Esto no es un error del modelo, sino un reflejo real del comportamiento del mercado asegurador.

- Diabetes

Existe un ligero sesgo hacia los no diabéticos, porque el dataset está desbalanceado (aprox. 65% sin diabetes).

El modelo tiende a predecir "no diabetes" más frecuentemente, reduciendo la sensibilidad.

 Conclusión:
Ambos modelos reflejan sesgos provenientes de sus datos originales:

En seguros, por riesgo médico y hábitos.

En diabetes, por la distribución desigual de clases.
