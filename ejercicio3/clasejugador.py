class Jugador:
    __nombre = ''
    __dni=''
    __ciudadNatal=''
    __paisDeOrigen=''
    __fechaNacimiento=''

    def __init__(self,nombre,dni,ciudad,pais,nacimiento):
        self.__nombre = nombre
        self.__dni = dni
        self.__ciudadNatal = ciudad
        self.__paisDeOrigen= pais
        self.__fechaNacimiento= nacimiento

    def getNombre(self):
        return self.__nombre

    def getDni(self):
        return self.__dni

    def getCiudadNatal(self):
        return self.__ciudadNatal

    def getPaisDeOrigen(self):
        return self.__paisDeOrigen

    def getFechaNacimiento(self):
        return self.__fechaNacimiento

    def __str__(self):
        s='Nombre: {} Dni: {} Ciudad Natal: {} Pais de Origen: {} Fecha de Nacimiento: {}\n'.format(self.getNombre(),self.getDni(),self.getCiudadNatal(),self.getPaisDeOrigen(),self.getFechaNacimiento())
        return s
