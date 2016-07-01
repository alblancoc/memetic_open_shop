import sys
import time

'''
Esta clase representa la medida de desempeno de los individuos en el algoritmo, calculando el makespan en una simulacion basada en eventos

Created on Apr 26, 2016

@author: Angie Blanco
'''
class FuncionFitness(object):
    
    '''
    Constructor de la clase. Recibe la cantidad de maquinas y trabajos, y el archivo donde se almacena la matriz de tiempos correspondiente
    @param maquinas: cantidad de maquinas de la simulacion
    @param trabajos: cantidad de trabajos de la simulacion
    @param archivo_tiempos: archivo con matriz de tiempos
    '''
    def __init__(self, maquinas, trabajos, archivo_tiempos):
        self.maquinas = maquinas #cantidad de maquinas
        self.trabajos = trabajos #cantidad de trabajos 
        self.tareas = [] #vector de tareas definido por trabajos y maquinas
        self.tabla_tiempos = [] #tabla de tiempos
        
        with open(archivo_tiempos, "r") as tiempos: #se lee el archivo de tiempos con la funcion "open"
            contenido = tiempos.readlines() #se agrega todo el contenido del archivo a una variable 

        for linea in contenido: #Se toma cada una de las lineas en el contenido
            linea = linea.replace(' \n', '').split(" ") #para la linea, se dividen los numeros por el espacio, y se ajusta el salto de la linea
            
            linea_ = [] #se crea un vector para almacenar los tiempos de cada linea
            for n in linea: #se toma cada tiempo de la linea
                linea_.append(int(n))  #se agrega el tiempo al vector
            
            self.tabla_tiempos.append(linea_) #se agrega el vector de tiempos de la linea, a la tabla de tiempos

    
    '''
     Metodo utilizado para definir el vector de tareas en terminos de trabajo y maquina
     @param individuo: cromosoma del individuo con al permutacion de tareas
    '''    
    def iniciar(self, individuo):
        #se inicializa el vector de tareas con respecto a la cantidad de tareas en el cromosoma del individuo
        for i in range(self.trabajos * self.maquinas): #Se crea el vector de tareas para la simulacion
            self.tareas.append( [] )
        
        for i in range( len( individuo ) ): #cada tarea se guarga en un vector de dos posiciones: trabajo y maquina
            trabajo = (individuo[i] - 1) / self.trabajos; #se obtiene el trabajo correspondiente a la tarea
            maquina = (individuo[i] - 1) % self.maquinas; #se obtiene la ,aquina correspondiente a la tarea
            
            self.tareas[i].append( trabajo ); #se agrega el trabajo a la tarra correspondiente
            self.tareas[i].append( maquina ); #se agrega la maquin a la tarea correspondiente
    
    
    '''
    Este metodo se utiliza para definir cual es el siguiente tiempo en el cual ocurre un evento importante. 
    @param tiempos: Vector de tiempos de terminacion de tareas en las maquinas
    @return: tiempo del siguiente evento en la simulacion
    '''
    def siguiente_tiempo(self, tiempos):
        tiempo = 0
        
        for i in range( len(tiempos) ): #se recorre el vector de tiempos de las maquinas
            if tiempos[i] != 0: #se tienen en cuenta los tiempos que son diferentes de cero, puesto que son donde las maquinas van a quedar libres si estan ocupadas
                tiempo = tiempos[i] if tiempo == 0 else (tiempos[i] if tiempos[i] < tiempo else tiempo) #se verifica si hay un tiempo mayor a cero, y de ser asi se coloca el minimo tiempo diferente de certo en el vector de tiempos
            
        return tiempo
    
    
    '''
    Metodo para calcular el makespan simulando el sistema open-shop de acuerdo al orden de tareas establecido en el individuo
    @param individuo: representacion genotipica del individuo
    @return: fitness del individuo
    '''
    def calcularFitness_eventos(self, individuo):
        self.tareas = [] #se inicializa el vector de tareas
        self.iniciar(individuo) #se asignan las tareas de acuerdo al orden de operaciones definido en el individuo
        
        tiempo_final = [0 for i in range(self.maquinas)] #se inicializa el vector de tiempos de maquinas en 0
        trabajos_proceso = [False for i in range(self.trabajos)] #se define un vector para saber si cada proceso tiene una tarea en ejecucion (True) o no (False)
        maquinas_procesando = [(-1) for i in range(self.maquinas)] #se define un vector para saber si la maquina esta procesando una tarea (numero del proceso) o no (-1)
        
        tareas_terminadas = 0 #cantidad de tareas terminadas
        tiempo = 1 #tiempo inicial de la simulacion
        total_tareas = self.maquinas * self.trabajos #se define la cantidad total de tareas a procesar como la multiplicacion de trabajos por maquinas
        
        while tareas_terminadas < total_tareas: #mientras no se hayan procesado todas las tareas
            
            #como se debe respetar la presedencia en las tareas, se marcan los trabajos y maquinas de tareas que no pueden ser procesadas por alguna restriccion, para que no se asignen tareas mas adelante en el cromosoma
            # 0 para maquinas o trabajos pasados, 0 para maquinas o trabajos validas para asignar la tarea
            maquinas_pasadas = [0 for i in range( self.maquinas )] #se usa un vector para marcar las maquinas que estan presentes en tareas que no se pueden procesar
            #trabajos_pasados  = [0 for i in range( self.trabajos )] #se usa un vector para marcar los trabajos que estan presentes en tareas que no se pueden procesar
            
            #se revisa si alguna tarea fue terminada
            terminada = False
            
            for i in range(self.maquinas): #se pregunta en cada una de las maquinas
                if maquinas_procesando[i] == (-1): #se verifica que la maquina este disponible
                    
                    trabajos_pasados  = [0 for j in range( self.trabajos )] #al comenzar a preguntar por tareas disponibles, se inicialica el vector de trabajos para marcar
                    
                    if maquinas_pasadas[i] == 0: #si la maquina no ha sido marcada por presedencia de tareas, se puede buscar una tarea a asignar
                        
                        for k in range(total_tareas): #se recorren todo el vector de tareas
                            if self.tareas[k][0] >= 0: #se verifica si las tareas no han sido procesadas. Las tareas procesadas se marcan con -2 en el vector.
                                
                                if self.tareas[k][1] == i: #se verifica que si la tarea k corresponde a la maquina i
                                    if (not trabajos_proceso[ self.tareas[k][0] ]) and trabajos_pasados[ self.tareas[k][0] ] == 0: #se verifica si el trabajo esta disponible
                                        #se asigna la tarea 
                                        maquinas_procesando[i] = self.tareas[k][0] #se define en la maquina el trabajo que se esta realizando a partir de la tarea asignada
                                        trabajos_proceso[ maquinas_procesando[i] ] = True #se marca el trabajo como en proceso de alguna de sus tareas
                                        
                                        tiempo_final[i] = tiempo + self.tabla_tiempos[ self.tareas[k][0] ][ self.tareas[k][1] ] - 1 #se asigna el tiempo de terminacion de la tarea en la maquina
                                        self.tareas[k][0] = self.tareas[k][1] = -2 # -1 es marca para las maquinas, -2 para las tareas ya procesadas
                                        break #como ya se asigno una tarea ya no se necesita buscar en mas
                                    else:
                                        maquinas_pasadas[i] = 1 #aunque la tarea corresponde a la maquina i, por alguna restriccion no puede ser asignada. entonces, se marca la maquina por presedencia pra no asignar alguna tarea posterior en el cromosoma
                                        break #al marcar la maquina ya no se hace necesario buscar asignar alguna tarea
                                
                                trabajos_pasados[ self.tareas[k][0] ] = 1 #se marca el trabajo como con alguna tarea en presedencia, para no asignar tareas posterior en el cromosoma
                                
                                if sum(maquinas_pasadas) == self.maquinas or sum(trabajos_pasados) == self.trabajos: #se verifica si ya todas las maquinas o trabajos estan marcados pro presedencias
                                    break #al estar todos los trabajos y maquinas con presedencias, ya no se pueden asignar tareas, por lo que se termina el ciclo
                    else:
                        break #si la maquina esta marcada por presedencias no se le puede asignar tarea
                else:
                    
                    if tiempo_final[i] == tiempo: #se verifica si el tiempo de finalizacion de procesamiento de la maquina i es el actual
                        trabajos_proceso[ maquinas_procesando[i] ] = False #el trabajo que estaba siendo procesado ahora se marco como NO en procesamiento, para que puedan asignarse sus tareas
                        maquinas_procesando[i] = (-1) #se marca la maquina como disponible
                        tareas_terminadas += 1 #se aumenta en uno la cantidad de tareas terminadas
                        tiempo_final[i] = 0  #se deja la maquina sin tiempo de finalizacion de procesamiento, puesto que no tiene ninguna tarea asignada
                        terminada = True #se define que si hubo una tarea terminada en este momento del tiempo
                        
            #si hubo tarea terminada, se aumenta en una unidad el tiempo para procurar asignar alguna tarea factible, de lo contrario se busca el siguiente tiempo de terminacion de procesamiento de una tarea    
            tiempo = tiempo + 1 if terminada else self.siguiente_tiempo ( tiempo_final ) 
        
        #se retorna el tiempo final de la simulacion                
        return tiempo + 1
    
    
    
    def mayor(self, tiempo_trabajo, tiempo_maquina):
        return tiempo_trabajo if tiempo_trabajo > tiempo_maquina else tiempo_maquina
    
    
    def calcularFitness(self, individuo):
        self.tareas = [] #se inicializa el vector de tareas
        self.iniciar(individuo) #se asignan las tareas de acuerdo al orden de operaciones definido en el individuo
        
        maquinas_tiempo = [ 0 for i in range(self.maquinas) ]
        trabajos_tiempo = [ 0 for i in range(self.trabajos) ]
        
        for tarea in self.tareas:
            tiempo_tarea = self.tabla_tiempos[ tarea[0] ][ tarea[1] ]
            trabajos_tiempo[ tarea[0] ] = maquinas_tiempo[ tarea[1] ] = self.mayor( trabajos_tiempo[ tarea[0] ], maquinas_tiempo[ tarea[1] ] ) + tiempo_tarea
        
        tiempo = max( max(trabajos_tiempo), max(maquinas_tiempo) )
        return tiempo
    
'''
file = raw_input()

fitness = FuncionFitness(4, 4, file)
individual = [9, 3, 13, 15, 8, 10, 5, 2, 7, 16, 12, 4, 14, 11, 1, 6]
print fitness.tabla_tiempos

tiempo_inicio = time.time()
print fitness.calcularFitness(individual)
tiempo_total = time.time() - tiempo_inicio
print tiempo_total


tiempo_inicio = time.time()
print fitness.carcularFitness_fast(individual)
tiempo_total = time.time() - tiempo_inicio
print tiempo_total

'''