# Guardar
nombres = ["Ana", "Luis", "Pedro"]
with open("nombres.txt", "w") as f:
    for nombre in nombres:
        f.write(nombre + "\n")

# Leer
with open("nombres.txt", "r") as f:
    for linea in f:
        print("Nombre:", linea.strip())
