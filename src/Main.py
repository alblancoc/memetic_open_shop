import sys
import time
from poblacion import Poblacion
from cgi import log


#Se piden los datos necesarios para que el programa funcione
tamano = int( sys.argv[1] ) #Tamano de la poblacion 
iteraciones = int( sys.argv[2] ) #iteraciones del algoritmo
maquinas = int( sys.argv[3] ) #cantidad de maquinas del problema
trabajos = int( sys.argv[4] ) #cantidad de trabajos del problema
archivo = sys.argv[5] #archivo donde se encuentra la matriz de tiempos
uniforme = True if sys.argv[6] == 'True' else False #detemina si la seleccion se hace por metodo uniforme (True) o por torneo (False)
generacional = True if sys.argv[7] == 'True' else False #detemina si el reemplazo se hace por metodo generacional (True) o por steady-state (False)
heuristica = True if sys.argv[8] == 'True' else False #detemina si se aplica la heuristica de mejora inicial  (True) o no (False)
archivo_salida = sys.argv[9] #archivo en el cual se van a almacenar los resultados arrojados por el algoritmo

#se toma el tiempo incial
tiempo_inicio = time.time()
    

#Si la poblacion o las iteraciones son muy pequenas no se ejecuta el algoritmo
if tamano < 6:
    print "La poblacion es demadiado pequena"
    sys.exit()
    
if iteraciones < 10:
    print "La cantida dde iteraciones es demadiado pequena"
    sys.exit()
    

#Se crea la poblacion y se invoca a la ejecucion del algoritmo genetico
poblacion = Poblacion(tamano, iteraciones, maquinas, trabajos, archivo, uniforme, generacional, heuristica)

#Se obtiene al mejor individuo al final de las iteraciones
log = poblacion.generarLog() + "\n"

#Se busca el tiempo final de ejecucion
tiempo_total = time.time() - tiempo_inicio #se calcula el tiempo que tardo el algoritmo en encontrar la solucion

#se crea el archivo de salida  y se guarda el mejor resultado  
try:     
    print "Finalizado. Tiempo: %.3f segundos" % tiempo_total #para informacion del desempeno del algoritmo, se imprime el tiempo total de la ejecucion
    
    #se abre (y si es necesario la funcion lo crea) el archivo donde se van a guardar los resultados
    with open(archivo_salida, 'a') as salida:
        salida.write( log ) #se agrega al archivo de resultados las salidas presentadas en el log del algoritmo
        salida.close()
except:
    print "ERROR. No se puede crear el archivo de salida"
    sys.exit(0)