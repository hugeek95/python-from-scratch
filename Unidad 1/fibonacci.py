def fibonacci(n):
    if n <= 0:
        return "La posición debe ser mayor que 0"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

# Programa principal
posicion = int(input("Ingrese la posición de la serie Fibonacci: "))
print(f"El número en la posición {posicion} es: {fibonacci(posicion)}")
