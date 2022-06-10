from manejadornp import Manejador

if __name__=='__main__':
    print('Ingrese cantidad de calefactores a cargar: \n')
    dimension=int(input('--> '))
    unmanejador=Manejador(dimension)
    unmanejador.leerarchivo('calefactor-electrico.csv')
    unmanejador.leerarchivo('calefactor-a-gas.csv')
    unmanejador.mostrarTodo() 
    unmanejador.AGasEconomicas()
    unmanejador.ElectricaEconomicas()

