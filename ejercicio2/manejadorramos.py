from claseramo import Ramo
from manejadorflores import ManejadorFlores

class ManejadorRamos:
    __ramos = []
    
    def __init__(self):
        self.__ramos = []
    
    def agregarRamo(self,unramo):
        if isinstance(unramo,Ramo):
            self.__ramos.append(unramo)

    def crearRamo(self, unmanejadorflores):
        if isinstance(unmanejadorflores, ManejadorFlores):
            print('Ingrese tamaño de ramo\n')
            size=str(input('---> '))
            unramo=Ramo(size)
            for i in range(1,unramo.getLength()):
                unramo.agregarFlor(unmanejadorflores.getFlor())
            self.__ramos.append(unramo)
