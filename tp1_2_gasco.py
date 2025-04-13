
import random
from termcolor import colored, cprint


# Parámetros fijos para la simulación
comida = 200           # Cantidad de comida a colocar en la grilla
tamaño_grilla = 250    # Dimensión de la grilla (250 x 250)
obstaculos = 100       # Número de obstáculos a colocar
hormigas = 20          # Número de hormigas (se colocan en posiciones iniciales)

comida_encontrada = 0  # Se incrementa cada vez que una hormiga se mueve a una celda con comida
pasos_globales = []    # Lista que almacenará, para cada simulación, el número de pasos (celdas recorridas)
grilla_final = []      # Guarda la grilla final de cada simulación

estado_a_color = {
    0: 'red', #Hormigas
    1: 'green',#celda libre
    2: 'black',#obstaculo
    3: 'white',#comida
    4: 'yellow',}#celda recorrida
               



def matrix (size,hormigas,obstaculos,comida):
    """
    Crea la grilla inicial.
    
    - Se genera una grilla de tamaño `n` x `n` con celdas inicializadas en 1 (vacías).
    """
    grilla =[]
    
    for i in range(0,size):
        grilla.append([])
        for y in range(0,size):
            grilla[i].append(1)
    
    # Llama a edit_grilla para insertar los elementos en la grilla.
    edit_grilla(grilla,hormigas,obstaculos,comida)
    



def edit_grilla (grilla,hormigas,obstaculos,comida):
    """
    Configura la grilla inicial colocando hormigas, obstáculos y comida.
    
    - Las hormigas se colocan en posiciones aleatorias y se guarda su posición inicial.
    - Se colocan obstáculos y comida en celdas vacías (valor 1) == verde.
    - Finalmente, se imprime la grilla y se inicia el movimiento de las hormigas.
    """
    comidalocal = comida #establecemos la comida que hay al momento 0 
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
    while comidalocal > 0:
        x = random.randint(0,len(grilla)-1)
        y = random.randint(0,len(grilla)-1)
        
        if grilla[x][y] == 1:
            grilla[x][y] = 3
            comidalocal -= 1
    
    
   
    
    
    exit = False
    while exit == False: #mientras la funcion movedor de hormigas detecte que se ha encontrado la mitad de la comida, las homigas se van a seguir moviendo
        nuevas_posiciones, exit, grilla_final = movedor_de_hormigas(grilla, posiciones_iniciales)
        posiciones_iniciales = nuevas_posiciones
    
    contador_de_pasos(grilla_final) #Cuando se haya la comida, se cuentan los pasos totales.
       
    
def movedor_de_hormigas(grilla, posiciones_iniciales):
    """
    Mueve cada hormiga una vez (o intenta hasta max_reintentos) a una dirección aleatoria.
    
    Si la celda destino contiene comida (valor 3), se incrementa el contador global 'comida_encontrada'
    
    Retorna una tupla con:
      - Las nuevas posiciones de las hormigas.
      - Un booleano (limite_alcanzado) que es True si se ha alcanzado al menos la mitad de la comida.
      - La grilla actualizada.
    """
    posiciones_finales= []
    
    global comida_encontrada
    for posicion in posiciones_iniciales:
       

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

                        if grilla[posicion[0]][posicion[1]] == 3: # Chequeamos si en la casilla hay comida
                            comida_encontrada += 1
                        grilla[posicion[0]][posicion[1]] = 0
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion)
                        

                elif direccion == "arriba":
                    if (posicion[0] - 1 >= 0 
                        and grilla[posicion[0] - 1][posicion[1]] != 2):
                        grilla[posicion[0]][posicion[1]] = 4
                        posicion = (posicion[0] - 1, posicion[1])

                        if grilla[posicion[0]][posicion[1]] == 3: # Chequeamos si en la casilla hay comida
                            comida_encontrada += 1
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
                        if grilla[posicion[0]][posicion[1]] == 3: # Chequeamos si en la casilla hay comida
                            comida_encontrada += 1
                        grilla[posicion[0]][posicion[1]] = 0
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion)
                elif direccion == "izquierda":
                    if (posicion[1] - 1 >= 0 
                        and grilla[posicion[0]][posicion[1] - 1] != 2):
                        grilla[posicion[0]][posicion[1]] = 4
                        posicion = (posicion[0], posicion[1] - 1)

                        if grilla[posicion[0]][posicion[1]] == 3: # Chequeamos si en la casilla hay comida
                            comida_encontrada += 1
                        grilla[posicion[0]][posicion[1]] = 0
                        movimiento_exitoso = True
                        posiciones_finales.append(posicion)
    
    if comida_encontrada >= (comida/2): #Si encontramos la mitad de la comida o mas. Detenemos la iteracion. 
        limite_alcanzado = True
        
        
    else:
        limite_alcanzado = False #No se alcanzo el limite
    
    return posiciones_finales, limite_alcanzado,grilla #Actualizamos las posiciones de los movimientos y si llegamos al limite de iteraciones.
    

def contador_de_pasos(grilla_final):
    """
    Cuenta el número de celdas con valor 4 (celdas recorridas) en la grilla final.

    y se agrega el resultado a la lista global 'pasos_globales'.
    """
    pasos = 0

    for fila in grilla_final:
        pasos +=fila.count(4) #Cuenta las casillas recorridas por las hormigas.
        
    pasos_globales.append(pasos/2) # dividimos los pasos ya que una celda representa 2 numeros dentro de nuestra grilla

def simulador (simulaciones):
    """
    Ejecuta la cantidad de simulaciones especificada.
    Para cada simulación:
      - Se reinicia el contador de comida encontrada.
      - Se registra el número de pasos realizados.
      
    Al finalizar, se calcula y muestra el número de pasos en promedio, el mínimo y el máximo necesarios.
    """

    for i in range(simulaciones):
        
        global comida_encontrada 
        comida_encontrada = 0
        matrix(tamaño_grilla,hormigas,obstaculos,comida)
    

    pasos_totales = 0
    for value in pasos_globales:
       
       pasos_totales += value  
    promedio_de_pasos = pasos_totales / len(pasos_globales)
    pasos_globales.sort() #Ordenamos los valores de menor a mayor para luego imprimir el primero y el ultimo
    
    print(f"Para encontrar al menos la mitad de la comida se necesitaron: \n - {round(promedio_de_pasos,2)} pasos en promedio. \n - {round(pasos_globales[0])} pasos como minimo.\n - {round(pasos_globales[-1])} pasos como maximo.")
   

simulador(100)