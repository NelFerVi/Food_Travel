import tkinter as tk
from tkinter import *
from tkinter import ttk
from models.ubicacion import Ubicacion

class VistaBusqueda(tk.Frame):
    def __init__(self, master=None, controlador=None):
        # Crea la vista de la lista de locales.
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.ubicaciones = Ubicacion.cargar_ubicaciones("data/ubicaciones.json")
        self.titulo = tk.Label(self, text="Busqueda Y Filtrado", font='bold')
        self.titulo.grid(pady=5)

        self.lbl_buscar = tk.Label(self, text="Buscar por:",bg='lightblue',font='consolas 12 bold',
        relief=tk.GROOVE,bd=2, width=30)
        self.lbl_buscar.grid(row=1, column=0, padx=10, pady=5)

        self.buscar_combo=StringVar()
        self.combo = ttk.Combobox(self,state="readonly", width=27, textvariable=self.buscar_combo,
            values=["Nombre", "Tipo de Cocina", "Platos", "Precio Minimo", "Precio Maximo", 
            "Popularidad", "Disponibilidad"])
        self.combo.grid(row=1, column=1, padx=10, pady=5)
        
        self.boton_buscar = tk.Button(self, text="Buscar", width=10, command=self.buscar)
        self.boton_buscar.grid(row=1, column=2, padx=10, pady=5)

        # Crea el botón para ir a inicio y lo agrega a la vista
        self.boton_inicio = tk.Button(
            self, text="Ir a Inicio", width=10, command=self.controlador.regresar_inicio)
        self.boton_inicio.grid(row=5, column=0, padx=1, pady=5)
        
    def buscar(self):
        self.boton_buscar.config(state='disabled')
        self.combo.config(state='disabled')
        
        self.lb_buscar = tk.Label(self, text="", state='normal',bg='lightblue',
            font='consolas 12 bold', relief=tk.GROOVE,bd=2, width=30)
        self.lb_buscar.grid(row=2, column=0, padx=10, pady=5)
        if self.buscar_combo.get() == 'Nombre':
            self.lb_buscar.config(text='Ingresar Nombre:')
        elif self.buscar_combo.get() == 'Tipo de Cocina':
            self.lb_buscar.config(text='Ingresar Cocina:')
        elif self.buscar_combo.get() == 'Platos':
            self.lb_buscar.config(text='Ingresar Plato:')
        elif self.buscar_combo.get() == 'Precio Minimo':
            self.lb_buscar.config(text='Ingresar Precio Min:')
        elif self.buscar_combo.get() == 'Precio Maximo':
            self.lb_buscar.config(text='Ingresar Precio Max:')
        elif self.buscar_combo.get() == 'Popularidad':
            self.lb_buscar.config(text='Popularidad (min 1 / max 5):')
        elif self.buscar_combo.get() == 'Disponibilidad':
            self.lb_buscar.config(text='Disponibilidad (si/no):')
                
        self.txt_buscar = StringVar()
        self.busqueda=tk.Entry(self,font='consolas 12 bold',state='normal',textvariable=self.txt_buscar)
        self.busqueda.grid(row=2, column=1, padx=10, pady=5)
        
        self.boton_ingresar = tk.Button(self, text="Ingresar",state='normal', 
                                        width=10, command=self.buscar_local)
        self.boton_ingresar.grid(row=2, column=2, padx=10, pady=5)
    
    def buscar_local(self):
        self.listbox = tk.Listbox(self)
        self.listbox.config(width=100, height=5)
        self.listbox.grid(row=4, column=0, columnspan=4, padx=15, pady=10)
        self.actualizar_locales()
        self.listbox.bind("<Double-Button-1>", self.local_ubicacion)
        
    def actualizar_locales(self):
        # Actualiza la lista de locales con los locales obtenidos del controlador.
        locales = self.controlador.obtener_locales()
        self.listbox.delete(0, tk.END)
        for local in locales:
            val1 = self.txt_buscar.get(); val2 = self.buscar_combo.get()
            if (val1).isnumeric():
                if int(val1) >= local.pr_min and val2 == 'Precio Minimo':
                    item = local.nombre + " - Precio minimo: " + str(local.pr_min)
                    self.listbox.insert(tk.END, item)
                elif int(val1) >= local.pr_max and val2 == 'Precio Maximo':
                    item = local.nombre + " - Precio maximo: " + str(local.pr_max)
                    self.listbox.insert(tk.END, item)
                elif int(val1) >= local.popul and val2 == 'Popularidad':
                    item = local.nombre + " - Popularidad: " + str(local.popul)
                    self.listbox.insert(tk.END, item)
            else:
                if (val1).lower() in (local.nombre).lower() and val2 == 'Nombre':
                    self.listbox.insert(tk.END, local.nombre)
                    self.indice = local.id; 
                    print("Local: ", local.nombre, " - Id: ", local.id)
                elif (val1).lower() in (local.t_cocina).lower() and val2 == 'Tipo de Cocina':
                    self.listbox.insert(tk.END, local.nombre)
                elif (val1).lower() in (local.disp).lower() and val2 == 'Disponibilidad':
                    self.listbox.insert(tk.END, local.nombre)
                else:
                    for plato in local.platos:
                        if (val1).lower() in (plato).lower() and val2 == 'Platos':
                            self.listbox.insert(tk.END, local.nombre)
                
        self.boton_ingresar.config(state='disabled')
        self.lb_buscar.config(state='disabled')
        self.boton_buscar.config(state='normal')
        self.combo.config(state='normal')
    
    def local_ubicacion(self, event):
        for ubic in self.ubicaciones:
            ubicacion = dict(ubic)
            if self.indice == ubicacion['id']:
                self.lat = ubicacion['latitud']; self.long = ubicacion['longitud']
        print("Latitud: ", self.lat, " - Longitud: ", self.long)
        self.app.vista_locales.mapa.set_position(self.lat, self.long)
        self.app.vista_locales.mapa.set_zoom(32)
        
    def limpiar(self):
        self.combo.config(state='normal')
        self.boton_buscar.config(state='normal')
        self.lb_buscar.config(text='')
        self.lb_buscar.config(state='disabled')
        self.busqueda.config(text='')
        self.busqueda.config(state='disabled')
        self.boton_ingresar.config(state='disabled')