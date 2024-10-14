import tkinter as tk
from tkinter import messagebox

def mensaje():
    messagebox.showinfo("Mensaje","Botón clicado")

#Crear la ventana principal
root = tk.Tk()
root.title("Ventana con dos Botones")
root.geometry("300x150")

#Crear los botones
boton_mensaje = tk.Button(root, text="No hagas Clic", command=mensaje)
boton_mensaje.pack(pady=10)
                                                    #Cerrar la ventana
boton_cerrar = tk.Button(root, text="Cerrar ventana", command=root.quit)
boton_cerrar.pack(pady=10)

#Ejecuta el bucle principal
root.mainloop()