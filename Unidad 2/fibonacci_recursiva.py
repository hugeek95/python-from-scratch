# Recursion
def fibonacci(n):
    if n <= 0:
        return "La posición debe ser mayor que 0"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) 
# Programa principal
posicion = int(input("Ingrese la posición de la serie Fibonacci: "))
print(f"El número en la posición {posicion} es: {fibonacci(posicion)}")
