import tkinter as tk
from tkinter.font import Font

class VistaInicio(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de inicio.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        # Define una fuente grande y en negrita para el título
        titulo_font = Font(size=24, weight="bold")

        # Crea una etiqueta para el título y la agrega a la vista
        self.titulo = tk.Label(self, text="Bienvenidos a Food Travel\nSeleccione una opcion:", font=titulo_font)
        self.titulo.grid(row=0,column=1,padx=100,pady=5)

        # Crea el botón para ir a Destinos Culinarios y lo agrega a la vista
        self.boton_locales = tk.Button(
            self, text="Destinos Culinarios", command=self.controlador.mostrar_locales
        )
        self.boton_locales.place(x=20,y=100)
        # Crea el botón para ir a Busqueda y lo agrega a la vista
        self.boton_busqueda = tk.Button(
            self, text="Busqueda", command=self.controlador.busqueda
        )
        self.boton_busqueda.place(width=100, x=180,y=100)

        self.boton_locales = tk.Button(
            self, text="Planificar Visitas", command=self.controlador.mostrar_locales
        )
        self.boton_locales.place(x=340,y=100)

        self.boton_locales = tk.Button(
            self, text="Reviews y Calificaciones", command=self.controlador.mostrar_locales
        )
        self.boton_locales.place(x=480,y=100)
