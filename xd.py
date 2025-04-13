
import time 
import random
from termcolor import colored, cprint
import sys

# Parámetros fijos de la simulación
comida = 200
tamaño_grilla = 250
obstaculos = 100
hormigas = 20

# Variables globales (se reiniciarán por simulación en 'simulador')
comida_encontrada = 0
pasos_globales = []   # Acumularemos aquí el total de pasos (celdas amarillas) de cada simulación
grilla_final = []     # Guardamos la última grilla de la simulación (para contar sus celdas amarillas)

estado_a_color = {
    0: 'red',    # Hormigas
    1: 'green',  # Celda libre
    2: 'black',  # Obstáculo
    3: 'white',  # Comida
    4: 'yellow'  # Celda recorrida
}

def printer(grilla):
    """Imprime la grilla coloreada (no es parte de la lógica de conteo)."""
    estado_a_color_local = {
        0: 'red',
        1: 'green',
        2: 'black',
        3: 'white',
        4: 'yellow',
    }
    for fila in grilla:
        fila_str = ""
        for celda in fila:
            fila_str += colored("▓▓", estado_a_color_local[celda])
        print(fila_str)
    return grilla

def matrix(size, hormigas, obstaculos, comida):
    """Crea una grilla de 'size x size' inicializando todas las celdas en 1, y luego llama a edit_grilla."""
    grilla = []
    for i in range(size):
        fila = [1] * size
        grilla.append(fila)
    edit_grilla(grilla, hormigas, obstaculos, comida)

def edit_grilla(grilla, hormigas, obstaculos, comida):
    """Coloca hormigas, obstáculos y comida en la grilla; luego ejecuta los movimientos hasta que se consuma la mitad de la comida."""
    global comida_encontrada, grilla_final
    # Guardamos la cantidad original de comida para la condición de parada
    comida_inicial = comida
    posiciones_iniciales = []
    
    # Colocación de hormigas (valor 0)
    while hormigas > 0:
        x = random.randint(0, len(grilla) - 1)
        y = random.randint(0, len(grilla) - 1)
        grilla[x][y] = 0
        hormigas -= 1
        posiciones_iniciales.append([x, y])
    
    # Colocación de obstáculos (valor 2) en celdas libres
    obstaculos_restantes = obstaculos
    while obstaculos_restantes > 0:
        x = random.randint(0, len(grilla) - 1)
        y = random.randint(0, len(grilla) - 1)
        if grilla[x][y] == 1:
            grilla[x][y] = 2
            obstaculos_restantes -= 1
    
    # Colocación de comida (valor 3) en celdas libres
    comidalocal = comida
    while comidalocal > 0:
        x = random.randint(0, len(grilla) - 1)
        y = random.randint(0, len(grilla) - 1)
        if grilla[x][y] == 1:
            grilla[x][y] = 3
            comidalocal -= 1

    # Ejecutamos el movimiento de hormigas hasta que se consuma la mitad de la comida
    # (La variable 'exit' se define en movedor_de_hormigas)
    exit = False
    while not exit:
        nuevas_posiciones, exit, grilla = movedor_de_hormigas(grilla, posiciones_iniciales, comida_inicial)
        posiciones_iniciales = nuevas_posiciones
    
    # Al terminar la simulación, guardamos la grilla final
    grilla_final = grilla
    # Se cuenta la cantidad de celdas amarillas (pasos) una sola vez al final
    total_pasos = contador_de_pasos(grilla_final)
    pasos_globales.append(total_pasos)

