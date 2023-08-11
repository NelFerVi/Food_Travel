class ControladorBusqueda:
    def __init__(self, app, modelo_buscar, modelo_actividad):
        self.app = app
        self.modelo_buscar = modelo_buscar
        self.modelo_actividad = modelo_actividad
            
    def obtener_locales(self):
        return self.modelo_buscar

    def seleccionar_local(self):
        """ Obtiene el índice del local seleccionado y llama a la vista de
        información para mostrar la información del local. """
        indice = self.app.vista_busqueda.obtener_local_seleccionado()
        if indice is not None:
            local = self.modelo_buscar[indice]
            actividades = []
            
            for actividad in self.modelo_actividad:
                actividades.append(actividad)
            #self.app.vista_info.mostrar_info_local(local, actividades)
            self.app.vista_info.mostrar_info_local(local)
            self.app.cambiar_frame(self.app.vista_info)
            
    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)
        self.app.vista_busqueda.limpiar()