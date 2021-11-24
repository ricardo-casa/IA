"""
PROGRAMA 6: CALCULO PROPOSICIONAL RECURSIVO
AUTORES:
    RICARDO CARRILLO SANCHEZ
    JUAN ARTURO LIRA NAVARRO
"""

operators = {'!', '^', 'v', '>', '(', ')', 'z'}
priority = {'!': [' not ', 1], '^': [' and ', 2], 'V': [' or ', 3], '>': ['', 4], 'z': ['', 5]}


def infix_to_postfix(expression):
    """
    function: inflix_to_postfix

    Esta funcion se encarga de encontrar la expresion equivalente en 
    notacion postfija a partir de una infija

    :parameters
        expression: funcion logica en String

    :attributes
        stack: pila en la cual se agregan operandos y operadores
        output: funcion logica en en notacion posfija.

    :return
        output: funcion logica en en notacion posfija.
    """

    stack = []
    output = ''

    for element in expression:
        if element not in operators:
            output += element

        elif element == '(':
            stack.append('(')

        elif element == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()

        else:
            while stack and stack[-1] != '(' and priority[element][1] <= priority[stack[-1]][1]:
                output += stack.pop()
            stack.append(element)

    while stack:
        output += stack.pop()

    return output


class node:
    """
    class node

    :parameters
        value: valor del nodo en string

    :attributes
        value: valor del nodo en string
        left: referencia futura a nodo hijo izquierdo
        right: referencia futura a nodo hijo derecho

    :return
        Esta clase no tiene ningun retorno en su metodo principal
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class binary_tree:
    """
    class binary_tree

    :parameters
        value_dicctionary: diccionario de valores de las variables 
                           involucradas en la funcion logica

    :attributes
        root: referencia futura al nodo raiz
        value_dictionary: diccionario de valores de las variables 
                          involucradas en la funcion logica

    :return
        Esta clase no tiene ningun retorno en su metodo principal
    """

    def __init__(self, value_dictionary):
        self.root = None
        self.value_dictionary = value_dictionary

    def create_binary_tree(self, postfix):
        """
        class binary_tree
        method: create_binary_tree:
        
        Este metod asignacion de nodos
        y los valores de los mismos, asi como referencias de los nodos a 
        partir de sus hijos en izquierda y derecha. 

        El mecanismo de funcionamiento se basa en el siguiente algoritmo: 

        1)  Si se encuentra un caracter que no pertenece a un operador logico,
            operando, se crea un nodo con el valor encontrado y se anade dicho 
            nodo a la pila.
        
        2)  Caso contrario al anterior, se habria encontrado un operador por 
            lo que se crea un nodo con el valor del operador y se hacen dos pop
            a la pila. Dichos pop, representaran los hijos encontrados del operador.
            A los elementos se les hara referencia como hijos del operador. 
            Finalmente se agrega el operador a la pila

        3) Una vez que se encontro al nodo raiz, se le asigna al arbol.


        :parameters
            postfix: funcion logica a evaluar en string
                            
        :attributes
            stack: pila en la cual se almacenaran las variables encontradas
                   en la funcion logica

        :return
            self.root: durante la creacion del arbol binario se encontrara el 
                       valor de la raiz por lo que se asigna, ya que estaba como
                       None, y se retorna
        """
        stack = []

        for char in postfix:
            if char not in operators:
                t = node(char)
                stack.append(t)
            else:
                t = node(char)
                t1, t2 = stack.pop(), stack.pop()
                t.right, t.left = t1, t2
                stack.append(t)
        self.root = stack.pop()
        return self.root

    def operate_logic(self, node):

        """
        class binary_tree
        method: operate_logic
        
        Este metodo esta disenado para evaluar una funcion logica 
        a partir de llamadas recursivas a la misma a partir de recorrer 
        el arbol binario con llamadas recursivas por medio de la raiz y 
        su valor (operando o operador)

        A) Caso base: llegar a un operando y retornar su valor logico

        B) Casos recursivo: llegar a un operando y hacer la llamada
                            recursiva a partir de una equivalencia 
                            logica (caso implicacion y doble implicacion)
                            evaluando los hijos izquierdos y derecho

        C) Caso vacio: retonar un mesaje advirtiendo de que el arbol esta vacio 
                       en caso de que el valor de la raiz sea de None. 
    
        :parameters
            node: referencia a nodo
                            
        :attributes
            No hay atributos

        :return
            A)  Llamada recursiva a la funcion con nodo nuevo
            B)  Valor logico evaluando la funcion
        """

        if node.value is None:
            return 'Empty Binary Tree'

        elif node.value not in operators:
            return self.value_dictionary[node.value]

        else:
            if node.value == '!':
                return eval('not ' + repr(self.operate_logic(node.right)))

            elif node.value == '^' or node.value == 'v':
                return eval(
                    repr(self.operate_logic(node.left)) + priority[node.value][0] + repr(
                        self.operate_logic(node.right)))

            elif node.value == '>':
                return eval(
                    'not ' + repr(self.operate_logic(node.left)) + ' or ' + repr(self.operate_logic(node.right)))

            else:  # for double implication, logically equivalent to (p -> q) ^ (q -> p)
                return eval(
                    ('not ' + repr(self.operate_logic(node.left)) + ' or ' + repr(self.operate_logic(node.right)))
                    and
                    ('not ' + repr(self.operate_logic(node.right)) + ' or ' + repr(self.operate_logic(node.left)))
                )


postfix = infix_to_postfix('((p^q)>q)')
print('infix expression: ((p^q)>q)')
print('postfix expression: ', postfix)
binary_tree = binary_tree({'p': True, 'q': False})
root = binary_tree.create_binary_tree(postfix)
print(binary_tree.operate_logic(root))
