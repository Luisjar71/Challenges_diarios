import random

# Opciones posibles
opciones = ["Piedra", "Papel", "Tijera"]

# Función para dar las opciones al usuario, leer y validar la elección
def obtener_eleccion_usuario():
    # Opciones para el usuario
    print("\nElige una opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")

    # Elección de parte del usuario
    eleccion = input("Introduce el número de tu elección: ")

    # Validación de la elección
    while eleccion not in ["1", "2", "3"]:
        print("Opción no válida. Intenta de nuevo.")
        eleccion = input("Introduce el número de tu elección: ")
    return opciones[int(eleccion) - 1] #Restamos 1 de este número entero para obtener el índice correcto en la lista opciones

# Función para elección aleatoria de la máquina
def obtener_eleccion_maquina():
    return random.choice(opciones)

# Función para definir el ganador
def determinar_ganador(usuario, maquina):

    # En caso de que la elección del usuario y la máquina sean iguales es empate
    if usuario == maquina:
        return "Empate"
     
     # Si se dan algunas de las pciones señaladas abajo, gana el usuario, si no gana la máquina
    elif (usuario == "Piedra" and maquina == "Tijera") or \
         (usuario == "Papel" and maquina == "Piedra") or \
         (usuario == "Tijera" and maquina == "Papel"):
        return "¡Ganaste!"
    else:
        return "Perdiste"

# Función de ejecución del juego
def jugar():
    victorias_usuario = 0
    victorias_maquina = 0

    # Toma la elección de ambos jugadores, las imprime y las compara, el primero que llega a 2 gana
    while victorias_usuario < 2 and victorias_maquina < 2:
        usuario = obtener_eleccion_usuario()
        maquina = obtener_eleccion_maquina()
        print(f"\nTu elección: {usuario}")
        print(f"Elección de la máquina: {maquina}")
        resultado = determinar_ganador(usuario, maquina)
        print(resultado)

        if resultado == "¡Ganaste!":
            victorias_usuario += 1
        elif resultado == "Perdiste":
            victorias_maquina += 1

        print("\nResultados hasta ahora:")
        print(f"Victorias del usuario: {victorias_usuario}")
        print(f"Victorias de la máquina: {victorias_maquina}")

    if victorias_usuario == 2:
        print("\n¡Felicidades! Ganaste el juego al mejor de 3.")
    else:
        print("\nLo siento, la máquina ganó el juego al mejor de 3.")


jugar()
