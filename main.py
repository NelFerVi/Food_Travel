import tkinter as tk
from models.actividades import Actividad
from models.local import Local
from models.usuario import Usuario
from models.ubicacion import Ubicacion
from views.vista_inicio import VistaInicio
from views.vista_locales import VistaLocales
from views.vista_info import VistaInfo
from views.vista_busqueda import VistaBusqueda
from controllers.controlador_inicio import ControladorInicio
from controllers.controlador_locales import ControladorLocales
from controllers.controlador_busqueda import ControladorBusqueda
from controllers.controlador_info import ControladorInfo

class Aplicacion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Food Travel")
        self.geometry("640x750")
        self.resizable(False, False)
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)
        
    def inicializar(self):
        locales = Local.cargar_locales("data/locales.json")
        usuarios = Usuario.cargar_usuarios("data/usuarios.json")
        ubicaciones = Ubicacion.cargar_ubicaciones("data/ubicaciones.json")
        actividades = Actividad.cargar_actividades("data/actividades.json")

        controlador_inicio = ControladorInicio(self)
        controlador_locales = ControladorLocales(self, locales, actividades)
        controlador_busqueda = ControladorBusqueda(self, locales, actividades)
        controlador_info = ControladorInfo(self)
        
        self.vista_inicio = VistaInicio(self, controlador_inicio)
        self.vista_locales = VistaLocales(self, controlador_locales)
        self.vista_info = VistaInfo(self, controlador_info)
        self.vista_busqueda = VistaBusqueda(self, controlador_busqueda)

        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_locales)
        self.ajustar_frame(self.vista_info)
        self.ajustar_frame(self.vista_busqueda)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")
    
    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
