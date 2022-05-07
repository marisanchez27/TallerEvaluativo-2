# 3. El banco de hierro de la isla de Braavos necesita de sus
# servicios para programar un software que permita:
# • Almacenar información de un cliente (nombre, apellido,
# cedula, ciudad)
# • Almacenar información de la cuenta (numeroCuenta, saldo)
# • Se debe permitir consultar saldo en cualquier momento
# • Se debe permitir ingresar o retirar dinero cuando se desee

class Cliente: 

    def __init__(self,nombre,apellido,cedula,ciudad):
         self.__nombre = nombre
         self.__apellido= apellido
         self.__cedula= cedula
         self.__ciudad= ciudad

    @property
    def nombre(self):
        return(self.__nombre)

    @property
    def apellido(self):
        return(self.__apellido)

    @property
    def cedula(self):
        return(self.__cedula)

    @property
    def ciudad(self):
        return(self.__ciudad)


    @nombre.setter
    def nombre(self,nombre):
        self.__nombre= nombre

    @apellido.setter
    def apellido(self,apellido):
        self.__apellido= apellido

    @cedula.setter
    def cedula(self,cedula):
        self.__cedula= cedula

    @ciudad.setter
    def ciudad(self,ciudad):
        self.__ciudad= ciudad

    