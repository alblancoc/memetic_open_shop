'''
En esta clase se definen los operadores geneticos que se usaran en el algoritmo genetico. 
Se define un operador para el cruce y otro para la mutacion.

Created on Apr 26, 2016

@author: Angie Blanco
'''
import random
import copy

class OperadoresGeneticos(object):
    
    '''
    Constructor de la clase
    '''
    def __init__(self):
        '''
        Este constructor no hace nada mas
        '''
       
        
    '''
    Este metodo representa la dinamica del operador de mutacion "SwapMutation". Se reciben los padres y se generan los cromosomas de los hijos.
    @param padre1: Cromosoma del primer padre
    @param padre2: Cromosoma del segundo padre 
    @return: cromosomas de los dos hijos resultantes
    '''    
    def swapMutation(self, padre1, padre2):
        hijos = [] #vector donde se almacenan los hijos
         
        #Se colocan los cromosomas de los padres en los hijos 
        hijos.append(padre1) 
        hijos.append(padre2)
        
        #Se generan los puntos de intercambio de forma aleatoria
        primerPunto = random.randint(0, len(padre1) - 1)
        segundoPunto = random.randint(0, len(padre1) - 1)
        
        #Se verifica que los dos puntos de intercambio no sean los mismos
        while(primerPunto == segundoPunto):
            segundoPunto = random.randint(0, len(padre1) - 1)
        
        #Se cambian las tareas en el cromosoma del primer hijo (posicion 0)
        valorTemporal = hijos[0][primerPunto]
        hijos[0][primerPunto] = hijos[0][segundoPunto]
        hijos[0][segundoPunto] = valorTemporal
         
         #Se cambian las tareas en el cromosoma del segundo hijo (posicion 1)
        valorTemporal = hijos[1][primerPunto]
        hijos[1][primerPunto] = hijos[1][segundoPunto]
        hijos[1][segundoPunto] = valorTemporal 
        
        return hijos #se retornan los cromosomas obtenidos de los hijos
    
    
    '''
    Este metodo representa la dinamica del operador de cruce "2-edge". Se reciben los padres y se generan los cromosomas de los hijos.
    @param padre1: Cromosoma del primer padre
    @param padre2: Cromosoma del segundo padre 
    @return: cromosomas de los dos hijos resultantes
    '''  
    def edge2Crossover(self, padre1, padre2):
        tamano = len( padre1 )
        hijos = []
        tabla = []
        
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
            encontrado = False #inicialmente se asume que no existe una adyacencia, y cuando se encuentra se desencadenan las reglas de marcacion logica
            
            for j in range( len( tabla[padre2[i] - 1] )): 
                if tabla[ padre2[i] - 1][j] == temporal: #si hay una adyacencia en comun, se marca como negativa
                    encontrado = True
                    cambio = tabla[padre2[i] - 1][j] * (-1)
                    primero = tabla[padre2[i] - 1][0]
                    
                    #se reorganizan las tareas, de tal manera que las negativas pasen a la primera posicion
                    tabla[ padre2[i] - 1 ][j] = primero
                    tabla[ padre2[i] - 1 ][0] = cambio
            
            
            if not encontrado: #si no esta la adyacencia en comun, se agrega la tarea a la tabla de adyacencias
                tabla[ padre2[i] - 1 ].append(temporal)
        
        
        tabla_ = copy.deepcopy( tabla ) #Se hace una copia de la tabla para procesar el hijo 2
        hijos.append( self.crossHijo(tabla, tamano) ) #a partir de la tabla de adyacencias se crea el hijo 1
        hijos.append( self.crossHijo(tabla_, tamano) ) #a partir de la tabla de adyacencias se crea el hijo 2
        
        return hijos #se retornan los hijos obtenidos
    
    
    '''
    Este metodo es un auxiliar para el operador de cruce 2-edge. En este caso, se recibe la tabla de adyacencias y se crea el cromosoma del hijo.
    @param tabla: tabla de adyacencias
    @param tamano: cantidad de tareas en la permutacion
    @return: cromosoma del nuevo hijo
    '''
    def crossHijo(self, tabla, tamano):
        hijo = [None] * tamano #se crea el vector donde se almacena el orden de tareas del hijo
        tarea = random.randint(1, len(tabla) ) #Seleccion aleatoria de la primera tarea
        hijo[0] = tarea #se asigna la primera tarea
        indice = 1 #Define la cantidad de tareas agregadas al hijo
        
        #Mientras no se hayan agregado toras las tareas
        while indice < len(tabla):
            invalido = True #por defecto se considera invalido, ya que se busca encontrar el caso donde no lo sea
            
            while (invalido):
                if len( tabla[tarea - 1] ) > 0: #Se revisa si quedan adjacencias
                    if tabla[tarea - 1][0] < 0:  #Si la primera tarea es negativa, se asigna automaticamente
                        enTabla = 0 #al ser negativa, la posicion en la que se encuentra s la inicial
                    else:
                        enTabla = random.randint(0, len( tabla[tarea - 1] ) - 1) #se escoge aleatoriamente de alguna de las tareas en el arreglo
                
                    nuevaTarea = tabla[tarea - 1][enTabla] #Define cual es la siguiente tarea a procesar
                    tabla[tarea - 1].remove( nuevaTarea ) #Se remueve la tarea asignada de la lista
                    nuevaTarea = abs( nuevaTarea ) #En caso de que sea negativa, se debe colocar en un rango valido
                else:
                    nuevaTarea = random.randint(1, len(tabla))  #Si la tarea ya no tiene mas adyacencias, se busca aleatoriamente una nueva tarea
        
                for i in range(indice): #Verifica si la tarea ya existe en el arreglo
                    if nuevaTarea == hijo[i]: #Si ya existe, hay que repetir el proceso
                        invalido = True
                        break
                else:
                    invalido = False #no es necesario repetir el proceso
                  
                
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