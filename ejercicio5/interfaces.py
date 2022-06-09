from zope.interface import Interface
from zope.interface import implementer

class IMinion(Interface):
    def agregarSpaceship(self, onespaceship): # Agrega nave al final de la coleccion
        pass
    def mostrarSpaceship(self): # Muestra nave dada su posicion en la lista  
        pass

class IOverlord(Interface):
    def insertarSpaceship(self, onespaceship): # Agrega nave en una posicion elegida
        pass
    def mostrarSpaceship(self): # Muestra nave dada su posicion en la lista
        pass
