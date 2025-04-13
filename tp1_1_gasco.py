
import time 
import random
from termcolor import colored, cprint


comida = 25
tamaño_grilla = 30
obstaculos = 30
hormigas = 5
tiempo = 100


def matrix (tamaño_grilla,hormigas,obstaculos,comida,tiempo):
    """
    Crea la grilla inicial.
    
    - Se genera una grilla de tamaño `n` x `n` con celdas inicializadas en 1 (vacías).
    """
    grilla =[]
    
    for i in range(0,tamaño_grilla):
        grilla.append([])
        for y in range(0,tamaño_grilla):
            grilla[i].append(1)
    
    
    edit_grilla(grilla,hormigas,obstaculos,comida,tiempo)
    
def edit_grilla (grilla,hormigas,obstaculos,comida,tiempo):
    """
    Configura la grilla inicial colocando hormigas, obstáculos y comida.
    
    - Las hormigas se colocan en posiciones aleatorias y se guarda su posición inicial.
    - Se colocan obstáculos y comida en celdas vacías (valor 1) == verde.
    - Finalmente, se imprime la grilla y se inicia el movimiento de las hormigas.
    """
    
    comida = comida
    posiciones_iniciales=[]
    
    # Coloca hormigas en posiciones aleatorias
    while hormigas > 0:
        x = random.randint(0, len(grilla) - 1)
        y = random.randint(0, len(grilla) - 1)
        grilla[x][y] = 0  # Marca la celda con una hormiga
        hormigas -= 1
        posiciones_iniciales.append([x, y])
    
    # Coloca obstáculos en celdas vacías
    while obstaculos > 0:
        x = random.randint(0, len(grilla) - 1)
        y = random.randint(0, len(grilla) - 1)
        if grilla[x][y] == 1:
            grilla[x][y] = 2  # Marca la celda como obstáculo
            obstaculos -= 1
            
    # Coloca comida en celdas vacías
    while comida > 0:
        x = random.randint(0, len(grilla) - 1)
        y = random.randint(0, len(grilla) - 1)
        if grilla[x][y] == 1:
            grilla[x][y] = 3  # Marca la celda con comida
            comida -= 1

   
    printer(grilla)
    iterador(grilla,posiciones_iniciales,tiempo)


def printer (grilla):

    """
    Imprime la grilla en la consola utilizando colores.
    
    Cada valor de la grilla se mapea a un color específico mediante el diccionario `estado_a_color`.
    """

    estado_a_color = {
    0: 'red', #Hormigas
    1: 'green',#Celda vacia
    2: 'black',#Obstaculo
    3: 'white',#Comida
    4: 'yellow',} #Celda recorrida

    for fila in grilla:
        fila_str = ""
        for celda in fila:
            color = estado_a_color[celda]
            fila_str += colored("▓▓", color)
        print(fila_str)
    return grilla
        

def iterador (grilla, posiciones_iniciales,tiempo):
    """
    Ejecuta iterativamente el movimiento de las hormigas durante el número de iteraciones especificado.
    
    En cada iteración se actualizan las posiciones de las hormigas llamando a `movedor_de_hormigas`.
    """
    for i in range(0,tiempo):
       posiciones_iniciales = movedor_de_hormigas(grilla, posiciones_iniciales)



def movedor_de_hormigas(grilla, posiciones_iniciales):
    """
    Mueve cada hormiga desde su posición actual a una posición adyacente válida.
    
    Se intenta mover la hormiga en el eje "x" o "y" de forma aleatoria, 
    evitando que se mueva a una celda con un obstáculo (valor 2). 
    La celda original se marca como visitada (valor 4) y la nueva posición recibe el valor de la hormiga (valor 0).
    Se intentará el movimiento hasta 10 veces en caso de encontrar una posición inválida.
    
    Devuelve una lista actualizada de las posiciones finales de las hormigas.
    """
    

    posiciones_finales= []
    
    for posicion in posiciones_iniciales:
        # Pintamos la grilla donde estuvo la hormiga con el valor 4 (amarillo)
        grilla[posicion[0]][posicion[1]] = 4 

        movimiento_exitoso = False
        reintentos = 0
        max_reintentos = 10

        # Intentamos hasta 10 veces hallar un movimiento válido
        while not movimiento_exitoso and reintentos < max_reintentos:
            reintentos += 1
            valor_aleatorio = random.choice(["x", "y"]) #Se elige aleatoriamente un valor x o y

            if valor_aleatorio == "y": 
                direccion = random.choice(["arriba", "abajo"])
                if direccion == "abajo":
                    if (posicion[0] + 1 < len(grilla) 
                        and grilla[posicion[0] + 1][posicion[1]] != 2): #Si la celda esta dentro de la grilla y no es un obstaculo movemos la hormiga
                        grilla[posicion[0]][posicion[1]] = 4
                        posicion = (posicion[0] + 1, posicion[1])
                        grilla[posicion[0]][posicion[1]] = 0
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion) #Se actualizan las posiciones

                elif direccion == "arriba":
                    if (posicion[0] - 1 >= 0 
                        and grilla[posicion[0] - 1][posicion[1]] != 2):
                        grilla[posicion[0]][posicion[1]] = 4
                        posicion = (posicion[0] - 1, posicion[1])
                        grilla[posicion[0]][posicion[1]] = 0
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion)
            else:  # valor_aleatorio == "x" y luego se define si va a la izquierda o la derecha.
                direccion = random.choice(["derecha", "izquierda"])
                if direccion == "derecha":
                    if (posicion[1] + 1 < len(grilla[0]) 
                        and grilla[posicion[0]][posicion[1] + 1] != 2):
                        grilla[posicion[0]][posicion[1]] = 4
                        posicion = (posicion[0], posicion[1] + 1)
                        grilla[posicion[0]][posicion[1]] = 0
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion)
                elif direccion == "izquierda":
                    if (posicion[1] - 1 >= 0 
                        and grilla[posicion[0]][posicion[1] - 1] != 2):
                        grilla[posicion[0]][posicion[1]] = 4
                        posicion = (posicion[0], posicion[1] - 1)
                        grilla[posicion[0]][posicion[1]] = 0
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion)

    time.sleep(0.25) #Separamos cada iteracion por un periodo de tiempo
    printer(grilla) #Imprimimos la grilla
    return posiciones_finales


matrix(tamaño_grilla,hormigas,obstaculos,comida,tiempo)
