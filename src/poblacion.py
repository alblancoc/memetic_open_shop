from funcionFitness import FuncionFitness
from operadoresGeneticos import OperadoresGeneticos
from Replacement import Reemplazo
from Individual import Individuo
from random import randint
from random import random

'''
Created on Apr 26, 2016

@author: Angie Blanco
'''

class Poblacion(object):
   
    '''
    classdocs
    '''
    def __init__(self, tamano, iteraciones, maquinas, trabajos, entrada, uniforme, generacional):
        self.poblacion = []
        
        self.tamano = tamano
        self.iteraciones = iteraciones
        self.archivo_tiempos = entrada
        self.trabajos = trabajos
        self.maquinas = maquinas
        self.uniforme = uniforme
        
        self.funcionFitness = FuncionFitness(maquinas, trabajos, entrada)
        self.mecanismoReemplazo = Reemplazo( generacional )
        
        self.log = ""
        self.operadores = OperadoresGeneticos()
        print "||---------- MAOS ----------|| \n\n Initializing algorithm..."
        
        print "Building initial population..."
        self.poblacionInicial()
        
        print "Start genetic algorithm...\n"
        self.generaciones()
        
        
        
    '''
    Esta funcion se utiliza para crear la poblacion inicial de manera aleatoria.
    Si el usuario lo escoge, se puede aplicar la heuristica de mejora inicial.
    '''
    def poblacionInicial(self):
        for x in range(self.tamano):
            individuo = [(i + 1) for i in range(self.maquinas * self.trabajos)]
            shuffle(individuo)
            self.poblacion.append( individuo )
            
        self.log += self.fitnessPromedio + "," + self.imprimirMejorIndividuo() + ","
        
        #TODO invocar heuristica
        
        
    
    '''
    Esta funcion se utiliza para llevar a cabo las generaciones del algoritmo genetico 
    de acuerdo a las iteraciones definidas para el algoritmo
    '''
    def generaciones(self):
        
        padres = None #variable para almacenar la pareja de padres desde la cual se obtendran hijos
        hijos_cromosoma = [] #variable donde
        hijos = []
        
        candidatos_nuevos = []
        
        
        for i in range( self.iteraciones ):
            nueva_generacion = []
            
            for j in range(self.tamano / 2):
                if self.uniforme:
                    padres = self.seleccionUniforme()
                else:
                    padres = self.seleccionTorneo()
                
                if random < 0.5:
                    hijos_cromosoma = self.operadores.swapMutation(padres[0], padres[1])
                else:
                    hijos_cromosoma = self.operadores.egde2Crossover(padres[0], padres[1])
                    
                hijos.append( Individuo( hijos_cromosoma[0], self.funcionFitness.calcularFitness( hijos_cromosoma[0] ) ) )
                hijos.append( Individuo( hijos_cromosoma[1], self.funcionFitness.calcularFitness( hijos_cromosoma[1] ) ) )
    
                candidatos_nuevos = self.mecanismoReemplazo.realizarReemplazo(padres[0], padres[1], hijos[0], hijos[1])
                nueva_generacion.append( candidatos_nuevos[0] )
                nueva_generacion.append( candidatos_nuevos[1] )
                
            self.poblacion = None
            self.poblacion = nueva_generacion
       
    '''
    '''        
    def trabajo(m):
        f = int((m - 1) / self.trabajos)
        return f
    
    '''
    '''
    def maquina(n):
        c = n % self.maquinas 
        return c 
        
    '''
    '''    
    def heuristicaMejoraInicial(self, cromosoma):
        
        ultima_tarea = -1
        total_tareas = self.maquinas * self.trabajos
        
        #/Move over all permutation
        for tarea in range( total_tareas ): 
            trabajo_tarea = trabajo( cromosoma[ tarea ] )  #Row from table
            maquina_tarea = maquina( cromosoma[ tarea ] ) #Column from table
            
            for tarea_en_grupo in range (i % self.trabajos):
           
                base = (tarea / self.trabajos);
                base = (base * self.trabajos) + tarea_en_grupo;
                
                trabajo_base = self.trabajo( cromosoma[ base ] )  #Get row
                maquina_base = self.maquina( cromosoma[ base ] ) #Get column
                
                if trabajo_tarea == trabajo_base or maquina_tarea == maquina_base: #If are same both rows and columns
                    ultima_tarea = tarea
                    
                    while True:
                        ultima_tarea += 1
                        successful = True
                        
                        trabajo_ultima = self.trabajo ( cromosoma[ ultima_tarea ] ) #Row from table
                        maquina_ultima = self.maquina( cromosoma[ ultima_tarea ] ) #Column from table
                        
                        for  l in range(tarea % self.trabajos):
                            base = (tarea / self.trabajos);
                            base = (base * self.trabajos) + l
                            
                            trabajo_base = self.trabajo( cromosoma[ base ] )  #Get row
                            maquina_base = self.maquina( cromosoma[ base ] ) #Get column
                            
                            if trabajo_ultima == trabajo_base or maquina_ultima == maquina_base: #If are same both rows and columns
                                successful = False
                                break
          
                        if (not successful) and (ultima_tarea < total_tareas - 1):
                            break
                    
                    valor_mover = cromosoma[ ultima_tarea ]
                    
                    for l in range(ultima_tarea, tarea, -1): 
                        cromosoma[l] = cromosoma[l - 1]
                    
                    cromosoma[tarea] = valor_mover
                    break
        
        return cromosoma
    
    
    '''
    '''
    def seleccionUniforme(self):
        padres = []
        padre1 = randint(0,self.tamano - 1)
        padre2 = randint(0, self.tamano - 1)
            
        while (padre1 == padre2):
            padre2 = randint(0, tamano - 1)
        
        padres.append( self.poblacion[padre1] )
        padres.append( self.poblacion[padre2] )
        
        return padres
    
    
    '''
    '''    
    def seleccionTorneo(self):
        padres = []
        mejor_indice = self.mejorIndividuo()
        
        participante1 = mejor_indice
        participante2 = randint(0, self.tamano - 1)
        participante3 = randint(0, self.tamano - 1)
        participante4 = randint(0, self.tamano - 1)
        
        padre1 = ruleta( self.poblacion[participante1], self.poblacion[participante2])
        padre2 = ruleta( self.poblacion[participante3], self.poblacion[participante4])
        padres.append( ruleta(padre1, padre2) )
    
        participante1 = randint(0, self.tamano - 1)
        participante2 = randint(0, self.tamano - 1)
        participante3 = randint(0, self.tamano - 1)
        participante4 = randint(0, self.tamano - 1)
        
        padre1 = ruleta( self.poblacion[participante1], self.poblacion[participante2])
        padre2 = ruleta( self.poblacion[participante3], self.poblacion[participante4])
        padres.append( ruleta(padre1, padre2) )
    
        return padres 
    
    
    '''
    '''
    def ruleta(self, jugador1, jugador2):
        total = (jugador1.obtenerDesempeno + jugador2.obtenerDesempeno)
        punto = 1 - (jugador1.obtenerDesempeno /total)
        aleatorio = random()
        if punto >= aleatorio:
            ganador = jugador1
        else:
            ganador = jugador2
            
        return ganador
    
    
    '''
    '''
    def fitnessPromedio(self):
        print "promedio"
    
    '''
    '''    
    def mejorIndividuo(self):
        indice = 0
        fitness = self.poblacion[indice].obtenerFitness()
        
        for i in range(1, self.tamano, 1):
            if self.population[i].obtenerFitness() < fitness:
                indice = i
                fitness = self.population[i].obtenerFitness()
        
        return indice
    
    '''
    '''    
    def imprimirMejorIndividuo(self):
        indice = self.mejorIndividuo()
        return self.poblacion[indice]        