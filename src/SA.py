from funcionFitness import FuncionFitness
import random 
from math import exp
from individuo import  Individuo
import copy

class RecocidoSimulado(object):
    
    '''
    Constructor de la clase
    '''
    def __init__(self, vecinos_, funcionFitness_):
        self.vecinos = vecinos_
        self.funcionFitness = funcionFitness_
       
        
    '''
    
    ''' 
    def cambiar(self, actual, vecino, temperatura):
        delta = vecino.obtenerFitness() - actual.obtenerFitness() 
        
        if delta < 0:
            return vecino
        else:
            prob = exp(-delta/temperatura)
            if random.random() < prob:
                return vecino
            else:
                return actual
    
    
    '''
    '''
    def actualizarTemperatura(self, temperatura):
        temperatura = temperatura * 0.8
        return temperatura
       
        
    '''
    '''    
    def vecindario(self, actual):
        vecindario_ = []
        
        for i in range( self.vecinos ):
            cromosoma_ = copy.deepcopy(  actual.obtenerGenotipo() )
            punto = random.randint(0, len( cromosoma_ ) - 2)
            
            temp = cromosoma_[punto]
            cromosoma_[punto] = cromosoma_[punto + 1]
            cromosoma_[punto + 1] = temp
            
            vecindario_.append( Individuo(cromosoma_, self.funcionFitness.calcularFitness(cromosoma_)) )
        
        return vecindario_
    
    def vecindario2(self, actual):
        vecindario_ = []
        
        for i in range( self.vecinos ):
            cromosoma_ = copy.deepcopy(  actual.obtenerGenotipo() )
            punto1 = random.randint(0, len( cromosoma_ ) - 1)
            punto2 = random.randint(0, len( cromosoma_ ) - 1)
            temp = cromosoma_[punto1]
            cromosoma_[punto1] = cromosoma_[punto2]
            cromosoma_[punto2] = temp
            
            punto1 = random.randint(0, len( cromosoma_ ) - 1)
            punto2 = random.randint(0, len( cromosoma_ ) - 1)
            temp = cromosoma_[punto1]
            cromosoma_[punto1] = cromosoma_[punto2]
            cromosoma_[punto2] = temp
            
            vecindario_.append( Individuo(cromosoma_, self.funcionFitness.calcularFitness(cromosoma_)) )
        
        return vecindario_
    
    
    def ejecutar(self, actual, temperatura):
        
        while temperatura > 1:
            vecindario_ = self.vecindario2(actual)
            for i in range( len( vecindario_ ) ):
                actual = self.cambiar(actual, vecindario_[i], temperatura)
                temperatura = self.actualizarTemperatura(temperatura)
            
        return actual


'''
chromosome = [i for i in range(1, 101, 1)]
random.shuffle( chromosome )
funcionFitness = FuncionFitness(10, 10, "a_10_1.txt")
individual = Individuo(chromosome, funcionFitness.calcularFitness(chromosome))
print individual

sa = RecocidoSimulado(10, funcionFitness)
newIndividual = sa.ejecutar(individual, 1000)

print newIndividual
'''