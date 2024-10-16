import tkinter as tk

from ejer3 import etiqueta

#Funciones para la selección los elementos de la lista y ver en una etiqueta la seleccionada.
def mostrar_selecciones():
    seleccion = listbox.curselection()
    elementos = [listbox.get(i) for i in seleccion]
    etiqueta.config(text=f"Seleccionaste: {', '.join(elementos)}")

#Crear ventana principal
root = tk.Tk()
root.title("Listbox")
root.geometry("300x250")

#Crear una lista de opciones
opciones = ["Manzana", "Banana", "Naranja"]

#Crear Listbox
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
for opcion in opciones:
    listbox.insert(tk.END, opcion)
listbox.pack(pady=5)

#Botón para mostrar las selecciones
boton = tk.Button(root, text="Mostrar selección", command=mostrar_selecciones)
boton.pack(pady=5)

#Etiqueta para mostrar la selección
etiqueta = tk.Label(root, text="Seleccionaste: Ninguno")
etiqueta.pack(pady=10)

#Ejecutar el bucle principal
root.mainloop()
