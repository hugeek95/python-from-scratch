# Lectura de iris con pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")  # Activa el estilo

df = pd.read_csv('iris.data', header=None)
df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "target"]

print(df.head())
print(df.describe())
print(df['target'].value_counts())

# Gráfico de dispersión
sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="target")
plt.show()

# Pairplot (comparación de todas las variables)
sns.pairplot(df, hue="target")
plt.show()
