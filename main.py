from Ciclista import Ciclista
from PruebaCrono import PruebaCrono

opcion=1
carrera=PruebaCrono()

while(opcion!=0):
    
    opcion=int(input("digite una opcion: "))

    if(opcion==1):
        nombre=input("digite el nombre del ciclista: ")
        edad=input("digite la edad del ciclista: ")
        pais=input("digite el pais del ciclista: ")
        equipo=input("digite el equipo del ciclista: ")
        minutos=int(input("digite el tiempo en minutos del ciclista: "))

        ciclista=Ciclista(nombre,edad,pais,equipo,minutos)
        
       
        carrera.agregarCiclistas(ciclista)

carrera.calcularMenorTiempoCiclista()        
        