def movedor_de_hormigas(grilla, posiciones_iniciales, comida_inicial):
    """
    Mueve a cada hormiga en una dirección aleatoria.
    Retorna (posiciones_finales, exit_flag, grilla_actualizada).
    El flag 'exit_flag' se pone en True cuando se ha encontrado al menos la mitad de la comida.
    """
    global comida_encontrada
    posiciones_finales = []
    # Para cada hormiga en posiciones_iniciales:
    for posicion in posiciones_iniciales:
        movimiento_exitoso = False
        reintentos = 0
        max_reintentos = 10
        while not movimiento_exitoso and reintentos < max_reintentos:
            reintentos += 1
            valor_aleatorio = random.choice(["x", "y"])
            if valor_aleatorio == "x":
                direccion = random.choice(["arriba", "abajo"])
                if direccion == "abajo":
                    if (posicion[0] + 1 < len(grilla) and grilla[posicion[0] + 1][posicion[1]] != 2):
                        # Marcamos la celda que se deja con valor 4
                        grilla[posicion[0]][posicion[1]] = 4
                        # Actualizamos la posición
                        posicion = (posicion[0] + 1, posicion[1])
                        # Si la celda destino tiene comida (3), se incrementa el contador
                        if grilla[posicion[0]][posicion[1]] == 3:
                            comida_encontrada += 1
                        # Colocamos 0 en la celda destino para señalar que la hormiga se movió allí
                        grilla[posicion[0]][posicion[1]] = 0
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion)
                elif direccion == "arriba":
                    if (posicion[0] - 1 >= 0 and grilla[posicion[0] - 1][posicion[1]] != 2):
                        grilla[posicion[0]][posicion[1]] = 4
                        posicion = (posicion[0] - 1, posicion[1])
                        if grilla[posicion[0]][posicion[1]] == 3:
                            comida_encontrada += 1
                        grilla[posicion[0]][posicion[1]] = 0
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion)
            else:  # valor_aleatorio == "y"
                direccion = random.choice(["derecha", "izquierda"])
                if direccion == "derecha":
                    if (posicion[1] + 1 < len(grilla[0]) and grilla[posicion[0]][posicion[1] + 1] != 2):
                        grilla[posicion[0]][posicion[1]] = 4
                        posicion = (posicion[0], posicion[1] + 1)
                        if grilla[posicion[0]][posicion[1]] == 3:
                            comida_encontrada += 1
                        grilla[posicion[0]][posicion[1]] = 0
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion)
                elif direccion == "izquierda":
                    if (posicion[1] - 1 >= 0 and grilla[posicion[0]][posicion[1] - 1] != 2):
                        grilla[posicion[0]][posicion[1]] = 4
                        posicion = (posicion[0], posicion[1] - 1)
                        if grilla[posicion[0]][posicion[1]] == 3:
                            comida_encontrada += 1
                        grilla[posicion[0]][posicion[1]] = 0
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion)
        # Si la hormiga no pudo moverse tras max_reintentos, se conserva en la misma posición
        if not movimiento_exitoso:
            posiciones_finales.append(posicion)
    
    # Verificamos la condición de salida: si se ha encontrado al menos la mitad de la comida inicial
    if comida_encontrada >= (comida_inicial / 2):
        exit_flag = True
    else:
        exit_flag = False
    return posiciones_finales, exit_flag, grilla

def contador_de_pasos(grilla):
    """Cuenta las celdas con valor 4 en la grilla final, que representa los pasos totales."""
    pasos = 0
    for fila in grilla:
        pasos += fila.count(4)
    return pasos

def simulador(simulaciones):
    global comida_encontrada, pasos_globales
    resultados = []
    for i in range(simulaciones):
        # Reinicia la variable de comida consumida para cada simulación
        comida_encontrada = 0
        matrix(tamaño_grilla, hormigas, obstaculos, comida)
        if pasos_globales:
            # Tomamos el último valor (el total final de pasos de esta simulación)
            resultados.append(pasos_globales[-1])
        else:
            resultados.append(0)
    print("Terminé")
    print("Pasos por simulación:", resultados)
    promedio = sum(resultados) / len(resultados) if resultados else 0
    print(f"Promedio de pasos: {round(promedio, 2)}")
    print(f"Mínimo de pasos: {min(resultados)}")
    print(f"Máximo de pasos: {max(resultados)}")

simulador(100)