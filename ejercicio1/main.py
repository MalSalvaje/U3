from manejadorfacultades import ManejaFacultades
from menu import Menu

if __name__=='__main__':
    unmanejador=ManejaFacultades()
    unmanejador.leerarchivo()
    unmenu=Menu()
    print(unmenu)
    op=(input('---> '))
    unmenu.opcion(op,unmanejador)
    #unmanejador.mostrarFacultades() 
    #unmanejador.mostrarFacultad()
    #unmanejador.mostrarCarrera()
