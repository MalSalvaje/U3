from manejadorjugadores import ManejadorJugadores
from manejadorequipos import ManejadorEquipos
from menu import Menu

if __name__=='__main__':
    unmanejadorequipos=ManejadorEquipos()
    unmanejadorjugadores=ManejadorJugadores()
    unmenu=menu()
    print(unmenu)
    op=input('Ingrese opcion preferida.\n')
    unmenu.opcion(op,unmanejadorequipos,unmanejadorjugadores)

    
