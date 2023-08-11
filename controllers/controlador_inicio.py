class ControladorInicio:
    def __init__(self, app):
        self.app = app

    def mostrar_locales(self):
        self.app.cambiar_frame(self.app.vista_locales)
        
    def busqueda(self):
        self.app.cambiar_frame(self.app.vista_busqueda)
        
    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)