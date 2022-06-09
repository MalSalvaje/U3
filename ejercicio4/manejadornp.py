import numpy as np
import csv
from clasecalefactor import Calefactor
from claseelectrico import Electrico
from claseagas import AGas

class Manejador:
    __cantidad = 0
    __dimension= 0 
    __incremento = 5
    __lista = None
    
    def __init__(self, dimension:int):
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = 5
        self.__lista = np.empty(dimension, dtype=Calefactor)


    def agregarCalefactor(self, uncalefactor):
        if isinstance(uncalefactor,Calefactor):
            if self.__cantidad == self.__dimension:
                self.__dimension += self.__incremento
                self.__lista.resize(self.__dimension)
            self.__lista[self.__cantidad] = uncalefactor
            self.__cantidad += 1

    def leerarchivo(self, nombre:str):
        archivo=open(nombre)
        reader=csv.reader(archivo,delimiter=';')
        if nombre.lower()=='calefactor-electrico.csv':
            for fila in reader:
                uncalefactor = Electrico(str(fila[0]),str(fila[1]),int(fila[2]))
                self.agregarCalefactor(uncalefactor)
        else:
            for fila in reader:
                uncalefactor = AGas(str(fila[0]),str(fila[1]),str(fila[2]),int(fila[3]))
                self.agregarCalefactor(uncalefactor)
        archivo.close()

    def mostrarTodo(self):
        for objeto in self.__lista:
            print(objeto)

    def AGasEconomicas(self):
        print('Ingrese costo del metro cubico de gas\n')
        costo = float(input('---> '))
        print('Ingrese metros cubicos a consumir \n')
        cant = int(input('---> '))
        max = -999999
        eco = None
        for estufa in self.__lista:
            if isinstance(estufa, AGas):
                if estufa.getCalorias()>max:
                    max=estufa.getCalorias()
                    eco = estufa
        print('La estufa con mejor rendimiento es {} {} \n' .format(eco.getMarca(), eco.getModelo()))

    def ElectricaEconomicas(self):
        print('Ingrese costo del Kilowatt\n')
        costo = float(input('---> '))
        print('Ingrese kilowatts a consumir por hora\n')
        cant = int(input('---> ')) * 1000
        for electrica in self.__lista:
            if isinstance(electrica, Electrico):
                if electrica.getPotenciaMaxima() < cant:
                    print('La estufa electrica {} {} no supera el consumo indicado \n'.format(electrica.getMarca(), electrica.getModelo()))
        


