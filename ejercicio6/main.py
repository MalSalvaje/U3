from objectencoder import ObjectEncoder
from menu import Menu

if __name__=='__main__':
    unobjectencoder = ObjectEncoder()
    d=unobjectencoder.leerJSONArchivo('aparatoselectronicos.json')
    unacoleccion=unobjectencoder.decodificarDiccionario(d)
    unacoleccion.mostrarTodo()
    unmenu = Menu()
    unmenu.ejecutarMenu(unacoleccion) 
    #d=unacoleccion.toJSON()
    #unobjectencoder.guardarJSONArchivo(d,'aparatoselectronicos.json')
