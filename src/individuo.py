'''
Clase que determina la representacion del individuo dentro del algoritmo

Created on Apr 26, 2016

@author: Angie Blanco
'''

class Individuo(object):
    
    '''
    Constructor de la clase
    @param genotipo: Permutacion sin repeticion que determina el orden de las tareas
    @param fitness: Makespan de acuerdo al orden de tareas definido en el fenotipo
    '''
    def __init__(self, genotipo, fitness):
        self.genotipo = genotipo #cromosoma
        self.fenotipo = genotipo #para este problema, el genotipo y el fenotipo se representan igual
        self.fitness = fitness #desempno del individuo
       
        
    '''
    Este metodo se utiliza para obtener la representacion fenotipica del individuo
    @return: fenotipo
    '''    
    def obtenerFenotipo(self):
        return self.fenotipo
    
    
    '''
    Este metodo se utiliza para obtener la representacion genotipica del individuo
    @return: genotipo
    '''
    def obtenerGenotipo(self):
        return self.genotipo
    
    
    '''
    Este metodo se usa para mofidicar el makespan del individuo, cuando se ha recalculado por cambios en el genotipo
    @param fitness: makespan calculado para el individuo
    '''
    def definirFitness(self, fitness):
        self.fitness = fitness
      
     
    '''
    Este metodo se usa para obtener el makespan del individuo
    @return: fitness (desempeno) del individuo
    '''   
    def obtenerFitness(self):
        return int(self.fitness)
    
    
    '''
    Este metodo se usa para modificar el cromosoma que representa al individuo
    @param cromosoma: Permutacion sin repeticion que determina el orden de las tareas
    '''
    def cambiarGenotipo(self, cromosoma):
        self.fenotipo = genotipo #se reemplaza el feonotipo
        self.genotipo = genotipo #se reemplaza el genotipo
    
    
    '''
    Metodo que se usa para imprimir la informacion del invididuo
    @return: informacion para imprimir
    '''
    def __repr__(self, *args, **kwargs):
        return ( str( self.genotipo ) + "," + str( self.fitness ))