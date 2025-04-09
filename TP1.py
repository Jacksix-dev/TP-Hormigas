from copy import deepcopy
import time 
import random
from termcolor import colored, cprint
import sys
sys.stdout.reconfigure(encoding='utf-8')



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
        





def edit_grilla (grilla,hormigas,obstaculos,comida):
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
    movedor_de_hormigas(grilla,posiciones_iniciales)
    
def movedor_de_hormigas (grilla,posiciones_iniciales):

    
    for pocision in posiciones_iniciales:
        grilla[pocision[0]][pocision[1]] = 4 
        valor_aleatorio = random.choice(["x", "y"])
        if valor_aleatorio == "x":
            direccion = random.choice(["derecha", "izquierda"])
            
            if direccion == "derecha":
                    
                    grilla[pocision[0]+1][pocision[1]] = 0

        if valor_aleatorio == "y":
            direccion = random.choice(["derecha", "izquierda"])

            if direccion == "derecha":

                    grilla[pocision[0]][pocision[1]+1] = 0           
            if direccion == "izquierda":
                    
                    grilla[pocision[0]][pocision[1]-1] = 0 
    time.sleep(0.5)
    print("---------------------------------------------------------")
    printer(grilla)


def matrix (size,hormigas,obstaculos,comida):
    
    grilla =[]
    
    for i in range(0,size):
        grilla.append([])
        for y in range(0,size):
            grilla[i].append(1)
    
    
    edit_grilla(grilla,hormigas,obstaculos,comida)


matrix(30,5,10,25)
