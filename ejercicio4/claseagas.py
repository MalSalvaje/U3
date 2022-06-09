from clasecalefactor import Calefactor

class AGas(Calefactor):
    __matricula = ''
    __calorias = ''

    def __init__(self, marca:int, modelo:str, matricula:str, calorias:int):
        super().__init__(marca, modelo)
        self.__matricula = matricula
        self.__calorias = calorias

    def getMatricula(self):
        return self.__matricula

    def getCalorias(self):
        return self.__calorias

    def __str__(self):
        s=super().__str__()
        s+='Matricula: {} Calorias: {}\n'.format(self.getMatricula(), self.getCalorias())
        return s

    
