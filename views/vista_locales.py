import tkinter as tk
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk
from models.local import Local
from models.ubicacion import Ubicacion

class VistaLocales(tk.Frame):
    def __init__(self, master=None, controlador=None):
        # Crea la vista de la lista de locales.
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.locales = Local.cargar_locales("data/locales.json")
        self.ubicaciones = Ubicacion.cargar_ubicaciones("data/ubicaciones.json")
        self.marcadores = []
        self.imagenes = []
        
        self.titulo = tk.Label(self, text="Destinos Culinarios", font="bold")
        self.titulo.grid(row=0, column=0, padx=50, pady=10)

        self.listbox = tk.Listbox(self)
        self.listbox.config(width=100)
        self.listbox.grid(row=1, column=0, padx=20, pady=20)
        self.actualizar_locales()

        # Asocia el evento de doble clic a la función seleccionar_local
        self.listbox.bind("<ButtonRelease-1>", self.centrar_local)
        self.listbox.bind("<Double-Button-1>", self.seleccionar_local)
        
        #Muestra el mapa
        self.mapa = TkinterMapView(width=600, height=400, corner_radius=20)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.set_zoom(16)
        self.mapa.grid(row=2, column=0, padx=20, pady=20)

        # Crea el botón para ir a inicio y lo agrega a la vista
        self.boton_inicio = tk.Button(
            self, text="Ir a Inicio", command=self.controlador.regresar_inicio
        )
        self.boton_inicio.grid(row=3, column=0, padx=50, pady=10)
        
        # Cargar las imagenes de los locales
        self.cargar_imagenes()
        # Carga los marcadores en el mapa
        self.cargar_marcadores()
        
    def actualizar_locales(self):
        # Actualiza la lista de locales con los locales obtenidos del controlador.
        locales = self.controlador.obtener_locales()
        self.listbox.delete(0, tk.END)
        for local in locales:
            self.listbox.insert(tk.END, local.nombre)

    def obtener_local_seleccionado(self):
        #Retorna el índice del local seleccionado en la lista.
        #print("Indice: ", indice)
        indice = self.listbox.curselection()
        if indice:
            return indice[0]
        else:
            return None

    def seleccionar_local(self, event):
        ''' Obtiene el índice del local seleccionado y llama al controlador para
        mostrar la información del local. '''
        self.controlador.seleccionar_local()
    
    #Los siguientes dos metodos se encargan de cargar las imagenes y los marcadores
    def cargar_imagenes(self):
        for local in self.locales:
            imagen = ImageTk.PhotoImage(Image.open(f"views/images/{local.imagen}").resize((200, 200)))
            self.imagenes.append(imagen)
    
    def cargar_marcadores(self):
        for ubicacion, local in zip(self.ubicaciones, self.locales):
            imagen = self.imagenes[ubicacion.id - 1]
            marcador = self.agregar_marcador_mapa(ubicacion.latitud, ubicacion.longitud, 
                        local.nombre, imagen)
            marcador.hide_image(True)
            self.marcadores.append(marcador)
    
    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None):
        lat = latitud; long = longitud
        return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen,
        command=seleccionar_ubicacion)
    
    def centrar_local(self, event):
        # Obtiene el índice del elemento seleccionado
        indice_seleccionado = self.listbox.curselection()
        # Obtiene el local seleccionado
        local_seleccionado = self.locales[indice_seleccionado[0]]
    
        ubicacion_seleccionada = Ubicacion(0, 0, 0, "")
    
        # Busca la ubicación correspondiente al local seleccionado
        for ubicacion in self.ubicaciones:
            if ubicacion.id == local_seleccionado.id_ubicacion:
                ubicacion_seleccionada = ubicacion
                break
    
        # Centra el mapa en la ubicación seleccionada
        self.mapa.set_position(ubicacion_seleccionada.latitud, ubicacion_seleccionada.longitud)
        self.mapa.set_zoom(32)

# Este metodo muestra u oculta la foto del local sobre el marcador en el mapa    
def seleccionar_ubicacion(marcador):
    if marcador.image_hidden is True:
        marcador.hide_image(False)
    else:
        marcador.hide_image(True)
    print("Ubicación seleccionada: ", marcador.text)

