import json
from coleccion import Coleccion
from claseaparato import Aparato
from clasetelevisor import Televisor
from claseheladera import Heladera
from claselavarropas import Lavarropas


class ObjectEncoder(object): 
    def decodificarDiccionario(self, d): 
        if '__class__' not in d: 
            return d 
        else: 
            class_name=d['__class__'] 
            class_=eval(class_name) 
            if class_name=='Coleccion': 
                aparatos=d['aparatos'] 
                dAparato = aparatos[0] 
                coleccion=class_() 
                for i in range(len(aparatos)): 
                    dAparato=aparatos[i] 
                    class_name=dAparato.pop('__class__') 
                    class_=eval(class_name) 
                    atributos=dAparato['__atributos__'] 
                    unAparato=class_(**atributos) 
                    coleccion.agregarAparato(unAparato) 
            return coleccion

    def guardarJSONArchivo(self, diccionario, nombre): 
        archivo = open(nombre, "w", encoding="UTF-8")
        json.dump(diccionario, destino, indent=4) 
        destino.close()             

    def leerJSONArchivo(self,nombre): 
        archivo=open(nombre)
        diccionario=json.load(archivo)
        archivo.close()
        return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)
