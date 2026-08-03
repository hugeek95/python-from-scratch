calificaciones = []

cantidad = int(input("¿Cuántas calificaciones deseas ingresar?: "))

for i in range(cantidad):
    calificacion = float(input(f"Ingrese la calificación #{i + 1}: "))
    calificaciones.append(calificacion)

promedio = sum(calificaciones) / len(calificaciones)

print("\n===== RESULTADOS =====")
print("Calificaciones:", calificaciones)
print("Promedio:", promedio)
print("Mayor calificación:", max(calificaciones))
print("Menor calificación:", min(calificaciones))

if promedio >= 70:
    print("Estado: Aprobado")
else:
    print("Estado: Reprobado")