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
    
maquinas = 4
trabajos = 4
#poblacion = [(i + 1) for i in range(maquinas * trabajos)] #Definir poblacion inicial
#shuffle(poblacion)

tamano = 2
poblacion = []

for x in range(tamano):
    individuo = [(i + 1) for i in range(maquinas * trabajos)]
    shuffle(individuo)
    poblacion.append( individuo )

print poblacion

def fila(m):
    return ceil(m/maquinas)
    
def columna(n):
    c = n % maquinas
    if c == 0:
        c = maquinas
    
    return c 
 
for x in range(tamano):
    poblacion[x]

   # def __init__(self, params):
    #    '''
     #   Constructor
      #  '''
        