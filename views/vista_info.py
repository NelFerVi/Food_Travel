import tkinter as tk
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk
import os

class VistaInfo(tk.Frame):
    def __init__(self, master=None, controlador=None):
        # Crea la vista de la información de un local de comida.
        super().__init__(master)
        self.master = master

        self.controlador = controlador
        self.datos = tk.Label(self, text="Datos del local:", font="bold")
        self.datos.grid(row=0, column=0, padx=20)
        self.dat_loc = tk.Listbox(self)
        self.dat_loc.config(width=45)
        self.dat_loc.grid(row=1, column=0, padx=20)
        
        self.actividades = tk.Label(self, text="Actividades:", font="bold")
        self.actividades.grid(row=0, column=1, padx=20)
        self.dat_act = tk.Listbox(self)
        self.dat_act.config(width=45)
        self.dat_act.grid(row=1, column=1, padx=20)
        self.boton_regresar = tk.Button(
            self, text="Regresar a lista", command=self.controlador.regresar_locales)
        self.boton_regresar.grid(pady=10)
        
    def mostrar_info_local(self, local, actividades):
        # Muestra los datos del local
        self.dat_loc.delete(0, tk.END)
        self.dat_loc.insert(tk.END, f"Nombre: {local.nombre}")
        self.dat_loc.insert(tk.END, f"Tipo de Cocina: {local.t_cocina}")
        self.dat_loc.insert(tk.END, f"Menu: {local.platos}")
        self.dat_loc.insert(tk.END, f"Precio Minimo: {local.pr_min}")
        self.dat_loc.insert(tk.END, f"Precio Maximo: {local.pr_max}")
        self.dat_loc.insert(tk.END, f"Popularidad: {local.popul}")
        self.dat_loc.insert(tk.END, f"Disponibilidad: {local.disp}")

        # Muestra las actividades artisticas del local
        self.dat_act.delete(0, tk.END)
        for act in actividades:
            actividad = dict(act)
            if actividad['id_destino'] == local.id:
                self.dat_act.insert(tk.END, f"Artista: {actividad['nombre']}")
                self.dat_act.insert(tk.END, f"Fecha de presentacion: {actividad['hora_inicio']}")
        