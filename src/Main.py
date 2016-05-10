import sys
import time
from poblacion import Poblacion


#Se piden los datos necesarios para que el programa funcione
trabajos = int( raw_input("Ingrese la cantidad de trabajos: ") )
maquinas = int( raw_input("Ingrese la cantidad de maquinas: ") ) 

tamano_poblacion = int (raw_input("Ingrese tamano de la poblacion: ") )
iteraciones = int (raw_input("Ingrese cantidad de iteraciones: ") )

archivo_entrada = raw_input("Ingrese el archivo de entrada: ")
archivo_salida = raw_input("Ingrese el archivo de salida: ")

#se toma el tiempo incial
tiempo_inicio = time.time()


#Si la poblacion o las iteraciones son muy pequenas no se ejecuta el algoritmo
if tamano_poblacion < 10:
    print "La poblacion es demadiado pequena"
    sys.exit()
    
if iteraciones < 10:
    print "La cantida dde iteraciones es demadiado pequena"
    sys.exit()
    


#Se crea la poblacion y se invoca a la ejecucion del algoritmo genetico
poblacion = Poblacion(tamano_poblacion, iteraciones, maquinas, archivo_entrada)

#Se obtiene al mejor individuo al final de las iteraciones
mejor_individuo = "\n" + poblacion.resultadoFinal()

#Se busca el tiempo de ejecucion
tiempo_total = time.time() - tiempo_inicio

#se intenta crear el archivo de salida  y guardar el mejor resultado  
try:     
    with open(archivo_salida, "a") as salida:
        salida.write(mejor_individuo)
        salida.close()
    
    print "Finalizado. Tiempo: %.3f segundos" % tiempo_total
except:
    print "ERROR. No se puede crear el archivo de salida"
    sys.exit(0)