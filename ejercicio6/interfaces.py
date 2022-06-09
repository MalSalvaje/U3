from zope.interface import Interface
from zope.interface import implementer

class ICajero(Interface):
    def agregarAparato(self, unaparato): # Agrega aparato al final de la coleccion
        pass
    def mostrarAparato(self): # Muestra aparato dada su posicion en la lista  
        pass

class IGerente(Interface):
    def insertarAparato(self, unaparato): # Agrega aparato en una posicion elegida
        pass
    def mostrarAparato(self): # Muestra aparato dada su posicion en la lista
        pass
