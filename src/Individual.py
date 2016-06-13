'''
Created on Apr 26, 2016

@author: Angie Blanco
'''

class Individuo(object):
    '''
    classdocs
    '''
    
    def __init__(self, genotipo, fitness):
        '''
        Constructor
        '''
        self.genotipo = genotipo
        self.fenotipo = genotipo
        self.fitness = fitness
        
    def obtenerFenotipo(self):
        return self.fenotipo
    
    def obtenerGenotipo(self):
        return self.genotipo
    
    def definirFitness(self, fitness):
        self.fitness = fitness
        
    def obtenerFitness(self):
        return int(self.fitness)
    
    def __repr__(self, *args, **kwargs):
        return ( str( self.genotipo ) + ", " + str( self.fitness ))