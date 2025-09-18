# Abrir el archivo en modo lectura ("r")
archivo = open("datos.txt", "r", encoding="utf-8")
print(archivo.read())
archivo.close()

"""
with open("datos.txt", "r", encoding="utf-8") as archivo:
    # Leer todas las líneas
    for linea in archivo:
        # strip() elimina saltos de línea y espacios extra
        print(linea.strip())
"""