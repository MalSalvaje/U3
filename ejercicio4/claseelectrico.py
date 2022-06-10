from clasecalefactor import Calefactor

class Electrico(Calefactor):
    __potenciaMaxima = ''

    def __init__(self, marca:str, modelo:str, potenciaMaxima:int):
        super().__init__(marca, modelo)
        self.__potenciaMaxima = potenciaMaxima

    def getPotenciaMaxima(self)->int:
        return self.__potenciaMaxima

    def __str__(self):
        s=super().__str__()
        s+='Potencia Maxima: {} Watts \n'.format(self.getPotenciaMaxima())
        return s
