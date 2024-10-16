import tkinter as tk



def texto():
    texto1 = entrada.get()
    etiqueta_resultado.config(text="Has escrito: " + texto1)

def borrar():
    entrada.delete(0,tk.END)
    etiqueta_resultado.config(text="")

#Crear la ventana principal
root = tk.Tk()
root.title("Frame")
root.geometry("300x500")

#Crear un frame
frame1 = tk.Frame(root, bg="grey", bd=2, relief="sunken")
frame1.pack(padx=20, pady=20, fill='both', expand=True)

#Agregamos widgets al frame
etiqueta_1 = tk.Label(frame1, text="Etiqueta 1 dentro del Frame")
etiqueta_1.pack(pady=10)

etiqueta_2 = tk.Label(frame1, text="Etiqueta 2 dentro del Frame")
etiqueta_2.pack(pady=10)

entrada = tk.Entry(frame1, width=30)
entrada.pack(pady=5)

frame2 = tk.Frame(root, bg="grey", bd=2, relief="sunken")
frame2.pack(padx=20, pady=20, fill='both', expand=True)


boton_mostrarTexto = tk.Button(frame2,text="Mostrar texto", command=texto)
boton_mostrarTexto.pack(pady=10)

etiqueta_resultado = tk.Label(frame2,text="")
etiqueta_resultado.pack(pady=10)

boton_borrar = tk.Button(frame2,text="Borrar texto", command=borrar)
boton_borrar.pack(pady=10)

root.mainloop()