import sys
import time
from poblacion import Poblacion
from cgi import log


#Se piden los datos necesarios para que el programa funcione
tamano = int( sys.argv[1] )
iteraciones = int( sys.argv[2] )
maquinas = int( sys.argv[3] )
trabajos = int( sys.argv[4] )
archivo = sys.argv[5]
uniforme = True if sys.argv[6] == 'True' else False
generacional = True if sys.argv[7] == 'True' else False
archivo_salida = sys.argv[8]

#se toma el tiempo incial
tiempo_inicio = time.time()


#Si la poblacion o las iteraciones son muy pequenas no se ejecuta el algoritmo
if tamano < 5:
    print "La poblacion es demadiado pequena"
    sys.exit()
    
if iteraciones < 10:
    print "La cantida dde iteraciones es demadiado pequena"
    sys.exit()
    


#Se crea la poblacion y se invoca a la ejecucion del algoritmo genetico
poblacion = Poblacion(tamano, iteraciones, maquinas, trabajos, archivo, uniforme, generacional)

#Se obtiene al mejor individuo al final de las iteraciones
log = poblacion.generarLog() + "\n"

#Se busca el tiempo de ejecucion
tiempo_total = time.time() - tiempo_inicio

#se intenta crear el archivo de salida  y guardar el mejor resultado  
try:     
    print "Finalizado. Tiempo: %.3f segundos" % tiempo_total
    
    with open(archivo_salida, 'a') as salida:
        salida.write( log )
        salida.close()
except:
    print "ERROR. No se puede crear el archivo de salida"
    sys.exit(0)