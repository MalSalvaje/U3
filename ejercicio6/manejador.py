import csv
from Aparato import Aparato

class Manejador:
    __aparatos:list[Aparato] = [] # Especifica el tipo de componente de la lista
    
    def __init__(self):
        self.__aparatos:list[Aparato] = []

    def agregarAparato(self, unaparato):
        if isinstance(unaparato, Aparato):
            self.__lista.append(unaparato)

    def mostrarTodo(self):
        for objeto in self.__lista:
            print(objeto) #Invoco str de objeto

    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                aparatos=[aparato.toJSON for aparato in self.__aparatos]
                )
        return d
