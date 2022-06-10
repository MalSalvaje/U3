import csv
from clasespaceship import Spaceship
from zope.interface import implementer
from interfaces import IMinion
from interfaces import IOverlord

@implementer(IMinion)
@implementer(IOverlord)
class Manejador:
    __lista = [] # Especifica el tipo de componente de la lista
    
    def __init__(self):
        self.__lista= []
    
    def agregarSpaceship(self, onespaceship):
        if isinstance(onespaceship, Spaceship):
            self.__lista.append(onespaceship)

    def leerarchivo(self):
        archivo=open('space-invaders.csv')
        reader=csv.reader(archivo,delimiter=';')
        next(reader)
        for fila in reader:
            onespaceship = Spaceship(str(fila[0]),str(fila[1]),bool(fila[2]),int(fila[3])) # Se castea tipos de dato
            self.agregarSpaceship(onespaceship)
        archivo.close()

    def mostrarTodo(self):
        for objeto in self.__lista:
            print(objeto) #Invoco str de objeto

    def getLength(self)->int:
        return len(self.__lista)

    def insertarSpaceship(self, onespaceship):
        print('Ingrese posicion para agregar nave\n')
        pos = int(input('---> '))
        if pos<=self.getLength():
            self.__lista.insert(pos, onespaceship)
            print('Nave insertada correctamente.\n')
        else:
            raise IndexError

    def mostrarSpaceship(self):
        print('Ingrese posicion para ver nave\n')
        pos = int(input('---> '))
        if self.getLength()>=pos:
            print('La nave indicada es:\n')
            print(self.__lista[pos])
        else:
            raise IndexError


