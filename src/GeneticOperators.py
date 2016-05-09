'''
Created on Apr 26, 2016

@author: carlosandressierra
'''
import random
import copy

class GeneticOperators(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def swapMutation(self, father1, father2):
        sonsChromosomes = []
         
        sonsChromosomes.append(father1)
        sonsChromosomes.append(father2)
        
        firstPoint = random.randint(0, len(father1) - 1)
        secondPoint = random.randint(0, len(father1) - 1)
        
        while(firstPoint == secondPoint):
            secondPoint = random.randint(0, len(father1) - 1)
        
        tempValue = sonsChromosomes[0][firstPoint]
        sonsChromosomes[0][firstPoint] = sonsChromosomes[0][secondPoint]
        sonsChromosomes[0][secondPoint] = tempValue
         
        tempValue = sonsChromosomes[1][firstPoint]
        sonsChromosomes[1][firstPoint] = sonsChromosomes[1][secondPoint]
        sonsChromosomes[1][secondPoint] = tempValue 
        
        return sonsChromosomes
    
    
    def crossover(self, father1, father2):
        size = len( father1 )
        sonsChromosomes = []
        table = [];
        
        for i in range(size):
            table.append( [] )
            
        for i in range(size):
            table[ father1[i] - 1].append( father1[(i + 1) % size] )
            table[ father1[i] - 1].append( father1[(i - 1 + size) % size] )
            
        
        for i in range(size):
            tempValue = father2[ (i + 1) % size ]
            find = False
            
            for j in range( len( table[father2[i] - 1]) ):
                
                if table[ father2[i] - 1][j] == tempValue:
                    find = True
                    tempChange = table[father2[i] - 1][j] * (-1)
                    tempFirst = table[father2[i] - 1][0]
                    
                    table[ father2[i] - 1 ][j] = tempFirst
                    table[ father2[i] - 1 ][0] = tempChange
            
            if not find:
                table[ father2[i] - 1 ].append(tempValue)
            
            tempValue = father2[ (i - 1 + size) % size ] 
            find = False
            
            for j in range( len( table[father2[i] - 1] )): 
                if table[ father2[i] - 1][j] == tempValue:
                    find = True
                    tempChange = table[father2[i] - 1][j] * (-1)
                    tempFirst = table[father2[i] - 1][0]
                    
                    table[ father2[i] - 1 ][j] = tempFirst
                    table[ father2[i] - 1 ][0] = tempChange
            
            if not find:
                table[ father2[i] - 1 ].append(tempValue)
        
        table_ = copy.deepcopy( table ) #TODO improve clonation
        sonsChromosomes.append( self.crossSon(table, size) )
        
        sonsChromosomes.append( self.crossSon(table_, size) )
        
        return sonsChromosomes
    
    
    
    def crossSon(self, table_copy, permutation_size):
        son = [None] * permutation_size
        task = random.randint(1, len(table_copy) ) #Seleccion aleatoria de la primera tarea
        son[0] = task #se asigna la primera tarea
        indexSon = 1 #Define la cantidad de tareas agregadas al hijo
        
        #Mientras no se hayan agregado toras las tareas
        while indexSon < len(table_copy):
            invalid = True
            
            while (invalid):
                #TODO remove current task from their adjacent tasks
                if len( table_copy[task - 1] ) > 0: #Se revisa si quedan adjacencias
                    if table_copy[task - 1][0] < 0:  #Si la primera tarea es negativa, se asigna automaticamente
                        inTable = 0
                    else:
                        inTable = random.randint(0, len( table_copy[task - 1] ) - 1) #se escoge aleatoriamente de alguna de las tareas en el arreglo
                
                    newTask = table_copy[task - 1][inTable] #Define cual es la siguiente tarea a procesar
                    table_copy[task - 1].remove( newTask ) #Se remueve la tarea asignada de la lista
                    newTask = abs( newTask ) #En caso de que sea negativa, se debe colocar en un rango valido
                else:
                    newTask = random.randint(1, len(table_copy))  #Si la tarea ya no tiene mas adyacencias, se busca aleatoriamente una nueva tarea
        
                for i in range(indexSon): #Verifica si la tarea ya existe en el arreglo
                    if newTask == son[i]: #Si ya xiste, hay que repetir el proceso
                        invalid = True
                        break
                else:
                    invalid = False
                  
                
            task = newTask
            son[indexSon] = task
            indexSon += 1
            
        return son
    
   

operators = GeneticOperators()
fat1 = [1,2,3,4,5,6,7,8,9]
fat2 = [1,3,5,7,9,8,6,4,2]

sons = operators.swapMutation(fat1, fat2)
print "Mutation 1"
print sons[0]
print sons[1]

sons = operators.swapMutation(fat1, fat2)
print "Mutation 2"
print sons[0]
print sons[1]


sons = operators.crossover(sons[0], sons[1])
print "Cross 1"
print sons[0]
print sons[1]
