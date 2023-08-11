import json

class Actividad:
    def __init__(self, id, id_destino, nombre, hora_inicio):
        self.id = id
        self.id_destino = id_destino
        self.nombre = nombre
        self.hora_inicio = hora_inicio

    # Retorna el objeto en formato string al print
    def __repr__(self):
        return str(self.__dict__)
    
    # Estos dos metodos retornan la clase dict para instanciar el objeto
    # como diccionario
    def keys(self):
        return ('id','id_destino','nombre','hora_inicio')
    def __getitem__(self,item):
        return getattr(self,item)

    @classmethod
    def cargar_actividades(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**local) for local in data]