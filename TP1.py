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
    2: 'blue',
    3: 'white',
    4: 'yellow',} 

    for fila in grilla:
        fila_str = ""
        for celda in fila:
            color = estado_a_color[celda]
            fila_str += colored("▓▓", color)
        print(fila_str)



def matrix (size):
    
    vacia = 1
    comida= 2
    ocupada = 3
    obstaculo = 4
    recorrida = 5
    grilla =[]
    
    for i in range(0,size):
        grilla.append([])
        for y in range(0,size):
            grilla[i].append(1)
    
    printer(grilla)
        
random = random.randint(0,4)

print(random)

