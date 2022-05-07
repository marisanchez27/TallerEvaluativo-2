# 1. Codificar un programa que permita recibir el nombre,
# edad, país, equipo y tiempo(minutos)) de la última prueba
# de crono individual de varios ciclistas del giro de
# Italia, al final el software estará en la capacidad de
# indicar cual fue el ciclista con el mejor tiempo y
# mostrar todos sus datos

class Ciclista: 

    def __init__(self,nombre,edad,pais,equipo,minutos):
         self.__nombre = nombre
         self.__edad= edad
         self.__pais= pais
         self.__equipo= equipo
         self.__minutos= minutos

    @property
    def nombre(self):
        return(self.__nombre)

    @property
    def edad(self):
        return(self.__edad)

    @property
    def pais(self):
        return(self.__pais)

    @property
    def equipo(self):
        return(self.__equipo)

    @property
    def minutos(self):
        return(self.__minutos)


    @nombre.setter
    def nombre(self,nombre):
        self.__nombre= nombre

    @edad.setter
    def edad(self,edad):
        self.__edad= edad

    @pais.setter
    def pais(self,pais):
        self.__pais= pais

    @equipo.setter
    def equipo(self,equipo):
        self.__equipo= equipo

    @minutos.setter
    def minutos(self,minutos):
        self.__minutos= minutos

    def tiempo (self):
        print (f"El menor tiempo fue {self.minutos}")                                        
