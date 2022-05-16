class Flor:
    __numero=''
    __nombre=''
    __color=''
    __descripcion=''

    def __init__(self, num, nom, col, desc):
        self.__numero=num
        self.__nombre=nom
        self.__color=col
        self.__descripcion=desc

    def getNumero(self):
        return self.__numero

    def getNombre(self):
        return self.__nombre

    def getColor(self):
        return self.__color

    def getDescripcion(self):
        return self.__descripcion
