![image](https://github.com/NelFerVi/Food_Travel/assets/95060671/7a2ca0f2-fa2e-4ea5-a4f0-32d5c714b89d)

# Food_Travel
Esta aplicación brindará información detallada sobre los lugares, eventos y actividades en diferentes destinos culinarios, y permitirá a los usuarios buscar, filtrar y planificar sus visitas de acuerdo a sus preferencias gastronómicas.
## Breve explicación del funcionamiento:
La pantalla inicial muestra un mapa interactivo en el cual aparecen los locales de comida con un marcador. Haciendo click sobre el marcador nos muestra una imagen del local.

En la parte superior hay cuatro botones:
- Destinos Culinarios
- Búsqueda
- Planificar Visitas
- Reviews y Calificaciones

![image](https://github.com/NelFerVi/Food_Travel/assets/95060671/e7a1e978-cb23-412f-af05-17b70656f6b1)

### Destinos Culinarios:
Esta función nos permite explorar los restaurantes que están precargados en el archivo locales.json.

Haciendo click sobre este botón pasamos a la segunda pantalla que nos muestra una lista con los nombres de los locales y abajo el mapa interactivo.

Haciendo simple click sobre uno de los locales de la lista el mapa se centra en ese local y amplía el zoom para ver con más detalle la dirección.

![image](https://github.com/NelFerVi/Food_Travel/assets/95060671/170ba276-30ac-47c5-ac42-78f64733925d)


Haciendo doble click sobre uno de los locales, pasamos a la tercera pantalla con la información de ese local y también nos centra en el mapa ese local y amplía el zoom.

![image](https://github.com/NelFerVi/Food_Travel/assets/95060671/c259bdda-09d8-4bda-904c-4fd7c06d9297)


Esta tercera pantalla nos muestra un listBox con la información del local y también otro listBox con las actividades o espectáculos que tiene agendados ese local. De no tener actividades el listBox apareceria vacío. Las actividades estan pre-cargadas en el archivo actividades.json. Hemos colocado algunas actividades en solo algunos locales para poder ver los dos casos cuando hay y cuando no hay actividades.

El botón **Regresar a lista** nos permite volver a la segunda pantalla con la lista completa de los locales. Alli podemos elegir otro para ver sus datos y actividades.

En la segunda pantalla podemos presionar el botón **Ir a Inicio** que nos levará a la primera pantalla con los cuatro botones.
### Búsqueda:
Este boton nos lleva a la función de búsqueda implementada en una cuarta pantalla en donde tenemos un comboBox en donde podemos elegir los criterios de búsqueda: Nombre, Tipo de Cocina, Platos, Precio Mínimo, Precio Máximo, Popularidad y Disponibilidad.

![image](https://github.com/NelFerVi/Food_Travel/assets/95060671/8353374b-e9c8-46a7-955e-fb3a3b4e2854)


Seleccionamos una de estas opciones, presionamos el boton **Buscar** y se habilita una caja de entrada tk.Entry en donde escribimos lo que deseamos buscar. La rutina de busqueda no diferencia mayúsculas y minusculas en el dato ingresado para flexibilizar la búsqueda, y tampoco es necesario escribir la palabra completa, podemos escribir solo una parte de la palabra que buscaremos.

![image](https://github.com/NelFerVi/Food_Travel/assets/95060671/82761010-ff0a-43a4-b08a-0fc2a9b85372)


Luego presionamos el botón **Ingresar** y nos desplegará un listBox con una lista de los locales que cumplen con ese criterio.

Por ejemplo ponemos buscar por tipo de cocina regional y nos mostrará en la lista los locales que ofrezcan este tipo de cocina.

![image](https://github.com/NelFerVi/Food_Travel/assets/95060671/24d5cb42-c10b-418d-a993-1888bcce53d2)


Si elegimos la opción por platos o tipo de comida, nos mostrara todos los locales que ofreden este tipo de plato.

![image](https://github.com/NelFerVi/Food_Travel/assets/95060671/3ff95964-598b-43e8-9ecb-427c82f01751)


Si elegimos la opción por Precio Mínimo, nos mostrara todos los locales cuyo precio mínimo sea menor o igual al ingresado.

![image](https://github.com/NelFerVi/Food_Travel/assets/95060671/855b0c57-278c-4e4b-8195-07c98450f1b6)


Si elegimos la opción por Precio Máximo, nos mostrará todos los locales cuyo precio máximo sea menor o igual al ingresado.

![image](https://github.com/NelFerVi/Food_Travel/assets/95060671/88172864-e48f-4605-abfb-fd51c5d3b586)


Si elegimos la opción por Popularidad, el valor ingresado debe estar **entre 1 (mínima)** y **5 (máxima)**, y nos mostrará todos los locales cuya popularidad sea menor o igual a la ingresada.

![image](https://github.com/NelFerVi/Food_Travel/assets/95060671/23c91a42-9857-4d19-aa03-cda3b7a26f04)


La opción Disponibilidad puede ser **si (local funcionando)** o **no (local cerrado)**, aunque podría implementarse con otra funcionalidad. En este caso nosotros hemos adoptado por simplicidad este criterio.

![image](https://github.com/NelFerVi/Food_Travel/assets/95060671/6d1eb855-8d60-454f-ab0f-0ff2304e8c95)


En la lista que tenemos los locales encontrados, teníamos pensado implementar una función que haciendo doble click sobre el local seleccionado lo centrará en el mapa. Escribimos el código pero nos da un error que no pudimos resolver hasta ahora.

![image](https://github.com/NelFerVi/Food_Travel/assets/95060671/df17c2d5-cef4-4184-acfe-592a34d65c0f)


Los botones 3 y 4 (Planificar Visitas y Reviews y Calificaciones) no llegamos a agregar los codigos porque nos aparecian errores que no pudimos resolver, solo dejamos las funciones que estaban funcionando bien.


