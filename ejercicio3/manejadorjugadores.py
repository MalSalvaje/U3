from clasejugador import Jugador
import csv

class ManejadorJugadores:
    __lista:list[Jugador] = []

    def __init__(self):
        self.__lista:list[Jugador] = []

    def agregarJugador(self, unjugador):
        if isinstance(unjugador,Jugador):
            self.__lista.append(unjugador)
        else:
            print('Tipo de datos incorrecto.')
    

    def getJugador(self):
        dni=input('Ingrese numero de jugador para seleccionarlo: ')
        jugador= None
        i=0
        while i<len(self.__lista) and self.__lista[i].getDni()!=dni:
            i+=1
        if i==len(self.__lista):
            jugador= -1
        else:
            jugador=self.__lista[i]
        return jugador


