from manejadorflores import ManejadorFlores
from manejadorramos import ManejadorRamos

class Menu:
    __switcher = None
    
    def __init__(self):
        self.__switcher={ '1':self.opcion1,
                          '2':self.opcion2,
                          '3':self.opcion3,
                          '4':self.salir
                        }

    def opcion(self, op, unmanejadorflores, unmanejadorramos):
        func=self.__switcher.get(op,lambda:print('Opcion no valida.'))
        if op=='1':
            return func(unmanejadorramos, unmanejadorflores) # Recordatorio: comprobar si ambas opciones necesitan todos los parametros
        elif op=='2' or op=='3':
            return func(unmanejadorramos)
        else:
            return func()

    def salir(self):
        print('Usted salio del programa.')
    
    def opcion1(self, unmanejadorramos, unmanejadorflores):
        if isinstance(unmanejadorramos,ManejadorRamos) and isinstance(unmanejadorflores,ManejadorFlores):
            return unmanejadorramos.crearRamo(unmanejadorflores)

    def opcion2(self, unmanejadorramos):
        if isinstance(unmanejadorramos,ManejadorRamos):
            unmanejadorramos.buscarMasVendidas()

    def opcion3(self,unmanejadorramos):
        if isinstance(unmanejadorramos,ManejadorRamos):
            unmanejadorramos.mostrarRamos()


    def __str__(self):
        s='\t-----------MENU----------\n1. Registrar venta de un ramo.\n2. Mostrar flores mas vendidas en un ramo.\n3. Mostrar ramos.\n4. Salir del programa.'
        return s
