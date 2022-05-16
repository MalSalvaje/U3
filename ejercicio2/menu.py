from manejadorflores import ManejadorFlores
from manejadorramos import ManejadorRamos

class Menu:
    __switcher = None
    
    def __init__(self):
        self.__switcher={ '1':self.opcion1,
                          #'2':self.opcion2,
                          '3':self.salir
                        }

    def opcion(self, op, unmanejadorflores, unmanejadorramos):
        func=self.__switcher.get(op,lambda:print('Opcion no valida.'))
        if op=='1' or op=='2':
            return func(unmanejadorramos, unmanejadorflores) # Recordatorio: comprobar si ambas opciones necesitan todos los parametros
        else:
            return func()

    def salir(self):
        print('Usted salio del programa.')
    
    def opcion1(self, unmanejadorramos, unmanejadorflores):
        if isinstance(unmanejadorramos,ManejadorRamos) and isinstance(unmanejadorflores,ManejadorFlores):
            return unmanejadorramos.crearRamo(unmanejadorflores)

    #def opcion2(self, unmanejadorramos):

    def __str__(self):
        s='1. Registrar venta de un ramo. 2. Mostrar flores mas vendidas en un ramo.\n'
        return s
