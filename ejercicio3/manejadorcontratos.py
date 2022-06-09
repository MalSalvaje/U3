import numpy as np
from clasecontrato import Contrato 
from manejadorequipos import ManejadorEquipos
from manejadorjugadores import ManejadorJugadores

class ManejadorContratos:
    __cantidad = 0
    __dimension= 30
    __incremento = 5
    __lista = None
    
    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 30
        self.__incremento = 5
        self.__lista = np.empty(30, dtype=Contrato)


    def agregarContrato(self, uncontrato):
        if isinstance(uncontrato,Contrato):
            if self.__cantidad == self.__dimension:
                self.__dimension += self.__incremento
                self.__lista.resize(self.__dimension)
            self.__lista[self.__cantidad] = uncontrato 
            self.__cantidad += 1

    def contratar(self, unmanejadorjugadores, unmanejadorequipos):
        jugador=unmanejadorjugadores.getJugador()
        equipo=unmanejadorequipos.getEquipo()
        if jugador!=-1 and equipo!=-1:
            uncontrato=Contrato(jugador,equipo)
            unmanejadorequipos.agregarContratoEnEquipo(equipo, uncontrato)
            unmanejadorcontratos.agregarContrato(uncontrato) 
        else:
            print('No se encontro el jugador o el equipo\n')
