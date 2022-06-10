class Calefactor:
    __marca = ''
    __modelo = ''

    def __init__(self,marca:str,modelo:str):
        self.__marca=marca
        self.__modelo=modelo

    def getMarca(self)->str:
        return self.__marca

    def getModelo(self)->str:
        return self.__modelo 

    def __str__(self):
        s='Marca: {} Modelo: {} '.format(self.getMarca(),self.getModelo())
        return s
