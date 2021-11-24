"""
PROGRAMA CADENAS DE MARKOV
AUTORES:
    RICARDO CARRILLO SANCHEZ
    JUAN ARTURO LIRA NAVARRO
"""
import numpy as np

'''
Function: generate_strings
    El funcionamiento general de este algoritmo se basa en recorrer a todos los nodos de la cadena de Markov
    de manera iterativa tomando en cuenta las probilidades que se tienen en cada transicion de nodos. 

    Algoritmo: 
        1) extraer los elementos del diccionario
        2) tomar a el primer elemento del diccionario como el elemento incial. 
        3) definir como estado anterior al primer elemento del diccionario
        
        Iteraciones mientras haya pasos (steps):
            a) escoger un nodo a partir del estado anterior tomando en cuenta probabilidad de transicion y nodos vecinos
            b) repetir pasos 2 y 3
            c) disminuir los pasos 
        
:parameters
    states: diccionario de estados 
    steps: cantidad de pasos que se daran a lo largo de la cadena

:returns: 
    esta funcion no presenta algun tipo de retorno

considerations: 
    Este algorimo recibe una cadena de markov representada por un diccionario por lo que tenemos que tener en cuenta que 
    para formar las relaciones entre los nodos se deben ingresar de forma ordenada las probabilidades de este, ed decir. 

    De tener una cadena de Markov con los siguientes nodos : Q1  Q2  Q3  Q4

    la forma de ingresar las probabilidades seria de

    nodo     Probabilidad de transicion hacia nodo:
               Q1| Q2| Q3| Q4
    'Q1'  :  [0.1, 0,  0,  0.9]      

    De esta forma estariamos diciendo que el nodo q1 tiene transicion a si mismo y al nodo q4, con sus respectivas probabilidades. 
'''


def generate_strings(states, steps):
    t = [*states, ]
    print(t[0], '--->', end=' ')
    previous_state = t[0]

    while steps - 1:
        current_state = np.random.choice(t, p=states[previous_state])
        print(current_state, '--->', end=' ')
        previous_state = current_state
        steps -= 1
    print('End of Steps')


states = {'sunny': [0.2, 0.6, 0.2, 0], 'cloudy': [0.2, 0, 0.7, 0.1], 'raining': [0.5, 0, 0.3, 0.2],
          'thunderstorm': [0.1, 0.4, 0.4, 0.1]}

generate_strings(states, 15)
