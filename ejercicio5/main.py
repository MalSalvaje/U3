from interfaces import *
from manejador import Manejador
from clasespaceship import Spaceship

def Minion(unmanejador: IMinion):
    print('Ingrese raza de invasores\n')
    race = str(input('---> '))
    print('Ingrese tipo de spaceship\n')
    tipo = str(input('---> '))
    print('Ingrese estado de Overdrive\n')
    estado = str(input('---> '))
    print('Ingrese numero de miembros de la tripulacion\n')
    miembros = str(input('---> '))
    onespaceship = Spaceship(race, tipo, estado, miembros)
    unmanejador.agregarSpaceship(onespaceship)

def Overlord(unmanejador: IOverlord):
    print('Ingrese raza de invasores\n')
    race = str(input('---> '))
    print('Ingrese tipo de spaceship\n')
    tipo = str(input('---> '))
    print('Ingrese estado de Overdrive\n')
    estado = str(input('---> '))
    print('Ingrese numero de miembros de la tripulacion\n')
    miembros = str(input('---> '))
    onespaceship = Spaceship(race, tipo, estado, miembros)
    unmanejador.insertarSpaceship(onespaceship)

def testInterfaces():
    unmanejador = Manejador()
    unmanejador.leerarchivo()
    print('Mostrando todas las naves:\n')
    unmanejador.mostrarTodo()
    print('Ingrese nombre de usuario(Minion/Overlord):\n')
    usuario = str(input('---> '))
    print('Ingrese clave de usuario: \n')
    clave = str(input('---> '))
    if usuario.lower()=='overlord' and clave=='2468':
        print('Testeando Overlord \n')
        Overlord(IOverlord(unmanejador))
    elif usuario.lower()=='minion' and clave=='1234':
        print('Testeando Minion\n')
        Minion(IMinion(unmanejador))
    else:
        print('No existe el usuario\n')

if __name__=='__main__':
   testInterfaces() 

