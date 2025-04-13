from copy import deepcopy
import time 
import random
from termcolor import colored, cprint
import sys
sys.stdout.reconfigure(encoding='utf-8')

comida = 200
tamaño_grilla = 60
tiempo = 1000
obstaculos = 100
hormigas = 20

pasos_globales = []

def contador_de_comida(grilla):
    comida_disponible = 0
    pasos = 0
    
    for i in range(tamaño_grilla):
        for y in range(tamaño_grilla):
            if grilla[i][y] == 4:
                pasos += 1
            if grilla[i][y] == 3:
                comida_disponible += 1                   
    if comida_disponible <= comida/2:
        
        pasos_globales.append(pasos)
        return True     
    else:
        
         
        return False
        

               


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

    if contador_de_comida(grilla) == False:
        
        iterador(grilla,posiciones_iniciales,tiempo)


def iterador (grilla, posiciones_iniciales,tiempo):
    for i in range(0,tiempo):
       if contador_de_comida(grilla) == False:
            posiciones_iniciales = movedor_de_hormigas(grilla, posiciones_iniciales)
       else:
           break
       
    
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

    
    
    
    
    return posiciones_finales
    



def matrix (size,hormigas,obstaculos,comida,tiempo):
    
    grilla =[]
    
    for i in range(0,size):
        grilla.append([])
        for y in range(0,size):
            grilla[i].append(1)
    
    
    edit_grilla(grilla,hormigas,obstaculos,comida,tiempo)
    

def simulador (simulaciones):
    for i in range(simulaciones):
        matrix(tamaño_grilla,hormigas,obstaculos,comida,tiempo)
    
    pasos_totales = 0
    for value in pasos_globales:
        pasos_totales += value  
    promedio_de_pasos = pasos_totales / len(pasos_globales)
    pasos_globales.sort()
    print(pasos_globales)
    print(f"Para encontrar al menos la mitad de la comida se necesitaron: \n - {round(promedio_de_pasos,2)} pasos en promedio. \n - {pasos_globales[0]} pasos como minimo.\n - {pasos_globales[-1]} pasos como maximo.")


simulador(100)