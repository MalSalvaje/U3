from clasecarrera import Carrera

class Facultad:
    __codigo=''
    __nombre=''
    __direccion=''
    __localidad=''
    __telefono=''
    __carreras=[]

    def __init__(self, cod, nom, direc, loc, tel):
        self.__codigo= cod
        self.__nombre= nom
        self.__direccion= direc
        self.__localidad= loc
        self.__telefono= tel
        self.__carreras=[]

    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self)->str:
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getLocalidad(self)->str:
        return self.__localidad
    
    def getTelefono(self):
        return self.__telefono
    
    def getLength(self):
        return len(self.__carreras)
    
    def __str__(self):
        s='CODIGO: {} NOMBRE: {} DIRECCION: {} LOCALIDAD: {} TELEFONO: {}\nCARRERAS:\n'.format(self.getCodigo(),self.getNombre(),self.getDireccion(),self.getLocalidad(),self.getTelefono())
        for carrera in self.__carreras:
            s+='{}'.format(carrera.__str__())
        return s
    
    def agregarCarrera(self, cod, nom, fecha, duracion, titulo):
        unacarrera=Carrera(cod, nom, fecha, duracion, titulo)#Para una composicion se deben crear los objetos en la clase continente, ya sea en el init o como método 
        self.__carreras.append(unacarrera)
    
    def buscarCodigoCarrera(self, nombre):
        i=0
        while i<self.getLength() and self.__carreras[i].getNombre()!=nombre:
            i=i+1
        if i!=self.getLength():
            return self.__carreras[i].getCodigo()
        else:
            return -1

    def __del__(self):
        del self.__carreras
