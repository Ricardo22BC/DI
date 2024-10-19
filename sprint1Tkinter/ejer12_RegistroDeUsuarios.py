import tkinter as tk

from tkinter import messagebox

#Funcion para agregar el usuario
def agregar_usuario():
    nombre=entrada_nombre.get()
    edad=scale.get()
    genero=var_genero.get()

    #Agregamos los datos del usuario en la lista
    usuario = f"Nombre: {nombre},  Edad: {edad},  Género: {genero}"
    lista_usuarios.insert(tk.END, usuario)

    #limpiar los campos
    entrada_nombre.delete(0, tk.END)
    var_genero.set(None)


#Función para eleminar usuario seleccionado
def eliminar_usuario():
    seleccion = lista_usuarios.curselection()
    for i in seleccion:
        lista_usuarios.delete(i)

#Función para salir de la aplicación
def salir():
    root.quit()

#Función para mensaje al seleccionar 'guardar lista'.
def guardar_lista():
    messagebox.showinfo("Guardar Lista", "La lista ha sido guardada con éxito")

# Función para mostrar mensaje de "Cargar Lista"
def cargar_lista():
    messagebox.showinfo("Cargar Lista", "La lista ha sido cargada con éxito")

#Función para seleccionar el valor del scale
def seleccionar_valor(val):
    etiqueta.config(text=f"Valor:{val}")

#Crear ventana principal
root = tk.Tk()
root.title("Registro de Usuarios")
root.geometry("600x700")

#Entrada para el nombre.
etiqueta = tk.Label(root, text="Escribe tu nombre:")
etiqueta.pack(pady=2)
entrada_nombre = tk.Entry(root, width=30)
entrada_nombre.pack(pady=2)

#Scale para la edad.
etiqueta = tk.Label(root, text="Edad:")
etiqueta.pack(pady=2)
scale = tk.Scale(root, from_=0, to=100, orient='horizontal', command=seleccionar_valor)
scale.pack(pady=2)
etiqueta = tk.Label(root, text="Valor : 0")
etiqueta.pack(pady=2)

#Radiobutton para la selección del género.
etiqueta = tk.Label(root, text="Género")
etiqueta.pack(pady=5)
var_genero=tk.StringVar()
var_genero.set(None)
radio_masc = tk.Radiobutton(root, text="Masculino", variable=var_genero, value="Masculino")
radio_masc.pack(pady=10)
radio_fem = tk.Radiobutton(root, text="Femenino", variable=var_genero, value="Femenino")
radio_fem.pack(pady=10)
radio_otro= tk.Radiobutton(root, text="Otro", variable=var_genero, value="Otro")
radio_otro.pack(pady=10)

#Boton para añadir el usuario a la lista.
boton = tk.Button(root, text="Añadir Usuario", command=agregar_usuario)
boton.pack(pady=5)

#Una lista que muestra los usuarios registrados y tiene que estar dentro de un frame para poder poner el Scrollbar..
frame_lista= tk.Frame(root)
frame_lista.pack(pady=5,fill='both', expand=True)

lista_usuarios= tk.Listbox(frame_lista, selectmode=tk.MULTIPLE,width=60)
lista_usuarios.pack(side='left', fill='both', expand=True)

#Scrollbar vertical
scroll_vert = tk.Scrollbar(frame_lista,orient='vertical', command=lista_usuarios.yview)
scroll_vert.pack(side='right', fill='both')
lista_usuarios.config(yscrollcommand=scroll_vert.set)

#Botón eliminar
boton_eliminar = tk.Button(root, text="Eliminar Usuario", command=eliminar_usuario)
boton_eliminar.pack(pady=5)

#Botón salir.
boton_salir = tk.Button(root, text="Salir", command=salir)
boton_salir.pack(pady=5)

#Menú desplegable con las opciones 'Guardar lista y 'Cargar lista'
menu = tk.Menu(root)
root.config(menu=menu)
menu_opciones = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Opciones", menu=menu_opciones)
menu_opciones.add_command(label="Guardar lista", command=guardar_lista)
menu_opciones.add_command(label="Cargar Lista", command=cargar_lista)

#Ejecutar el bucle
root.mainloop()

