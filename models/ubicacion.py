import json

class Ubicacion:
    def __init__(self, id, latitud, longitud, direccion):
        self.id = id
        self.latitud = latitud
        self.longitud = longitud
        self.direccion = direccion
    
    # Estos dos metodos retornan la clase dict para instanciar el objeto
    # como diccionario
    def keys(self):
        return ('id','latitud','longitud','direccion')
    def __getitem__(self,item):
        return getattr(self,item)
    
    @classmethod
    def cargar_ubicaciones(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**local) for local in data]