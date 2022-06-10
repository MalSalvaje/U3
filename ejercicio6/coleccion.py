from claseaparato import Aparato
from clasetelevisor import Televisor
from claseheladera import Heladera
from claselavarropas import Lavarropas 
from nodo import Nodo
from interfaces import ICajero
from interfaces import IGerente
from zope.interface import Interface
from zope.interface import implementer

@implementer(ICajero)
@implementer(IGerente)
class Coleccion:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato

    def agregarAparatoCabeza(self, aparato):
        nodo = Nodo(aparato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1

    def agregarAparato(self, aparato:Aparato):# Agrega un aparato al final de la lista
        unnodo = Nodo(aparato)
        if self.__comienzo == None:
            self.__comienzo = unnodo
            self.__actual = self.__comienzo
        else:
            aux = self.__comienzo
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            aux.setSiguiente(unnodo)
        self.__tope += 1

    def insertarAparato(self, elemento: Aparato, pos: int): # Inserta un aparato en la posicion indicada de la lista
        insertado = False
        unnodo = Nodo(elemento)
        if pos == 0:
            unnodo.setSiguiente(self.__comienzo)
            self.__comienzo = unnodo
            self.__actual = self.__comienzo
            insertado = True
        else:
            if self.__comienzo != None:
                i = 1
                aux = self.__comienzo
                while aux.getSiguiente() != None and i < pos:
                    aux = aux.getSiguiente()
                    i += 1
                if i == pos:
                    unnodo.setSiguiente(aux.getSiguiente())
                    aux.setSiguiente(unnodo)
                    insertado = True
                else:
                    raise IndexError("Indice fuera de rango")
        self.__tope += 1
        return insertado

    def mostrarElemento(self, pos: int):
        unNodo = None
        if pos == 0:
            if self.__comienzo == None:
                raise(IndexError("Indice fuera de rango"))
            unNodo = self.__comienzo
        else:
            i = 1
            if self.__comienzo == None:
                raise(IndexError("Indice fuera de rango"))
            unNodo = self.__comienzo.getSiguiente()
            while i < pos and unNodo.getSiguiente() != None:
                i += 1
                unNodo = unNodo.getSiguiente()
            if i < pos:
                raise(IndexError("Indice fuera de rango"))
        unAparato = unNodo.getDato()
        print(unAparato)

    def mostrarTodo(self):
        unnodo=self.__comienzo
        while unnodo.getSiguiente()!= None:
            print(unnodo.getDato())
            unnodo=unnodo.getSiguiente()

    def contarPhillips(self):
        cont = 0
        unnodo=self.__comienzo
        while unnodo.getSiguiente()!= None:
            if unnodo.getDato().getMarca().lower()=='philips':
                cont += 1
            unnodo=unnodo.getSiguiente()
        print('Hay {} aparatos marca Phillips.'.format(cont))

    def mostrarTodos(self):
        unnodo=self.__comienzo
        while unnodo.getSiguiente()!= None:
            print('Marca: {0} Pais de Fabricacion: {1} Importe de Venta: {2}\n'.format(unnodo.getDato().getMarca(),unnodo.getDato().getPaisDeFabricacion(), unnodo.getDato().getImporteDeVenta()))
            unnodo=unnodo.getSiguiente()

    def mostrarCargaSuperior(self):
        unnodo=self.__comienzo
        while unnodo.getSiguiente()!= None:
            if isinstance(unnodo.getDato(), Lavarropas):
                if unnodo.getDato().getTipoDeCarga().lower()=='superior':
                    print('Lavarropas de carga superior: '+ unnodo.getDato().getMarca())
            unnodo=unnodo.getSiguiente()
