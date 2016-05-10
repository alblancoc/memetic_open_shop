'''
Created on Apr 26, 2016

@author: carlosandressierra
'''
from random import shuffle
from math import ceil
from math import floor
#class Population(object):
   # '''
   # classdocs
    
   # '''
    
maquinas = 3
trabajos = 3
#poblacion = [(i + 1) for i in range(maquinas * trabajos)] #Definir poblacion inicial
#shuffle(poblacion)

tamano = 1
poblacion = []

for x in range(tamano):
    individuo = [(i + 1) for i in range(maquinas * trabajos)]
    shuffle(individuo)
    poblacion.append( individuo )

print poblacion



def fila(m):
    f = int(ceil(m/maquinas))
    return f
    
def columna(n):
    c = n % maquinas 
    if c == 0:
        c = maquinas 
    
    return c 

def mejora(poblacion):      
    for x in range(0,len(poblacion),1): #para todos los individuos de la poblacion
        mover = [(0) for i in range(maquinas * trabajos)] # Creacion de vector de movimientos
        for z in range(1,((maquinas*trabajos)-maquinas)): # Recorrer todas las operaciones que se pueden correr
            for i in range((z-1),(z+maquinas+1)): # operaciones cercanas
                if fila(i) == fila(i+1) or columna(i) == columna(i+1): #Misma fila o misma columna
                    mover[(poblacion[x][i+1]-1)] = 1
                    cambio = poblacion[x][i+1]
                    movimiento = 0
                    act = i+1
                    act2 = i+1
                    while movimiento < (maquinas - 1) and act < (maquinas*trabajos)-maquinas-2 and act2 < (maquinas*trabajos)-maquinas-2:
                        while mover[(poblacion[x][act+1]-1)] == 1 :
                            act += 1
                        if act > (i+1):
                           poblacion[x][i+1] = poblacion[x][act+1]
                           poblacion[x][act+1] = cambio
                           movimiento += 1
                           z -= 1
                        if (act2 >= (i+1)):
                            poblacion[x][i+1] = poblacion[x][act2+1]
                            poblacion[x][act2+1] = cambio
                            movimiento += 1
                            act2 += 1
                            z -= 1
        
    return poblacion    

hu = mejora(poblacion)
print hu


            
           

   # def __init__(self, params):
    #    '''
     #   Constructor
      #  '''
    
def uniforme(self):
    padres = []
    padre1 = randint(0,len(poblacion)-1)
    padre2 = randint(0, len(poblacion)-1)
        
    while (padre1 == padre2):
        padre2 = randint(0, len(poblacion)-1)
    
    padres.append(poblacion[padre1])
    padres.append(poblacion[padre2])
    
    return padres
 
    
def ruleta(self, player1, player2):
        desempeno1 = player1.obtainFitness 
        desempeno2 = player2.obtainFitness
        total = (desempeno1+desempeno2)
        punto = 1 - (desempeno1/total)
        aleatorio = random()
        if punto >= aleatorio:
            winner = player1
        else:
            winner = player2
            
        return winner

def torneo(self,mejor_indice):
    
    participante1 = mejor_indice
    participante2 = randint(0,len(poblacion))
    participante3 = randint(0,len(poblacion))
    participante4 = randint(0,len(poblacion))
    
    padre1 = ruleta(poblacion[participante1],poblacion[participante2])
    padre2 = ruleta(poblacion[participante3],poblacion[participante4])
    padre = ruleta(padre1, padre2)
    
    return padre        