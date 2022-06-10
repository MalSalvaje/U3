class Contrato:
    __fechaInicio = ''
    __fechaFin = ''
    __pagoMensual = ''
    __jugador = None
    __equipo = None

    def __init__(self, inicio, fin, pago, jugador, equipo):
        self.__fechaInicio = inicio
        self.__fechaFin = fin 
        self.__pagoMensual = pago
        self.__jugador = jugador
        self.__equipo = equipo

    def getFechaInicio(self):
        return self.__fechaInicio

    def getFechaFin(self):
        return self.__fechaFin

    def getPagoMensual(self):
        return self.__pagoMensual

    def __str__(self):
        s='Fecha de Inicio: {} Fecha de Fin: {}Pago Mensual: {}\n'.format(self.getFechaInicio(),self.getFechaFin(),self.getPagoMensual())
        return s
