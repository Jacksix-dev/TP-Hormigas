import time 
import random
from termcolor import colored
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Parámetros de la simulación
COMIDA = 200
TAMAÑO_GRILLA = 250
OBSTACULOS = 100
HORMIGAS = 20
MAX_ITERACIONES = 100000  # límite para evitar bucles infinitos en cada simulación
SIMULACIONES = 100

# (Opcional) Diccionario de estado para usar en impresión, no necesario para la lógica
estado_a_color = {
    0: 'hormiga',
    1: 'libre',
    2: 'obstaculo',
    3: 'comida',
    4: 'celda recorrida'
}

# Lista para guardar los pasos totales requeridos en cada simulación
resultados_pasos = []


def crear_grilla(size):
    """Crea una grilla de 'size x size' inicializada en 1 (celda libre)."""
    grilla = []
    for i in range(size):
        fila = [1] * size
        grilla.append(fila)
    return grilla


def iniciar_elementos(grilla, hormigas, obstaculos, comida):
    """
    Coloca hormigas (valor 0), obstáculos (valor 2) y comida (valor 3) en la grilla.
    Devuelve la lista de posiciones iniciales de las hormigas y
    conserva la cantidad de comida inicial (antes de consumirla).
    """
    posiciones_iniciales = []

    # Colocar hormigas: se colocan en celdas aleatorias sin importar colisiones
    for _ in range(hormigas):
        x = random.randint(0, len(grilla)-1)
        y = random.randint(0, len(grilla)-1)
        grilla[x][y] = 0  # hormiga
        posiciones_iniciales.append([x, y])

    # Colocar obstáculos: se coloca en celdas que estén libres (valor 1)
    obstaculos_restantes = obstaculos
    while obstaculos_restantes > 0:
        x = random.randint(0, len(grilla)-1)
        y = random.randint(0, len(grilla)-1)
        if grilla[x][y] == 1:
            grilla[x][y] = 2
            obstaculos_restantes -= 1

    # Colocar comida: se coloca en celdas libres
    comida_restante = comida
    while comida_restante > 0:
        x = random.randint(0, len(grilla)-1)
        y = random.randint(0, len(grilla)-1)
        if grilla[x][y] == 1:
            grilla[x][y] = 3
            comida_restante -= 1

    return posiciones_iniciales


def mover_hormigas(grilla, posiciones_iniciales):
    """
    Mueve cada hormiga una vez (o intenta hasta max_reintentos) según una dirección
    aleatoria. Actualiza:
      - El contador de pasos de esta ronda.
      - La cantidad de comida encontrada, si la hormiga se mueve a una celda con comida.
    Devuelve la lista de nuevas posiciones.
    """
    posiciones_finales = []
    pasos = 0
    max_reintentos = 10

    # Para cada hormiga, se intenta mover según una dirección válida.
    for posicion in posiciones_iniciales:
        # Marcamos la celda actual como recorrida (valor 4)
        grilla[posicion[0]][posicion[1]] = 4

        movimiento_exitoso = False
        reintentos = 0

        while not movimiento_exitoso and reintentos < max_reintentos:
            reintentos += 1
            eje = random.choice(["x", "y"])

            if eje == "x":
                direccion = random.choice(["arriba", "abajo"])
                if direccion == "abajo":
                    if posicion[0] + 1 < len(grilla) and grilla[posicion[0] + 1][posicion[1]] != 2:
                        # Si la celda destino contiene comida (valor 3)
                        if grilla[posicion[0] + 1][posicion[1]] == 3:
                            # La hormiga "consume" la comida y se cuenta
                            
                            comida_encontrada += 1
                        # Se actualiza la posición (movimiento hacia abajo)
                        posicion = (posicion[0] + 1, posicion[1])
                        grilla[posicion[0]][posicion[1]] = 0  # la hormiga ahora ocupa esta celda
                        pasos += 1
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion)
                elif direccion == "arriba":
                    if posicion[0] - 1 >= 0 and grilla[posicion[0] - 1][posicion[1]] != 2:
                        if grilla[posicion[0] - 1][posicion[1]] == 3:
                            global comida_encontrada
                            comida_encontrada += 1
                        posicion = (posicion[0] - 1, posicion[1])
                        grilla[posicion[0]][posicion[1]] = 0
                        pasos += 1
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion)

            else:  # eje == "y"
                direccion = random.choice(["derecha", "izquierda"])
                if direccion == "derecha":
                    if posicion[1] + 1 < len(grilla[0]) and grilla[posicion[0]][posicion[1] + 1] != 2:
                        if grilla[posicion[0]][posicion[1] + 1] == 3:
                            global comida_encontrada
                            comida_encontrada += 1
                        posicion = (posicion[0], posicion[1] + 1)
                        grilla[posicion[0]][posicion[1]] = 0
                        pasos += 1
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion)
                elif direccion == "izquierda":
                    if posicion[1] - 1 >= 0 and grilla[posicion[0]][posicion[1] - 1] != 2:
                        if grilla[posicion[0]][posicion[1] - 1] == 3:
                            global comida_encontrada
                            comida_encontrada += 1
                        posicion = (posicion[0], posicion[1] - 1)
                        grilla[posicion[0]][posicion[1]] = 0
                        pasos += 1
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion)
        # Si ninguno de los intentos tuvo éxito, la hormiga no se mueve y se mantiene en su posición.
        if not movimiento_exitoso:
            posiciones_finales.append(posicion)

    # Acumulamos los pasos realizados en esta ronda.
    global pasos_totales
    pasos_totales += pasos
    return posiciones_finales


def simular():
    """
    Realiza una simulación en la que se detiene cuando se ha consumido al menos la mitad
    de la comida inicial. Devuelve la cantidad total de pasos realizados.
    """
    global comida_encontrada, pasos_totales

    # Reiniciamos contadores para esta simulación
    comida_encontrada = 0
    pasos_totales = 0

    grilla = crear_grilla(TAMAÑO_GRILLA)
    posiciones_iniciales = iniciar_elementos(grilla, HORMIGAS, OBSTACULOS, COMIDA)

    # Guardamos la cantidad inicial de comida para la comparación (sin modificarla al colocar comida)
    comida_inicial = COMIDA

    iteraciones = 0
    # Ejecutamos movimientos hasta que se encuentre la mitad de la comida o se alcance un límite
    while comida_encontrada < (comida_inicial / 2) and iteraciones < MAX_ITERACIONES:
        posiciones_iniciales = mover_hormigas(grilla, posiciones_iniciales)
        iteraciones += 1

    return pasos_totales


def simulador(simulaciones):
    resultados = []
    for i in range(simulaciones):
        pasos = simular()
        resultados.append(pasos)
        print(f"Simulación {i+1}: {pasos} pasos")
    # Calcular promedio, mínimo y máximo
    promedio = sum(resultados) / len(resultados)
    minimo = min(resultados)
    maximo = max(resultados)
    print("\nResultados finales:")
    print(f"  Promedio de pasos: {round(promedio, 2)}")
    print(f"  Mínimo de pasos: {minimo}")
    print(f"  Máximo de pasos: {maximo}")


# Ejecutar 100 simulaciones
simulador(SIMULACIONES)