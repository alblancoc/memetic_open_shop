'''
Created on Apr 26, 2016

@author: carlosandressierra
'''
from random import random

class Replacement(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
    
        
    
    def generacional(self, father1, father2, son1, son2):
        winners = []
        winners.append(son1)
        winners.append(son2)
        
        return winners
    
    
    
    def ruleta(self, player1, player2):
        desempeno1 = player1.fitness 
        desempeno2 = player2.fitness
        total = (desempeno1+desempeno2)
        punto = 1 - (desempeno1/total)
        aleatorio = random()
        if punto >= aleatorio:
            winner = player1
        else:
            winner = player2
            
        return winner
    
    def steadyState(self, padre1, padre2, hijo1, hijo2):
        winners = []
        desempenop1 = padre1.fitness 
        desempenop2 = padre2.fitness
        desempenoh1 = hijo1.fitness
        desempenoh2 = hijo2.fitness
        if desempenop1 >= desempenop2:
            if desempenoh1 >= desempenoh2:
                jugadora = (padre1)
                jugadorb = (hijo1)
                jugadorc = (padre2)
                jugadord = (hijo2)
            else:
                jugadora = (padre1)
                jugadorb = (hijo2)
                jugadorc = (padre2)
                jugadord = (hijo1)
        else:
            if desempenoh1 >= desempenoh2:
                jugadora = (padre2)
                jugadorb = (hijo1)
                jugadorc = (padre1)
                jugadord = (hijo2)
            else:
                jugadora = (padre2)
                jugadorb = (hijo2)
                jugadorc = (padre1)
                jugadord = (hijo1)
            
        ganador1 = ruleta(jugadora,jugadorb)
        ganador2 = ruleta(jugadorc,jugadord)
        
        winners.append(ganador1)
        winners.append(ganador2)
        
        return winners
    
    
    