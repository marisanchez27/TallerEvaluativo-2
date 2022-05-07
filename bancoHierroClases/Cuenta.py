# 3. El banco de hierro de la isla de Braavos necesita de sus
# servicios para programar un software que permita:
# • Almacenar información de un cliente (nombre, apellido,
# cedula, ciudad)
# • Almacenar información de la cuenta (numeroCuenta, saldo)
# • Se debe permitir consultar saldo en cualquier momento
# • Se debe permitir ingresar o retirar dinero cuando se desee

class Cuenta: 

    def __init__(self, saldo):
         self.__numeroCuenta = None
         self.__saldo= saldo

    @property
    def numeroCuenta(self):
        return(self.__numeroCuenta)

    @property
    def saldo(self):
        return(self.__saldo)

    @numeroCuenta.setter
    def numeroCuenta(self,numeroCuenta):
        self.__numeroCuenta= numeroCuenta

    @saldo.setter
    def saldo(self,saldo):
        self.__saldo= saldo

    def consultarSaldo (self):
        print (self.saldo)

    def retirarSaldo(self,cantidadIngresar):
        self.saldo -= cantidadIngresar

    def ingresarSaldo (self,cantidadIngresar):
       self.saldo += cantidadIngresar                       