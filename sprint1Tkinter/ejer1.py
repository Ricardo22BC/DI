import tkinter as tk

def cambio_texto():
    etiqueta3.config(text="Empezamos con Tkinter.")

root = tk.Tk()
root.title("Mi primera ventana")
root.geometry("300x200")


etiqueta1 = tk.Label(root, text="¡Hola!")
etiqueta1.pack(pady=10)

etiqueta2= tk.Label(root, text="Ricardo")
etiqueta2.pack(pady=10)

etiqueta3= tk.Label(root, text="Texto a cambiar")
etiqueta3.pack(pady=10)

boton= tk.Button(root, text="[X]", command=cambio_texto )
boton.pack(pady=5)

root.mainloop()
