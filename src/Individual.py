'''
Created on Apr 26, 2016

@author: carlosandressierra
'''

class Individual(object):
    '''
    classdocs
    '''
    
    def __init__(self, genotype, fitness):
        '''
        Constructor
        '''
        self.genotype = genotype
        self.fenotype = genotype
        self.fitness = fitness
        
    def obtainFenotype(self):
        return self.fenotype
    
    def obtainGenotype(self):
        return self.genotype
    
    def defineFitness(self, fitness):
        self.fitness = fitness
        
    def obtainFitness(self):
        return self.fitness
    
    
    def __repr__(self, *args, **kwargs):
        return ("Genotype = " + self.genotype + "\tFitness = " + self.fitness) 
        