import sys
import time
from poblacion import Poblacion


#Se piden los datos necesarios para que el programa funcione
linea_entrada = raw_input("").split(" ")
tamano = int( linea_entrada[0] )
iteraciones = int( linea_entrada[1] )
maquinas = int( linea_entrada[2] )
trabajos = int( linea_entrada[3] )
archivo = linea_entrada[4]
uniforme = linea_entrada[5]
generacional = linea_entrada[6]


#se toma el tiempo incial
tiempo_inicio = time.time()


#Si la poblacion o las iteraciones son muy pequenas no se ejecuta el algoritmo
if tamano < 10:
    print "La poblacion es demadiado pequena"
    sys.exit()
    
if iteraciones < 10:
    print "La cantida dde iteraciones es demadiado pequena"
    sys.exit()
    


#Se crea la poblacion y se invoca a la ejecucion del algoritmo genetico
poblacion = Poblacion(tamano, iteraciones, maquinas, trabajos, archivo, uniforme, generacional)

#Se obtiene al mejor individuo al final de las iteraciones
log = "\n" + poblacion.generarLog()

#Se busca el tiempo de ejecucion
tiempo_total = time.time() - tiempo_inicio

#se intenta crear el archivo de salida  y guardar el mejor resultado  
try:     
    with open(archivo_salida, "a") as salida:
        salida.write( log )
        salida.close()
    
    print "Finalizado. Tiempo: %.3f segundos" % tiempo_total
except:
    print "ERROR. No se puede crear el archivo de salida"
    sys.exit(0)