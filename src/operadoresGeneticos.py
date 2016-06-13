'''
Created on Apr 26, 2016

@author: Angie Blanco
'''
import random
import copy

class OperadoresGeneticos(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
    #Metodo para aplicar el operador genetico SwapMutation    
    def swapMutation(self, padre1, padre2):
        hijos = []
         
        #Se colocan los cromosomas de los padres en los hijos 
        hijos.append(padre1)
        hijos.append(padre2)
        
        #Se generan los puntos de intercambio de forma aleatoria
        primerPunto = random.randint(0, len(padre1) - 1)
        segundoPunto = random.randint(0, len(padre1) - 1)
        
        #Se verifica que los dos puntos de intercambio no sean los mismos
        while(primerPunto == segundoPunto):
            segundoPunto = random.randint(0, len(padre1) - 1)
        
        #Se cambian las tareas en el cromosoma del hijo 1
        valorTemporal = hijos[0][primerPunto]
        hijos[0][primerPunto] = hijos[0][segundoPunto]
        hijos[0][segundoPunto] = valorTemporal
         
         #Se cambian las tareas en el cromosoma del hijo 2
        valorTemporal = hijos[1][primerPunto]
        hijos[1][primerPunto] = hijos[1][segundoPunto]
        hijos[1][segundoPunto] = valorTemporal 
        
        return hijos
    
    
    #Metodo para aplicar el operador genetico de cruce 2-edge 
    def edge2Crossover(self, padre1, padre2):
        tamano = len( padre1 )
        hijos = []
        tabla = [];
        
        #se inicializa la tabla que va a almacenas las adyacencias
        for i in range(tamano):
            tabla.append( [] )
            
        #Se agregan a la tabla las tareas adyacentes de acuerdo a la permutacion del padre 1
        for i in range(tamano):
            tabla[ padre1[i] - 1].append( padre1[(i + 1) % tamano] )
            tabla[ padre1[i] - 1].append( padre1[(i - 1 + tamano) % tamano] )
         
            
        #se toma el cromosoma del padre 2, y se compran las adjacencias con la tabla obtenida del padre 1
        for i in range(tamano):
            temporal = padre2[ (i + 1) % tamano ]  #se mira la tarea adyacente hacia adelante del indice i
            encontrado = False
            
            for j in range( len( tabla[padre2[i] - 1]) ):
                
                if tabla[ padre2[i] - 1][j] == temporal: #si hay una adyacencia en comun, se marca como negativa
                    encontrado = True
                    cambio = tabla[padre2[i] - 1][j] * (-1)
                    primero = tabla[padre2[i] - 1][0]
                    
                    tabla[ padre2[i] - 1 ][j] = primero
                    tabla[ padre2[i] - 1 ][0] = cambio
            
            if not encontrado: #si no esta la adyacencia en comun, se agrega la tarea a la tabla de adyacencias
                tabla[ padre2[i] - 1 ].append(temporal)
            
            temporal = padre2[ (i - 1 + tamano) % tamano ]  #se mira la tarea adyacente hacia atras del indice i
            encontrado = False
            
            for j in range( len( tabla[padre2[i] - 1] )): 
                if tabla[ padre2[i] - 1][j] == temporal: #si hay una adyacencia en comun, se marca como negativa
                    encontrado = True
                    cambio = tabla[padre2[i] - 1][j] * (-1)
                    primero = tabla[padre2[i] - 1][0]
                    
                    tabla[ padre2[i] - 1 ][j] = primero
                    tabla[ padre2[i] - 1 ][0] = cambio
            
            if not encontrado: #si no esta la adyacencia en comun, se agrega la tarea a la tabla de adyacencias
                tabla[ padre2[i] - 1 ].append(temporal)
        
        
        tabla_ = copy.deepcopy( tabla ) #TODO mejorar clonacion
        hijos.append( self.crossHijo(tabla, tamano) ) #a partir de la tabla de adyacencias se crea el hijo 1
        hijos.append( self.crossHijo(tabla_, tamano) ) #a partir de la tabla de adyacencias se crea el hijo 2
        
        return hijos
    
    
    
    #Apoyo para el operador 2-edge. Usa la tabla de adyacencias y construye el individuo
    def crossHijo(self, tabla, tamano):
        hijo = [None] * tamano
        tarea = random.randint(1, len(tabla) ) #Seleccion aleatoria de la primera tarea
        hijo[0] = tarea #se asigna la primera tarea
        indice = 1 #Define la cantidad de tareas agregadas al hijo
        
        #Mientras no se hayan agregado toras las tareas
        while indice < len(tabla):
            invalido = True
            
            while (invalido):
                #TODO remove current task from their adjacent tasks
                if len( tabla[tarea - 1] ) > 0: #Se revisa si quedan adjacencias
                    if tabla[tarea - 1][0] < 0:  #Si la primera tarea es negativa, se asigna automaticamente
                        enTabla = 0
                    else:
                        enTabla = random.randint(0, len( tabla[tarea - 1] ) - 1) #se escoge aleatoriamente de alguna de las tareas en el arreglo
                
                    nuevaTarea = tabla[tarea - 1][enTabla] #Define cual es la siguiente tarea a procesar
                    tabla[tarea - 1].remove( nuevaTarea ) #Se remueve la tarea asignada de la lista
                    nuevaTarea = abs( nuevaTarea ) #En caso de que sea negativa, se debe colocar en un rango valido
                else:
                    nuevaTarea = random.randint(1, len(tabla))  #Si la tarea ya no tiene mas adyacencias, se busca aleatoriamente una nueva tarea
        
                for i in range(indice): #Verifica si la tarea ya existe en el arreglo
                    if nuevaTarea == hijo[i]: #Si ya xiste, hay que repetir el proceso
                        invalido = True
                        break
                else:
                    invalido = False
                  
                
            tarea = nuevaTarea #La tarea seleccionada en la tabla ahora sera la tarea en la cual se busque la adyacencia
            hijo[indice] = tarea #Se agrega la tarea seleccionada al cromosoma del hijo
            indice += 1 #Se mueve en el cromosoma para asignar la siguiente tarea
        
        #una vez construido todo el hijo, se acaba el metodo y se retorna el cromosoma    
        return hijo
    
   
   
'''
operadores = OperadoresGeneticos()
fat1 = [1,2,3,4,5,6,7,8,9]
fat2 = [1,3,5,7,9,8,6,4,2]

sons = operadores.swapMutation(fat1, fat2)
print "Mutation 1"
print sons[0]
print sons[1]

sons = operadores.swapMutation(fat1, fat2)
print "Mutation 2"
print sons[0]
print sons[1]

sons = operadores.edge2Crossover(sons[0], sons[1])
print "Cross 1"
print sons[0]
print sons[1]
'''