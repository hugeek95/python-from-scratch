# Diccionarios. Clave-Valor 
persona = {"nombre": "Ana", "edad": 30}
persona["edad"] = 31  # Modificar el valor asociado a la clave 'edad'
print(f"Persona: {persona['edad']}")

if "ana" == persona["nombre"]:
    print(f"Hola Ana")
else:
    print("No eres Ana")