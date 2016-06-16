'''
Created on Apr 26, 2016

@author: Angie Blanco
'''

class Individuo(object):
    
    '''
    Constructor de la clase
    @param genotipo:
    @param fitness: 
    '''
    def __init__(self, genotipo, fitness):
        self.genotipo = genotipo
        self.fenotipo = genotipo
        self.fitness = fitness
       
        
    '''
    '''    
    def obtenerFenotipo(self):
        return self.fenotipo
    
    
    '''
    '''
    def obtenerGenotipo(self):
        return self.genotipo
    
    
    '''
    @param fitness: 
    '''
    def definirFitness(self, fitness):
        self.fitness = fitness
      
     
    '''
    '''   
    def obtenerFitness(self):
        return int(self.fitness)
    
    
    '''
    @param cromosoma: 
    '''
    def cambiarGenotipo(self, cromosoma):
        self.fenotipo = genotipo
        self.genotipo = genotipo
    
    
    '''
    '''
    def __repr__(self, *args, **kwargs):
        return ( str( self.genotipo ) + "," + str( self.fitness ))