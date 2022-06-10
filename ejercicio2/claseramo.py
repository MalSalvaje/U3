from claseflor import Flor

class Ramo:
    __size= None
    __flores:list[Flor] = []

    def __init__(self,s):
        self.__switcher = {'S':2,
                           'M':4,
                           'L':6
                          } 
        self.__size=self.__switcher.get(s, lambda: print('Opcion no valida.'))
        self.__flores:List[Flor] = []

    def agregarFlor(self, unaflor):
        if isinstance(unaflor,Flor):
            self.__flores.append(unaflor)

    def getLength(self):
        return self.__size

    def __str__(self):
        s='Flores en el Ramo:\n'
        for flor in self.__flores:
            s+='{}\n'.format(flor.__str__())
        return s

