from claseaparato import Aparato

class Televisor(Aparato):
    __tipoDePantalla = ''
    __pulgadas = ''
    __tipoDeDefinicion = ''
    __conexionAInternet = ''
    __importeDeVenta = ''

    def __init__(self, marca:str, modelo:str, color:str, paisDeFabricacion:str, precioBase:float, tipoDePantalla:str, pulgadas:int, tipoDeDefinicion:str, conexionAInternet:str):
        super().__init__(marca, modelo, color, paisDeFabricacion, precioBase)
        self.__tipoDePantalla = tipoDePantalla
        self.__pulgadas = pulgadas
        self.__tipoDeDefinicion = tipoDeDefinicion
        self.__conexionAInternet = conexionAInternet
        self.__importeDeVenta = self.setImporteDeVenta()

    def getTipoDePantalla(self):
        return self.__tipoDePantalla

    def getPulgadas(self):
        return self.__pulgadas

    def getTipoDeDefinicion(self):
        return self.__tipoDeDefinicion

    def getConexionAInternet(self):
        return self.__conexionAInternet

    def setImporteDeVenta(self):
        importe = self.getPrecioBase()
        if self.getConexionAInternet():
            importe += self.getPrecioBase()* 0.1
        if self.__tipoDeDefinicion.lower()=='sd':
            importe += self.getPrecioBase()* 0.01 
        elif self.__tipoDeDefinicion.lower()=='hd':
            importe += self.getPrecioBase()* 0.02
        else:
            importe += self.getPrecioBase()* 0.03
        return importe

    def getImporteDeVenta(self)->float:
        return self.__importeDeVenta

    def __str__(self):
        s='TELEVISOR '
        s+=super().__str__()
        s+=' Tipo de pantalla: {} Pulgadas: {} Tipo de Definicion: {} Conexion a Internet: {}\n'.format(self.getTipoDePantalla(),self.getPulgadas(),self.getTipoDeDefinicion(),self.getConexionAInternet())
        return s

    def toJSON(self)->dict:
            d=super().toJSON()
            d["__atributos__"]["tipoDePantalla"] = self.getTipoDePantalla()
            d["__atributos__"]["pulgadas"] = self.getPulgadas()
            d["__atributos__"]["tipoDeDefinicion"] = self.getTipoDeDefinicion()
            d["__atributos__"]["conexionAInternet"] = self.getConexionAInternet()
            return d
