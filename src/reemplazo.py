'''
Esta clase determina las estrategias de reemplazo a utilizar en el algoritmo genetico

Created on Apr 26, 2016

@author: Angie Blanco
'''
from random import random

class Reemplazo(object):
    
    '''
    Constructor de la clase
    @param generacional: si la estrategia de reemplazo es generacional (True) o Steady-State (False)
    '''
    def __init__(self, generacional):
        self.mecanismo = generacional #se determina que mecanismo de reemplazo se va a utilizar

        
    '''
    Este metodo recibe a los dos padres y a los dos hijos, y define que individuos pasan a la siguiente generacion.
    @param padre1: Representacion del primer padre
    @param padre2: Representacion del segundo padre
    @param hijo1: Representacion del primer hijo
    @param hijo2: Representacion del segundo hijo
    @return: individuos para la siguiente generaicon
    '''    
    def realizarReemplazo(self, padre1, padre2, hijo1, hijo2):
        if self.mecanismo: #se determina si el mecanismo es generacional (True) o steady-state (False)
            return self.generacional(padre1, padre2, hijo1, hijo2) #se invoca a generacional
        else:
            return self.steadyState(padre1, padre2, hijo1, hijo2) #se invoca a steady-state
        
        
    '''
    Estrategia de reemplazo generacional, en la cual quienes pasan a la siguien generacion son los hijos
    @param padre1: Representacion del primer padre
    @param padre2: Representacion del segundo padre
    @param hijo1: Representacion del primer hijo
    @param hijo2: Representacion del segundo hijo
    @return: individuos para la siguiente generacion
    '''
    def generacional(self, padre1, padre2, hijo1, hijo2):
        siguienteGeneracion = [] #vector de hijos 
        siguienteGeneracion.append(hijo1) #pasa el hijo 1
        siguienteGeneracion.append(hijo2) #pasa el hijo 2
        
        return siguienteGeneracion 
    
    
    '''
    Estrategia de ruleta para definir el ganador entre dos individuos de acuerdo a su fitness
    @param jugador1:
    @param jugador2:
    @return: 
    '''
    def ruleta(self, jugador1, jugador2):
        total = ( jugador1.obtenerFitness() + jugador2.obtenerFitness() ) #se suma el desempeno de los dos individuos, para normalizar la ruleta
        
        punto = 1.0 - (jugador1.obtenerFitness() / float(total)) #se define la proporcion de la ruleta que corresponde al jugador 1
        aleatorio = random()
        
        if aleatorio < punto: #si la ruleta cae en la parte del jugador 1 este gano, sino el ganador sera el jugador 2
            ganador = jugador1
        else:
            ganador = jugador2
            
        return ganador
    
    
    '''
    Empareja el mejor padre con el mejor hijo, el peor padre con el peor hijo, y mediante enfrentamientos en ruleta determina quienes pasan a la siguiente generacion
    @param padre1: Representacion del primer padre
    @param padre2: Representacion del segundo padre
    @param hijo1: Representacion del primer hijo
    @param hijo2: Representacion del segundo hijo
    @return: individuos para la siguiente generacion
    '''
    def steadyState(self, padre1, padre2, hijo1, hijo2):
        siguienteGeneracion = [] #vector que va a pasar a la siguiente genecion
        
        #de acuerdo a los desempenos, se deja al mejor padre como jugadorA, el mejor hijo como jugadorB, el peor padre como jugadorC, y el peor hijo como jugadorD
        if padre1.obtenerFitness() < padre2.obtenerFitness():
            if hijo1.obtenerFitness() < hijo2.obtenerFitness():
                jugadorA = padre1
                jugadorB = hijo1
                jugadorC = padre2
                jugadorD = hijo2
            else:
                jugadorA = padre1
                jugadorB = hijo2
                jugadorC = padre2
                jugadorD = hijo1
        else:
            if hijo1.obtenerFitness() < hijo2.obtenerFitness():
                jugadorA = (padre2)
                jugadorB = (hijo1)
                jugadorC = (padre1)
                jugadorD = (hijo2)
            else:
                jugadorA = (padre2)
                jugadorB = (hijo2)
                jugadorC = (padre1)
                jugadorD = (hijo1)
            
        ganador1 = self.ruleta(jugadorA, jugadorB) #se enfrentan el mejor padre y el mejor hijo
        ganador2 = self.ruleta(jugadorC, jugadorD) #se enfrentan el peor padre y el peor hijo
        
        siguienteGeneracion.append(ganador1) #se agrega el ganador de la primera ruleta
        siguienteGeneracion.append(ganador2) #se agrega el ganador de la segunda ruleta
        
        return siguienteGeneracion