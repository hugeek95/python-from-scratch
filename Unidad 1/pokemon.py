print("=== Batalla Pokémon ===")

# Puntos de vida iniciales
vida_jugador = 50
vida_enemigo = 50

# Elección de Pokémon
print("Elige tu Pokémon:")
print("1. Charmander 🔥")
print("2. Squirtle 💧")

opcion = int(input("Opción: "))

if opcion == 1:
    pokemon = "Charmander"
elif opcion == 2:
    pokemon = "Squirtle"
else:
    pokemon = "Pikachu ⚡ (se eligió por defecto)"

print(f"\n¡Has elegido a {pokemon}!")
print("El enemigo es Bulbasaur 🌱\n")

# Ciclo de batalla
while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{pokemon} HP: {vida_jugador} | Bulbasaur HP: {vida_enemigo}")
    print("\n¿Qué ataque quieres usar?")
    print("1. Ataque rápido (daño 5)")
    print("2. Ataque especial (daño 10, pero fallas 1 de cada 3 veces)")

    ataque = int(input("Opción: "))

    if ataque == 1:
        print(f"{pokemon} usa Ataque rápido ⚡")
        vida_enemigo -= 5
    elif ataque == 2:
        import random
        if random.randint(1, 3) == 1:
            print(f"{pokemon} intentó el ataque especial, ¡pero falló!")
        else:
            print(f"{pokemon} usa Ataque especial 💥")
            vida_enemigo -= 10
    else:
        print("¡Opción inválida, pierdes el turno!")

    # Turno del enemigo
    if vida_enemigo > 0:
        print("Bulbasaur contraataca con Látigo Cepa 🌿 (-7 HP)")
        vida_jugador -= 7

# Resultado final
if vida_jugador <= 0 and vida_enemigo <= 0:
    print("\n¡Empate! Ambos Pokémon cayeron al mismo tiempo 😵")
elif vida_jugador <= 0:
    print(f"\n{pokemon} ha sido derrotado... ¡Perdiste! 💀")
else:
    print(f"\n¡Bulbasaur ha caído! {pokemon} gana la batalla 🎉")
