import random

def juego_con_opciones_aleatorio():
    palabras = {
        "sol": "Brilla en el cielo durante el día y da luz y calor.",
        "lluvia": "Cae del cielo en gotas y moja la tierra.",
        "viento": "No se puede ver, pero se siente cuando sopla."
    }
    
    palabra_correcta = random.choice(list(palabras.keys()))
    pista = palabras[palabra_correcta]
    intentos = 0
    max_intentos = 5
    
    print("¡Bienvenido al juego para salir del bucle!")
    print("Debes adivinar la palabra correcta entre estas opciones: sol, lluvia, viento")
    print("Aquí tienes una pista para ayudarte:")
    print(f"Pregunta: {pista}")
    
    while intentos < max_intentos:
        intento = input("Escribe la palabra correcta para salir del bucle: ").lower()
        intentos += 1
        
        if intento == palabra_correcta:
            print(f"¡Felicidades! Has salido del bucle en {intentos} intento(s).")
            break
        elif intento in palabras:
            print(f"Has elegido '{intento}', pero no es la palabra correcta. Intenta otra vez.")
            print(f"Pista: {pista}")
        else:
            print("Esa palabra no está entre las opciones. Por favor, elige entre sol, lluvia o viento.")
    
    else:
        print("Se te acabaron los intentos. ¡Has quedado atrapado en el bucle!")

juego_con_opciones_aleatorio()
