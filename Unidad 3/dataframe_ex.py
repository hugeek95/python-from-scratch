import pandas as pd

datos = {
    "Nombre": ["Ana", "Luis", "María"],
    "Edad": [23, 30, 35],
    "Ciudad": ["CDMX", "Monterrey", "Guadalajara"]
}

df = pd.DataFrame(datos)
print(df)
