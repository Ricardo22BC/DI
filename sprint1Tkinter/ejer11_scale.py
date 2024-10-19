import tkinter as tk

def seleccionar_valor(val):
    etiqueta.config(text=f"Valor:{val}")

#Crear la ventana principal
root = tk.Tk()
root.title("Ejer 11 Scale")
root.geometry("300x200")

#Crear Scale
scale = tk.Scale(root, from_=0, to=100, orient='horizontal', command=seleccionar_valor)
scale.pack(pady=20)

#Etiqueta para mostrar el valor seleccionado
etiqueta = tk.Label(root, text="Valor: 0")
etiqueta.pack(pady=10)

#Ejecutar el bucle principal
root.mainloop()