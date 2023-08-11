import json

class Usuario:
    def __init__(self, id, nombre, apellido, hist_rutas):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.hist_rutas = hist_rutas
    
    @classmethod
    def cargar_usuarios(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**local) for local in data]