import tkinter as tk
from tkinter import messagebox

def acerca_de():
    messagebox.showinfo("Mensaje","Este es el ejercicio 9")

def salir_aplicacion():
    root.quit()

#Crear la ventana principal
root = tk.Tk()
root.title("Menú")
root.geometry("300x200")

#Crar la barra de menú
menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

#Crear un submenú "Archivo"
menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Nuevo")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir_aplicacion)

#Crear submenú "Ayuda"
menu_ayuda = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)

#Ejecutar
root.mainloop()