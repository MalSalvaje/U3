from manejadorfacultades import ManejaFacultades

class Menu:
    __switcher: None
    def __init__(self):
        self.__switcher={'1':self.opcion1,
                         '2':self.opcion2,
                         '3':self.salir
                        }
    def opcion(self,op,unmanejador):
        func=self.__switcher.get(op, lambda: print('Opcion no válida.'))
        if op=='1' or op=='2':
            return func(unmanejador)
        else:
             return func()
    def salir(self):
        print('Usted salió del programa')
    def opcion1(self,unmanejador):
        if isinstance(unmanejador,ManejaFacultades):
            unmanejador.mostrarFacultad()
    def opcion2(self,unmanejador):
        if isinstance(unmanejador,ManejaFacultades):
            unmanejador.mostrarCarrera()
    def __str__(self):
        s='\t\t-----------MENU----------\n1. Seleccionar facultad para ver carreras que se dictan en ese establecimiento\n2. Buscar carrera por nombre.\n3. Salir del programa\n'
        return s
