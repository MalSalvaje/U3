import csv
from clasecarrera import Carrera
from clasefacultad import Facultad

class ManejaFacultades:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def agregarFacultad(self, unafacultad):
        if isinstance(unafacultad,Facultad):
            self.__lista.append(unafacultad)
        else:
            print('Error. Sólo se puede agregar objetos de clase facultad.')
    def leerarchivo(self):
        archivo=open('Facultades.csv')
        reader=csv.reader(archivo, delimiter=';')
        for fila in reader:
            if fila[1].isdecimal():
                self.__lista[int(fila[0])-1].agregarCarrera(fila[1],fila[2],fila[3],fila[4],fila[5]) 
            else:
               unafacultad=Facultad(fila[0],fila[1],fila[2],fila[3],fila[4]) 
               self.agregarFacultad(unafacultad)
        archivo.close()
    def mostrarFacultades(self):
        for facultad in self.__lista:
            print(facultad)
    def mostrarFacultad(self):
        cod=int(input('Ingrese codigo de facultad:\n'))
        print(self.__lista[cod-1])
    def mostrarCarrera(self):
        nombre=str(input('Ingrese nombre de la carrera:'))
        i=0
        while i<len(self.__lista) and self.__lista[i].buscarCodigoCarrera(nombre)==-1:
            i=i+1
        if i!=len(self.__lista):
            print('CODIGO DE CARRERA:{} {} FACULTAD: {} DIRECCION {}'.format(self.__lista[i].getCodigo(),self.__lista[i].buscarCodigoCarrera(nombre),self.__lista[i].getNombre(),self.__lista[i].getDireccion()))
        else:
            print('No se encontro la carrera')



