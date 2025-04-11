from copy import deepcopy
import time 
import random
from termcolor import colored, cprint
import sys
sys.stdout.reconfigure(encoding='utf-8')

comida = 25
tamaño = 30

def contador_de_comida(grilla):
    comida_disponible = 0

    for i in range(tamaño):
        for y in range(tamaño):
            if grilla[i][y] == 3:
                comida_disponible += 1
                print(comida_disponible)
                if comida_disponible == comida/2:
                    print("te comiste mas de la mitad")
                    
             


               


def printer (grilla):

    estado_a_color = {
    0: 'red',
    1: 'green',
    2: 'black',
    3: 'white',
    4: 'yellow',} 

    for fila in grilla:
        fila_str = ""
        for celda in fila:
            color = estado_a_color[celda]
            fila_str += colored("▓▓", color)
        print(fila_str)
    return grilla
        

def edit_grilla (grilla,hormigas,obstaculos,comida,tiempo):
    comida = comida
    posiciones_iniciales=[]
    
    while hormigas > 0:
        x = random.randint(0,len(grilla)-1)
        y = random.randint(0,len(grilla)-1)
        
        grilla[x][y] = 0
        hormigas -= 1
        posiciones_iniciales.append([x,y])

    while obstaculos > 0:
        x = random.randint(0,len(grilla)-1)
        y = random.randint(0,len(grilla)-1)
        
        if grilla[x][y] == 1:
            grilla[x][y] = 2
            obstaculos -= 1
    while comida > 0:
        x = random.randint(0,len(grilla)-1)
        y = random.randint(0,len(grilla)-1)
        
        if grilla[x][y] == 1:
            grilla[x][y] = 3
            comida -= 1

   
    printer(grilla)
    iterador(grilla,posiciones_iniciales,tiempo)
    contador_de_comida(grilla)
    
def movedor_de_hormigas(grilla, posiciones_iniciales):
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
            valor_aleatorio = random.choice(["x", "y"])

            if valor_aleatorio == "x":
                direccion = random.choice(["arriba", "abajo"])
                if direccion == "abajo":
                    if (posicion[0] + 1 < len(grilla) 
                        and grilla[posicion[0] + 1][posicion[1]] != 2):
                        grilla[posicion[0]][posicion[1]] = 4
                        posicion = (posicion[0] + 1, posicion[1])
                        grilla[posicion[0]][posicion[1]] = 0
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion)

                elif direccion == "arriba":
                    if (posicion[0] - 1 >= 0 
                        and grilla[posicion[0] - 1][posicion[1]] != 2):
                        grilla[posicion[0]][posicion[1]] = 4
                        posicion = (posicion[0] - 1, posicion[1])
                        grilla[posicion[0]][posicion[1]] = 0
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion)
            else:  # valor_aleatorio == "y"
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

    time.sleep(0.1)
    
    
    printer(grilla)
    return posiciones_finales

def iterador (grilla, posiciones_iniciales,tiempo):
    for i in range(0,tiempo):
       posiciones_iniciales = movedor_de_hormigas(grilla, posiciones_iniciales)


def matrix (tamaño,hormigas,obstaculos,comida,tiempo):
    
    grilla =[]
    
    for i in range(0,tamaño):
        grilla.append([])
        for y in range(0,tamaño):
            grilla[i].append(1)
    
    
    edit_grilla(grilla,hormigas,obstaculos,comida,tiempo)
    

matrix(tamaño,5,comida,50,50)
