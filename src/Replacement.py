'''
Created on Apr 26, 2016

@author: Angie Blanco
'''
from random import random

class Reemplazo(object):
    
    '''
    classdocs
    '''
    def __init__(self, generacional):
        '''
        Constructor
        '''
        self.mecanismo = generacional

        
    def realizarReemplazo(self, padre1, padre2, hijo1, hijo2):
        if self.mecanismo:
            return self.generacional(padre1, padre2, hijo1, hijo2)
        else:
            return self.steadyState(padre1, padre2, hijo1, hijo2)
        
        
    '''
    'Estrategia de reemplazo generacional
    '''
    def generacional(self, padre1, padre2, hijo1, hijo2):
        siguienteGeneracion = []
        siguienteGeneracion.append(hijo1) #pasa el hijo 1
        siguienteGeneracion.append(hijo2) #pasa el hijo 2
        
        return siguienteGeneracion
    
    
    '''
    Estrategia de ruleta para definir el ganador entre dos individuos de acuerdo a su fitness
    '''
    def ruleta(self, jugador1, jugador2):
        total = ( jugador1.fitness + jugador2.fitness ) #se suma el desempeno de los dos individuos, para normalizar la ruleta
        
        punto = 1 - (jugador1.fitness / total) #se define la proporcion de la ruleta que corresponde al jugador 1
        aleatorio = random()
        
        if punto >= aleatorio: #si la ruleta cae en la parte del jugador 1 este gano, sino el ganador sera el jugador 2
            ganador = jugador1
        else:
            ganador = jugador2
            
        return ganador
    
    
    '''
    '''
    def steadyState(self, padre1, padre2, hijo1, hijo2):
        winners = []
        desempenop1 = padre1.fitness 
        desempenop2 = padre2.fitness
        desempenoh1 = hijo1.fitness
        desempenoh2 = hijo2.fitness
        
        #de acuerdo a los desempenos, se deja al mejor padre como jugadorA, el mejor hijo como jugadorB, el peor padre como jugadorC, y el peor hijo como jugadorD
        if desempenop1 >= desempenop2:
            if desempenoh1 >= desempenoh2:
                jugadorA = (padre1)
                jugadorB = (hijo1)
                jugadorC = (padre2)
                jugadorD = (hijo2)
            else:
                jugadorA = (padre1)
                jugadorB = (hijo2)
                jugadorC = (padre2)
                jugadorD = (hijo1)
        else:
            if desempenoh1 >= desempenoh2:
                jugadorA = (padre2)
                jugadorB = (hijo1)
                jugadorC = (padre1)
                jugadorD = (hijo2)
            else:
                jugadorA = (padre2)
                jugadorB = (hijo2)
                jugadorC = (padre1)
                jugadorD = (hijo1)
            
        ganador1 = ruleta(jugadora,jugadorb) #se enfrentan el mejor padre y el mejor hijo
        ganador2 = ruleta(jugadorc,jugadord) #se enfrentan el peor padre y el peor hijo
        
        siguienteGeneracion.append(ganador1) #se agrega el ganador de la primera ruleta
        siguienteGeneracion.append(ganador2) #se agrega el ganador de la segunda ruleta
        
        return siguienteGeneracion