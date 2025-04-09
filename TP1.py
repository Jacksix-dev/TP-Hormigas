from copy import deepcopy
import time 
import random
from termcolor import colored, cprint
import sys
sys.stdout.reconfigure(encoding='utf-8')



def printer (grilla):
    

    for i in range(len(grilla)):
        for j in range(len(grilla[i])):
            
            if grilla[i][j] == 1: 
                grilla[i][j] = colored("▓▓", "green")
            if grilla[i][j] == 2:
                grilla[i][j] = colored("▓▓", "white")
            if grilla[i][j] == 3:
                grilla[i][j] = colored("▓▓", "red")
            if grilla[i][j] == 4:
                grilla[i][j] =  colored("▓▓", "black")           
            if grilla[i][j] == 5:
                grilla[i][j] =  colored("▓▓", "yellow")

    
    for i in range(len(grilla[i])):
        print("".join(grilla[i]))


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
            grilla[i].append(2)
    
    printer(grilla)
        


matrix(30)


lol = colored("▓▓", "green")
cprint(lol)
text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
print(text)
cprint("Hello, World!", "green", "on_red")