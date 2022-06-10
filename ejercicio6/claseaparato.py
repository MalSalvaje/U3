from abc import ABC
import abc

class Aparato(ABC):
    __marca = ''
    __modelo = ''
    __color = ''
    __paisDeFabricacion = ''
    __precioBase = ''

    def __init__(self, marca:str, modelo:str, color:str, paisDeFaricacion:str, precioBase:float):
        self.__marca = marca 
        self.__modelo = modelo
        self.__color = color 
        self.__paisDeFabricacion = paisDeFaricacion 
        self.__precioBase = precioBase 

    def getMarca(self)->str:
        return self.__marca

    def getModelo(self)->str:
        return self.__modelo

    def getColor(self)->str:
        return self.__color

    def getPaisDeFabricacion(self)->str:
        return self.__paisDeFabricacion

    def getPrecioBase(self)->float:
        return self.__precioBase

    @abc.abstractmethod
    def __str__ (self):
        s='Marca: {} Modelo: {} Color: {} Pais De Fabricacion: {}' .format(self.getMarca(), self.getModelo(), self.getColor(), self.getPaisDeFabricacion())
        return s

    @abc.abstractmethod
    def toJSON(self):
        d= dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca = self.__marca,
                modelo = self.__modelo,
                color = self.__color,
                paisDeFaricacion = self.__paisDeFabricacion,
                )
            )
