import tkinter as tk

def escribir_texto():
    texto = entrada.get()
    etiqueta_resultado.config(text="Has escrito: " + texto )
#Crear ventana principal
root = tk.Tk()
root.title("Entry")
root.geometry("300x200")
#Crear widgets
etiqueta = tk.Label(root, text="Escribe tu nombre:")
etiqueta.pack(pady=10)

entrada = tk.Entry(root, width=30)
entrada.pack(pady=5)

boton = tk.Button(root,text="Mostrar texto", command=escribir_texto)
boton.pack(pady=10)

etiqueta_resultado = tk.Label(root,text="")
etiqueta_resultado.pack(pady=10)
#Ejecutar el bucle principal
root.mainloop()