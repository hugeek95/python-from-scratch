import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Cargar dataset
cancer = load_breast_cancer()

# Crear DataFrame
df = pd.DataFrame(
    cancer.data,
    columns=cancer.feature_names
)

df["target"] = cancer.target

print("Primeros registros:")
print(df.head())

print("\nInformación general:")
print(df.info())

print("\nDistribución de clases:")
print(df["target"].value_counts())

# Variables predictoras
X = cancer.data

# Variable objetivo
y = cancer.target

# División entrenamiento-prueba
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)

# Crear modelo
modelo = KNeighborsClassifier(n_neighbors=5)

# Entrenar modelo
modelo.fit(X_train, y_train)

# Predicciones
y_pred = modelo.predict(X_test)

# Métricas
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:")
print(accuracy)

print("\nMatriz de Confusión:")
print(confusion_matrix(y_test, y_pred))

print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred))

import matplotlib.pyplot as plt

df["target"].value_counts().plot(kind="bar")

plt.title("Distribución de Clases")
plt.xlabel("Clase")
plt.ylabel("Cantidad")

plt.show()