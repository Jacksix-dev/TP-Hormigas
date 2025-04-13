#Funciones utilizadas en todos los archivos

import random

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
    
    # Llama a edit_grilla para insertar los elementos en la grilla.
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

def movedor_de_hormigas(grilla, posiciones_iniciales):
    """
    Mueve cada hormiga desde su posición actual a una posición adyacente válida.
    
    Se intenta mover la hormiga en el eje "x" o "y" de forma aleatoria, 
    evitando que se mueva a una celda con un obstáculo (valor 2) o fuera de la grilla. 
    La celda original se marca como visitada (valor 4 - amarillo) y la nueva posición recibe el valor de la hormiga (valor 0).
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
                        grilla[posicion[0]][posicion[1]] = 4 #Se marca la celda como recorrida 
                        posicion = (posicion[0] + 1, posicion[1])
                        grilla[posicion[0]][posicion[1]] = 0 #Se mueve la hormiga
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion) #Se actualizan las posiciones

                elif direccion == "arriba":
                    if (posicion[0] - 1 >= 0 
                        and grilla[posicion[0] - 1][posicion[1]] != 2): #Si la celda esta dentro de la grilla y no es un obstaculo movemos la hormiga
                        grilla[posicion[0]][posicion[1]] = 4 #Se marca la celda como recorrida 
                        posicion = (posicion[0] - 1, posicion[1])
                        grilla[posicion[0]][posicion[1]] = 0 #Se mueve la hormiga
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion)
            else:  # valor_aleatorio == "x" y luego se define si va a la izquierda o la derecha.
                direccion = random.choice(["derecha", "izquierda"])
                if direccion == "derecha":
                    if (posicion[1] + 1 < len(grilla[0]) 
                        and grilla[posicion[0]][posicion[1] + 1] != 2): #Si la celda esta dentro de la grilla y no es un obstaculo movemos la hormiga
                        grilla[posicion[0]][posicion[1]] = 4 #Se marca la celda como recorrida 
                        posicion = (posicion[0], posicion[1] + 1)
                        grilla[posicion[0]][posicion[1]] = 0 #Se mueve la hormiga
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion)
                elif direccion == "izquierda":
                    if (posicion[1] - 1 >= 0 
                        and grilla[posicion[0]][posicion[1] - 1] != 2): #Si la celda esta dentro de la grilla y no es un obstaculo movemos la hormiga
                        grilla[posicion[0]][posicion[1]] = 4 #Se marca la celda como recorrida 
                        posicion = (posicion[0], posicion[1] - 1)
                        grilla[posicion[0]][posicion[1]] = 0 #Se mueve la hormiga
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion)