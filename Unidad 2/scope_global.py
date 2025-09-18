mensaje = "Soy global"

def mostrar():
    print(mensaje)  # Puede acceder a la variable global

def cambiar():
    global mensaje  # Indica que usaremos la variable global
    mensaje = "He cambiado la variable global"

cambiar()
mostrar()
print(mensaje)  # También fuera de la función
