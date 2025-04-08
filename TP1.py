from copy import deepcopy
import time 
import random
import sys
from termcolor import colored, cprint


def printer (mtx,dimention):
    
    
    for i in range(len(mtx)):
        if mtx[i] == 1: 
            print("entro")
            mtx[i] = colored("▓▓", "green")
        if mtx[i] == 2:
            mtx[i] = colored("▓▓", "white")
        if mtx[i] == 3:
            mtx[i] = colored("▓▓", "red")
        if mtx[i] == 4:
            mtx[i] =  colored("▓▓", "black")           
        if mtx[i] == 5:
            mtx[i]=  colored("▓▓", "yellow")

    dimentionstart = deepcopy(dimention)
    counter = 0
    print(f"{dimentionstart} xdddddd")
    while dimention < dimentionstart*dimentionstart:
        
        if counter == dimention:
            
            slicedmatrix = mtx[counter-dimention:dimention-1]
            
            dimention = dimention + dimention
            
            print("".join(slicedmatrix))
        else:
            counter = counter + 1


    

def matrix (size):
    print("entro")
    vacia = 2222
    comida= 2
    ocupada = 3
    obstaculo = 4
    recorrida = 5
    mtx =[]
    for i in range(0,size**2):
        mtx.append(4)
        
    
    
    printer(mtx,size)



matrix(5)


