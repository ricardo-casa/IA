"""
PROGRAMA EL AGENTE SECRETO
CLASE: TABLA ENCRIPTAR
AUTORES:
    RICARDO CARRILLO SANCHEZ
    JUAN ARTURO LIRA NAVARRO
"""
class tablaEncriptar:

    '''
    Este tipo de encriptacion se basa en el almacenamiento de un texto en una tabla
    de tamano n (clave). Asi mismo se forma una tabla similar para realizar el proceso de desencriptado

    :parameter
        mensaje: es el texto que se desea encriptar
        clave: es el numero de columnas que contendra la tabla a construir

    :attributes
        mensaje: mensaje a encriptar
        clave: es el numero de columnas que contendra la tabla a construir
        mensajeTabla: tabla en la que se almacenara el mensaje a encriptar
        mensajeEncriptado: texto que ha sido alterado.

    :return
        No presenta ningun retorno del metodo constructor

    '''

    def __init__(self, mensaje, clave):
        mensaje = mensaje.replace(" ", "")
        mensaje = mensaje.upper()
        self.mensaje = mensaje
        self.clave = clave
        self.mensajeTabla = []
        self.mensajeEncriptado = ''


        for i in range(0, len(self.mensaje), clave):
            t = self.mensaje[i:i + clave]
            self.mensajeTabla.append([t + (clave - len(t)) * 'S' if len(t) < clave else t])

    def encriptar(self):
        '''
        A traves de la tabla que se ha generado, se realizan un par de iteraciones sobre ella para
        reacomodar el contenido de la misma. De modo que se altera el mensaje original.

        En caso de tener espacios vacios ya que la tabla debe ser cuadrada, estos se llenaran con la
        letra: s.

        :parameter
            Este metodo no presenta ningun parametro.

        :return:
            Este metodo no presenta retornos
        '''
        for columna in range(self.clave):
            for fila in self.mensajeTabla:
                self.mensajeEncriptado += fila[0][columna]

    def desencriptar(self):
        '''
        Por medio del mensaje que se ha encriptado, formaremos de nuevo una tabla, dividiendo el mensaje
        encriptado en una longitud a la de la clave, concatenaremos un mensaje nuevo a partir de un patron
        establecido, de arriba a abajo y de izquierda a derecha.

        :parameter
            Este metodo no presenta ningun parametro.

        :return:
            mensajeDesencriptado: mensaje que se encuentra desencriptado.
        '''
        mensajeDesencriptado = ''
        longitud = len(self.mensajeEncriptado) // self.clave
        desencriptarTabla = [self.mensajeEncriptado[i:i + longitud] for i in range(0, len(self.mensajeEncriptado), longitud)]

        for columna in range(longitud):
            for fila in desencriptarTabla:
                mensajeDesencriptado += fila[columna]
        return mensajeDesencriptado


te = tablaEncriptar("LA CRIPTOGRAFIA ES ROMANTICA", 4)
te.encriptar()
print(te.mensajeEncriptado)
print(te.desencriptar())