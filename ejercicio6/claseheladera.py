from claseaparato import Aparato

class Heladera(Aparato):
    __capacidadEnLitros = ''
    __freezer = ''
    __ciclica = ''
    __importeDeVenta = ''
    
    def __init__(self,marca:str, modelo:str, color:str, paisDeFabricacion:str, precioBase:float, capacidadEnLitros:int, freezer:bool, ciclica:bool):
        super().__init__(marca, modelo, color, paisDeFabricacion, precioBase)
        self.__capacidadEnLitros = capacidadEnLitros
        self.__freezer = freezer
        self.__ciclica = ciclica
        self.__importeDeVenta = self.setImporteDeVenta()

    def getCapacidadEnLitros(self):
        return self.__capacidadEnLitros
    
    def getFreezer(self):
        return self.__freezer

    def getCiclica(self):
        return self.__ciclica

    def setImporteDeVenta(self):
        importe = self.getPrecioBase()
        if self.getCiclica(): 
            importe += self.getPrecioBase()* 0.1 
        if self.getFreezer():
            importe += self.getPrecioBase()* 0.05
        else:
            importe += self.getPrecioBase()* 0.01
        return importe

    def getImporteDeVenta(self)->float:
        return self.__importeDeVenta

    def __str__(self):
        s='HELADERA '
        s+=super().__str__()
        s+=' Capacidad en Litros: {} Freezer: {} Ciclica: {}\n'.format(self.getCapacidadEnLitros(), self.getFreezer(), self.getCiclica())
        return s

    def toJSON(self)->dict:
            d=super().toJSON()
            d["__atributos__"]["capacidadEnLitros"] = self.getCapacidadEnLitros()
            d["__atributos__"]["Freezer"] = self.getFreezer()
            d["__atributos__"]["Ciclica"] = self.getCiclica()
            return d
