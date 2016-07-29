from funcionFitness import FuncionFitness
from operadoresGeneticos import OperadoresGeneticos
from reemplazo import Reemplazo
from individuo import Individuo
from random import randint
from random import random
from random import shuffle
from SA import RecocidoSimulado

'''
Created on Apr 26, 2016

@author: Angie Blanco
'''

class Poblacion(object):
   
    '''
    Constructor de la clase
    @param tamano:
    @param iteraciones:
    @param maquinas:
    @param trabajos:
    @param entrada:
    @param uniforme:
    @param generacional:
    @param heuristica: 
    '''
    def __init__(self, tamano, iteraciones, maquinas, trabajos, entrada, uniforme, generacional, heuristica):
        self.poblacion = []
        
        self.tamano = tamano
        self.iteraciones = iteraciones
        self.archivo_tiempos = entrada
        self.trabajos = trabajos
        self.maquinas = maquinas
        self.uniforme = uniforme
        
        self.funcionFitness = FuncionFitness(maquinas, trabajos, entrada)
        self.mecanismoReemplazo = Reemplazo( generacional )
        self.recocidoSimulado = RecocidoSimulado( 10, self.funcionFitness )
        
        self.log = ""
        self.operadores = OperadoresGeneticos()
        
        print "||---------- MAOS ----------|| \n\n Initializing algorithm..."
        
        print "Building initial population..."
        self.poblacionInicial(heuristica)
        
        print "Start genetic algorithm..."
        self.generaciones()
        
        self.log += (",%.2f,") % self.fitnessPromedio()
        self.log += "" + str ( self.imprimirMejorIndividuo() )
        
        
        
    '''
    Esta funcion se utiliza para crear la poblacion inicial de manera aleatoria.
    Si el usuario lo escoge, se puede aplicar la heuristica de mejora inicial.
    @param heuristica:
    '''
    def poblacionInicial(self, heuristica):
        for contador in range(self.tamano):
            individuo = [(i + 1) for i in range(self.maquinas * self.trabajos)]
            shuffle(individuo)
            nuevoIndividuo = Individuo(individuo, self.funcionFitness.calcularFitness( individuo )  ) 
            self.poblacion.append( nuevoIndividuo )
            
        self.log += ("%.2f,") % self.fitnessPromedio()
        self.log += "" + str ( self.imprimirMejorIndividuo() ) 
        
        if heuristica:
            for i in range( len( self.poblacion ) ):
                individuo = self.heuristicaMejoraInicial( self.poblacion[i].obtenerGenotipo() )
                self.poblacion[i].definirFitness( self.funcionFitness.calcularFitness( individuo ) ) 
                
            self.log += (",%.2f,") % self.fitnessPromedio()
            self.log += "" + str ( self.imprimirMejorIndividuo() )
        
        
    
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
                
                if random < 0.3:
                    hijos_cromosoma = self.operadores.swapMutation(padres[0].obtenerGenotipo(), padres[1].obtenerGenotipo())
                else:
                    hijos_cromosoma = self.operadores.edge2Crossover(padres[0].obtenerGenotipo(), padres[1].obtenerGenotipo())
                 
                hijos = []    
                hijos.append( Individuo( hijos_cromosoma[0], self.funcionFitness.calcularFitness( hijos_cromosoma[0] ) ) )
                hijos.append( Individuo( hijos_cromosoma[1], self.funcionFitness.calcularFitness( hijos_cromosoma[1] ) ) )
    
                candidatos_nuevos = self.mecanismoReemplazo.realizarReemplazo(padres[0], padres[1], hijos[0], hijos[1])
                
                nueva_generacion.append( candidatos_nuevos[0] )
                nueva_generacion.append( candidatos_nuevos[1] )
                #nueva_generacion.append( self.recocidoSimulado.ejecutar( candidatos_nuevos[0], 10) )
                #nueva_generacion.append( self.recocidoSimulado.ejecutar( candidatos_nuevos[1], 10) )
                
            self.poblacion = None
            self.poblacion = nueva_generacion
    
       
    '''
    Este metodo se utiliza para determinar a que trabajo pertenece una tarea dentro de la permutacion
    @param m:
    @return: 
    '''        
    def trabajo(self, n):
        t = int((n - 1) / self.trabajos)
        return t
    
    
    '''
    Este metodo se utiliza para determinar a que maquina pertenece una tarea dentro de la permutacion
    @param n:
    @return: 
    '''
    def maquina(self, n):
        m = n % self.maquinas 
        return m 
        
        
    '''
    @param cromosoma:
    @return: 
    '''    
    def heuristicaMejoraInicial(self, cromosoma):
        
        ultima_tarea = -1
        total_tareas = self.maquinas * self.trabajos
        
        #/Move over all permutation
        for tarea in range( total_tareas - 1 ): 
            trabajo_tarea = self.trabajo( cromosoma[ tarea ] )  #Row from table
            maquina_tarea = self.maquina( cromosoma[ tarea ] ) #Column from table
            
            for tarea_en_grupo in range (tarea % self.trabajos):
           
                base = (tarea / self.trabajos)
                base = (base * self.trabajos) + tarea_en_grupo
                
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
          
                        if (successful) or (ultima_tarea >= total_tareas - 1):
                            break
                    
                    valor_mover = cromosoma[ ultima_tarea ]
                    
                    for l in range(ultima_tarea, tarea, -1): 
                        cromosoma[l] = cromosoma[l - 1]
                    
                    cromosoma[tarea] = valor_mover
                    break
        
        return cromosoma
    
    
    '''
    Este metodo representa la seleccion de padres mediante un mecanismo uniforme, en donde el fitness no es tenido en cuenta
    @return: 
    '''
    def seleccionUniforme(self):
        padres = []
        padre1 = randint(0,self.tamano - 1)
        padre2 = randint(0, self.tamano - 1)
            
        while (padre1 == padre2):
            padre2 = randint(0, self.tamano - 1)
        
        padres.append( self.poblacion[padre1] )
        padres.append( self.poblacion[padre2] )
        
        return padres
    
    
    '''
    @return: 
    '''    
    def seleccionTorneo(self):
        padres = []
        mejor_indice = self.mejorIndividuo()
        
        participante1 = mejor_indice
        participante2 = randint(0, self.tamano - 1)
        participante3 = randint(0, self.tamano - 1)
        participante4 = randint(0, self.tamano - 1)
        
        padre1 = self.ruleta( self.poblacion[participante1], self.poblacion[participante2])
        padre2 = self.ruleta( self.poblacion[participante3], self.poblacion[participante4])
        padres.append( self.ruleta(padre1, padre2) )
    
        participante1 = randint(0, self.tamano - 1)
        participante2 = randint(0, self.tamano - 1)
        participante3 = randint(0, self.tamano - 1)
        participante4 = randint(0, self.tamano - 1)
        
        padre1 = self.ruleta( self.poblacion[participante1], self.poblacion[participante2])
        padre2 = self.ruleta( self.poblacion[participante3], self.poblacion[participante4])
        padres.append( self.ruleta(padre1, padre2) )
        
        return padres 
    
    
    '''
    @param jugador1:
    @param jugador2:
    @return: 
    '''
    def ruleta(self, jugador1, jugador2):
        total = (jugador1.obtenerFitness() + jugador2.obtenerFitness())
        punto = 1 - (jugador1.obtenerFitness() /total)
        aleatorio = random()
        if punto >= aleatorio:
            ganador = jugador1
        else:
            ganador = jugador2
            
        return ganador
    
    
    '''
    Este metodo se utiliza para calcular el fitness promedio de la poblacion en un isntante de tiempo dato
    @return: fitmess promedio en la poblacion
    '''
    def fitnessPromedio(self):
        fitnessProm = 0
        
        for individuo in  self.poblacion: #se recorren todos los individuos
            fitnessProm += individuo.obtenerFitness() #se guarda en una variable acumuladora todo los fitness
        
        fitnessProm /= self.tamano #se divide el fitness acumulado por la cantidad de individuos de la poblacion, para ai obtener el promedio
        
        return fitnessProm #retorna el promedio
        
    
    '''
    En este metodo se comparan los fitness de todos los individuos y se retorna la posicion en la cual se encuentra el individuo con el mejor fitness
    @return: indice del mejor individuo
    '''    
    def mejorIndividuo(self):
        indice = 0 #se asume que el primer individuo temporalmente es el mejor
        fitness = self.poblacion[indice].obtenerFitness() #se toma el fitness del primer individuo como referencia de comparacion
        
        for i in range(1, self.tamano, 1): #se recorren todos los individuos de la poblacion despues del primero
            #se compara el fitness del individuo con el mejor fitness encontrado hasta el momento
            if self.poblacion[i].obtenerFitness() < fitness:  #si se ha encontrado un mejor fitness
                indice = i  #se cambia el indice del mejor al individuo que se ha encontrado con mejor fitness
                fitness = self.poblacion[i].obtenerFitness() #se actualiza el valor de referencia del fitness
        
        return indice #se retorna el indice del mejor individuo encontrado
    
    
    '''
    Este metodo se utiliza para obtener la informacion del mejor individuo en la iteracion en la que se invoque
    @return: mejor individuo
    '''    
    def imprimirMejorIndividuo(self):
        indice = self.mejorIndividuo() #Se busca el indice en el cual esta el mejor individup
        return self.poblacion[indice] #Se retorna el individuo en el indice encontrado    
    
    
    '''
    Este metodo simplemente retorna el log en el que guarda la informacion que se saque de la ejecucion del algoritmo
    @return: log de la ejecucion
    '''
    def generarLog(self):
        return self.log
    
    
'''
poblacion = Poblacion(10, 10, 4, 4, "a_4_1.txt", True, True)
cromosoma = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print cromosoma
poblacion.heuristicaMejoraInicial(cromosoma)
print cromosoma
'''