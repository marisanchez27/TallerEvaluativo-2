from Ciclista import Ciclista


class PruebaCrono:

    def __init__(self):
        self.ciclistas=[]
    
    def agregarCiclistas(self,ciclista):
        self.ciclistas.append(ciclista)

    def calcularMenorTiempoCiclista(self):
        menorTiempo=self.ciclistas[0]
        for ciclista in self.ciclistas:
            if(ciclista.minutos < menorTiempo.minutos):
                menorTiempo=ciclista 

        print(f"mejor tiempo es: {menorTiempo.nombre}, la eda es: {menorTiempo.edad}, el pais es : {menorTiempo.pais}, equipo al que pertenece es : {menorTiempo.equipo} ")            
            