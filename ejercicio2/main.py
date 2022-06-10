from menu import Menu 
from manejadorflores import ManejadorFlores
from manejadorramos import ManejadorRamos

if __name__=='__main__':
    unmanejadorflores = ManejadorFlores()
    unmanejadorramos = ManejadorRamos()
    unmanejadorflores.leearchivo()
    unmenu = Menu()
    print(unmenu)
    print('Ingrese opción preferida:\n')
    op=input('---> ')
    while op!='4':
        unmenu.opcion(op,unmanejadorflores,unmanejadorramos)
        print(unmenu)
        print('Ingrese opción preferida:\n')
        op=input('---> ')

