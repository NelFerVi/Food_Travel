import json

class Local:
    def __init__(self, id, nombre, t_cocina, platos, pr_min, pr_max, popul, disp,imagen, id_ubicacion):
        self.id = id
        self.nombre = nombre
        self.t_cocina = t_cocina
        self.platos = platos
        self.pr_min = pr_min
        self.pr_max = pr_max
        self.popul = popul
        self.disp = disp
        self.imagen = imagen
        self.id_ubicacion = id_ubicacion

    @classmethod
    def cargar_locales(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**local) for local in data]

