class Carrera:
    __codigo=''
    __nombre=''
    __fechaInicio=''
    __duracion=''
    __titulo=''
    def __init__(self, cod, nom, fecha, dur, tit):
        self.__codigo=cod
        self.__nombre=nom
        self.__fechaInicio=fecha
        self.__duracion=dur
        self.__titulo=tit
    def getCodigo(self):
        return self.__codigo
    def getNombre(self)->str:
        return self.__nombre
    def getInicio(self):
        return self.__fechaInicio
    def getDuracion(self):
        return self.__duracion
    def getTitulo(self)->str:
        return self.__titulo
    def __str__(self):
        s='CODIGO: {} NOMBRE: {} FECHA DE INICIO: {} DURACION: {} TITULO: {}\n'.format(self.getCodigo(),self.getNombre(),self.getInicio(),self.getDuracion(),self.getTitulo())
        return s
