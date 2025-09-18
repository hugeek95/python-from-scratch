local = "Soy global"

def funcion():
    local = "Soy local"
    print(local)

def otra_funcion():
    print(local)  # Error: no existe

funcion()
#print(local)  # Error: no existe fuera
