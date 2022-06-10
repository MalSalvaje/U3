from claseequipo import Equipo
import numpy as np

class ManejadorEquipos:
    __cantidad=0
    __dimension=0
    __incremento=0
    __lista = []

    def __init__(self):
        self.__cantidad=0
        self.__dimension = 0 
        self.__incremento=5
        self.__lista = np.empty(0, dtype=Equipo)

    def agregarEquipo(self, unequipo):
        if isinstance(unequipo, Equipo):
            if self.__cantidad==self.__dimension:
                self.__dimension+=self.__incremento
                self.__lista.resize(self.__dimension) 
            self.__lista[self.__cantidad] = unequipo
            self.__cantidad += 1

    def leearchivo(self):
        archivo=open('Equipos.csv')
        reader=csv.open(archivo,delimiter=';') 
        band= True
        for fila in reader:
            if(band):
                self.__dimension=fila
                self.__lista = np.empty(fila, dtype=Equipo)
                band = False 
            else:
            unequipo=Equipo(str(fila[0]),str(fila[1]))
            self.agregarEquipo(unequipo)
        archivo.close()

    def mostrarEquipos(self):
        for equipo in self.__lista:
            print(equipo)


    def getEquipo(self):
        nom=input('Ingrese nombre de equipo para seleccionarlo: ')
        i=0
        equipo= None
        while i<len(self.__lista) and self.__lista[i].getNombre()!=nom:
           i+=1
        if i==len(self.__lista):
            equipo=-1
        else:
            equipo=self.__lista[i]
        return equipo

    def agregarContratoEnEquipo(self, unequipo, uncontrato):
        if isinstance(equipo, Equipo) and isinstance(contrato, Contrato):
            equipo.agregarContrato(uncontrato)
            print('Se agrego correctamente el contrato al equipo\n'
        else:
            print('Hay un tipo de datos incorrecto\n')
