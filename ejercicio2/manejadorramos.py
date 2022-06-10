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
            print('Ingrese tamaño de ramo: S(Small)-M(Medium)-L(Large)\n')
            size=str(input('---> '))
            unramo=Ramo(size)
            for i in range(unramo.getLength()):
                unaflor=unmanejadorflores.getFlor()
                unramo.agregarFlor(unaflor)
            self.__ramos.append(unramo)

    def mostrarRamos(self):
        for ramo in self.__ramos:
            print(ramo)

    def buscarMasVendidas(self):
        totales=[0,0,0,0,0]
        for ramo in self.__ramos:
            for flor in ramo:
                totales[flor.getNumero()-1]+=1
        for i in range(totales):
            print('La flor {} vendió {} unidades\n'.format(i+1,totales[i]))

