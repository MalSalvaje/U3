from manejadorequipos import ManejadorEquipos
from manejadorjugadores import ManejadorJugadores
from manejadorcontratos import ManejadorContratos

class Menu:
    __switcher = None
    
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.salir
                          }

    def opcion(self,op,unmanejadorjugadores, unmanejadorequipos):
        func=self.__switcher.get(op, lambda: print('Opción no válida.')
        if op=='1':
            return func(unmanejadorcontratos,unmanejadorequipos,unmanejadorjugadores)
        else:
            return func()

    def salir(self):
        print('Usted salió del programa\n')

    def opcion1(self, unmanejadorcontratos, unmanejadorequipos, unmanejadorjugadores):
        if isinstance(unmanejadorcontratos,ManejadorContratos) and isinstance(unmanejadorjugadores,ManejadorJugadores) and isinstance(unmanejadorequipos, ManejadorEquipos):
            unmanejadorcontratos.contratar(unmanejadorequipos, unmanejadorjugadores)

