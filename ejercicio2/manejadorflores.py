import numpy as np
import csv
from claseflor import Flor

class ManejadorFlores:
    __cantidad = 0
    __dimension = 5
    __incremento = 5
    __flores = None

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 5
        self.__incremento = 5
        self.__flores = np.empty(5, dtype=Flor)

    def agregarFlor(self, unaflor):
        if isinstance(unaflor, Flor):
            if self.__dimension==self.__cantidad:
                self.__dimension+=self.__incremeneto
                self.__ramos.resize(self.__dimension)
            self.__flores[self.__cantidad] = unaflor
            self.__cantidad += 1

    def leearchivo(self):
        archivo=open('flores.csv')
        reader=csv.reader(archivo, delimiter=',')
        for fila in reader:
            unaflor=Flor(int(fila[0]),str(fila[1]),str(fila[2]),str(fila[3]))
            self.agregarFlor(unaflor)

    def mostrarFlores(self):
        for flor in self.__flores:
            print(flor)

    def getFlor(self):
        print('Ingrese numero de flor para agregarla al ramo:\n')
        self.mostrarFlores()
        num=int(input('---> '))
        return self.__flores[num-1]
