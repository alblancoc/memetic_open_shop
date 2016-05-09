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

      
for x in range(tamano):
    mover = [(0) for i in range(maquinas * trabajos)] # Creacion de vector de movimientos
    
    
            
               
print poblacion            

   # def __init__(self, params):
    #    '''
     #   Constructor
      #  '''
        