
from random import random
from math import exp

t = 15

def cambiar(actual,vecino):
    delta = vecino.obtenerFitness - actual.obtenerFitness 
    if delta < 0:
        return vecino
    else:
        prob = exp(-delta/t)
        if random() < prob :
            return vecino
        else:
            return actual

def act_temp(t):
    t = t*0.9
    return t

def vecinos(actual, tamano):
    vecindario = []
    cont  = 1
    while cont < tamano:
        actual1 = actual
        punto = random.randint(0, len(actual) - 2)
        temp = actual1[punto]
        actual1[punto] = actual1[punto+1]
        actual1[punto+1] = temp
        vecindario.append(acutal1)
        cont += 1
    
return vecindario


def recocidosimulado(actual,t):
    
    vecindario = vecinos(actual, 15)
    for i in range(0,15):
        mejor = cambiar(actual, vecindario[i])
        t = act_temp(t)
        
return mejor