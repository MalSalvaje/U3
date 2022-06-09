from clasecontrato import Contrato

class Equipo:
    __nombre=''
    __ciudad=''
    __contratos= None

    def __init__(self,nombre,ciudad):
        self.__nombre=nombre
        self.__ciudad=ciudad
        self.__contratos:list[Contrato]= []
    
    def agregarContrato(self, uncontrato):
        if isinstance(uncontrato, Contrato):
            self.__contratos.append(uncontrato)
    
    def getNombre(self):
        return self.__nombre

    def getCiudad(self):
        return self.__ciudad

    def __str__(self):
        s='Nombre: {} Ciudad: {}\n'.format()
        return s

        
