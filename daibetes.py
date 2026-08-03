import pandas as pd

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Cargar dataset desde CSV
df = pd.read_csv("diabetes.csv")

print("Primeros registros:")
print(df.head())

print("\nInformación general:")
print(df.info())

print("\nDistribución de clases:")
print(df["Outcome"].value_counts())

# Variables predictoras
X = df.drop("Outcome", axis=1)

# Variable objetivo
y = df["Outcome"]

# División de datos
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)

# Crear modelo
modelo = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

# Entrenamiento
modelo.fit(X_train, y_train)

# Predicciones
y_pred = modelo.predict(X_test)

# Evaluación
print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))

print("\nMatriz de Confusión:")
print(confusion_matrix(y_test, y_pred))

print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred))