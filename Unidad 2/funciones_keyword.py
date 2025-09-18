#Keywords argument y return en funciones
def crear_usuario(nombre, ciudad, edad):
    return {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad
    }

usuario = crear_usuario(nombre="Ana", edad=28, ciudad="Madrid")

print(usuario)