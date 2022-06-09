from claseaparato import Aparato

class Lavarropas(Aparato):
    __capacidadDeLavado = ''
    __velocidadDeCentrifugado = ''
    __cantidadDeProgramas = ''
    __tipoDeCarga = ''
    __importeDeVenta = ''

    def __init__(self, marca:str, modelo:str,color:str, paisDeFabricacion:str, precioBase:float, capacidadDeLavado:int, velocidadDeCentrifugado:int, cantidadDeProgramas:int, tipoDeCarga:str):
        super().__init__(marca,modelo,color,paisDeFabricacion,precioBase)
        self.__capacidadDeLavado = capacidadDeLavado
        self.__velocidadDeCentrifugado = velocidadDeCentrifugado
        self.__cantidadDeProgramas = cantidadDeProgramas
        self.__tipoDeCarga = tipoDeCarga
        self.__importeDeVenta = self.setImporteDeVenta()

    def getCapacidadDeLavado(self)->int:
        return self.__capacidadDeLavado

    def getVelocidadDeCentrifugado(self)->int:
        return self.__velocidadDeCentrifugado

    def getCantidadDeProgramas(self)->int:
        return self.__cantidadDeProgramas

    def getTipoDeCarga(self)->str:
        return self.__tipoDeCarga


    def setImporteDeVenta(self)->float:
        importe = self.getPrecioBase()
        if self.getCapacidadDeLavado()<=5:
            importe += self.getPrecioBase()* 0.01 
        else:
            importe += self.getPrecioBase()* 0.03
        return importe

    def getImporteDeVenta(self)->float:
        return self.__importeDeVenta

    def __str__(self):
        s='LAVARROPAS '
        s+=super().__str__()
        s+=' Capacidad de Lavado: {} Velocidad de Centrifugado: {} Cantidad de Programas: {} Tipo de carga: {} \n'.format(self.getCapacidadDeLavado(), self.getVelocidadDeCentrifugado(), self.getCantidadDeProgramas(), self.getTipoDeCarga())
        return s
    
    def toJSON(self)->dict:
        d=super().toJSON()
        d["__atributos__"]["capacidadDeLavado"] = self.getCapacidadDeLavado()
        d["__atributos__"]["velocidadDeCentrifugado"] = self.getVelocidadDeCentrifugado()
        d["__atributos__"]["cantidadDeProgramas"] = self.getCantidadDeProgramas()
        d["__atributos__"]["tipoDeCarga"] = self.getTipoDeCarga()
        return d
