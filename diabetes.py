import os
import kagglehub
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Descargar automáticamente el dataset desde Kaggle
path = kagglehub.dataset_download(
    "uciml/pima-indians-diabetes-database"
)

print("Dataset descargado en:", path)

# Localizar el archivo CSV
csv_path = os.path.join(path, "diabetes.csv")

# Leer dataset
df = pd.read_csv(csv_path)

print("\nPrimeros registros:")
print(df.head())

print("\nInformación general:")
print(df.info())

print("\nDistribución de clases:")
print(df["Outcome"].value_counts())

# Variables predictoras
X = df.drop("Outcome", axis=1)

# Variable objetivo
y = df["Outcome"]

# División entrenamiento/prueba
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)

# Modelo
modelo = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

modelo.fit(X_train, y_train)

# Predicciones
y_pred = modelo.predict(X_test)

# Métricas
print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))

print("\nMatriz de Confusión:")
print(confusion_matrix(y_test, y_pred))

print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred))

import matplotlib.pyplot as plt

importancias = pd.Series(
    modelo.feature_importances_,
    index=X.columns
)

importancias.sort_values().plot(kind="barh")

plt.title("Importancia de Variables")
plt.xlabel("Importancia")
plt.show()