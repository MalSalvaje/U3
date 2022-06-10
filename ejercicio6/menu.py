from coleccion import Coleccion
from interfaces import IGerente
from interfaces import ICajero
from claseaparato import Aparato
from claseheladera import Heladera
from clasetelevisor import Televisor
from claselavarropas import Lavarropas

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4,
                            '5':self.opcion5,
                            '6':self.opcion6,
                            '7':self.salir
                          }

    def opcion(self,op,unacoleccion):
        func=self.__switcher.get(op, lambda: print('Opción no válida.'))
        if op!='7':
            return func(unacoleccion)
        else:
            return func()

    def salir(self):
        print('Usted salió del programa\n')

    def crearAparato(self)->Aparato:
        print('Ingrese tipo de aparato \n')
        tipo = str(input('---> '))
        print('Ingrese marca de aparato \n')
        marca = str(input('---> '))
        print('Ingrese modelo de aparato \n') 
        modelo = str(input('---> '))
        print('Ingrese color de aparato \n')
        color = str(input('---> '))
        print('Ingrese pais de origen de aparato \n')
        origen = str(input('---> '))
        print('Ingrese precio base de aparato \n')
        preciobase = float(input('---> '))
        if tipo.lower()=='heladera':
            print('Ingrese capacidad en litros.')
            capacidadenlitros = int(input('---> '))
            print('Tiene freezer? (True/False)')
            freezer = bool(input('---> '))
            print('Es ciclica?(True/False)')
            ciclica = bool(input('---> '))
            unaparato = Heladera(marca, modelo, color, origen, preciobase, capacidadenlitros, freezer, ciclica)
        elif tipo.lower()=='televisor':
            print('Ingrese tipo de pantalla.')
            tipodepantalla = str(input('---> '))
            print('Ingrese cantidad de pulgadas.')
            pulgadas = int(input('---> '))
            print('Ingrese tipo de definicion.')
            tipodedefinicion = str(input('---> '))
            print('Tiene conexion a internet?(True/False)')
            internet = bool(input('---> '))
            unaparato = Televisor(marca, modelo, color, origen, preciobase, tipodepantalla, pulgadas, tipodepantalla, internet)
        elif tipo.lower()=='lavarropas':
            print('Ingrese capacidad de lavado (en kilogramos).')
            capacidad = int(input('---> '))
            print('Ingrese velocidad de centrifugado.')
            velocidad = int(input('---> '))
            print('Ingrese cantidad de programas del lavarropas.')
            cantidaddeprogramas= int(input('---> '))
            print('Ingrese tipo de carga. (Frontal/Superior)')
            tipodecarga = str(input('---> '))
            unaparato = Lavarropas(marca, modelo, color, origen, preciobase, capacidad, velocidad, cantidaddeprogramas, tipodecarga)
        else:
            print('Tipo de aparato no valido\n')
        return unaparato



    def opcion1(self, unacoleccion:IGerente):
        if isinstance(unacoleccion,Coleccion):
            unaparato = self.crearAparato()
            print('Ingrese posicion donde colocar aparato: \n')
            pos = int (input('---> '))
            unacoleccion.insertarAparato(unaparato, pos)

    def opcion2(self, unacoleccion:ICajero):
        if isinstance(unacoleccion,Coleccion):
            unaparato = self.crearAparato()
            unacoleccion.agregarAparato(unaparato)

    def opcion3(self, unacoleccion:Coleccion):
        if isinstance(unacoleccion,Coleccion):
            print('Ingrese posicion del aparato a mostrar: \n')
            pos = int (input('---> '))
            unacoleccion.mostrarElemento(pos)
    
    def opcion4(self, unacoleccion:Coleccion):
        if isinstance(unacoleccion,Coleccion):
            unacoleccion.contarPhillips()

    def opcion5(self, unacoleccion:Coleccion):
        if isinstance(unacoleccion,Coleccion):
            unacoleccion.mostrarCargaSuperior()

    def opcion6(self, unacoleccion:Coleccion):
        if isinstance(unacoleccion,Coleccion):
            unacoleccion.mostrar()

    def ejecutarMenu(self, unacoleccion:Coleccion):
        op = '0'
        while op != '7':
            print('Ingrese la opcion preferida')
            print('1. Insertar un aparato en una posicion a eleccion.')
            print('2. Agregar un aparato al final de la coleccion.')
            print('3. Mostrar un objeto seleccionado por posicion en la lista.')
            print('4. Mostrar cuantas heladeras, lavarropas y televisores Phillips hay en inventario.')
            print('5. Mostrar marca de todos los lavarropas de carga superior.')
            print('6. Mostrar marca, pais de fabricacion e importe de veta de todos los aparators.')
            print('7. Guardar cambios y salir.')
            op = input('---> ')
            self.opcion(op, unacoleccion)

