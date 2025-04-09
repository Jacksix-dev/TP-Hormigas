from copy import deepcopy
import time 
import random
from termcolor import colored, cprint

size= 5

def printer (grilla):
    
    
    for i in range(len(grilla)):

        for valor in grilla[i]:
            print(grilla[i])
            if valor == 1: 
                valor = colored("▓▓", "green")
            if valor == 2:
                valor = colored("▓▓", "white")
            if valor == 3:
                valor = colored("▓▓", "red")
            if valor == 4:
                valor =  colored("▓▓", "black")           
            if valor == 5:
                valor =  colored("▓▓", "yellow")
    colored_grid = deepcopy(grilla)   

    for i in range(0,len(colored_grid)):
        for valor in colored_grid:
            print(valor)



    

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
    
        


matrix(size)


