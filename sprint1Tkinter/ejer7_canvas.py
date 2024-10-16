import tkinter as tk
from stringprep import b1_set


def dibujar_figuras():
    #Obtener las coordenadas del círculo y rectángulo de los campos de entrada
    a1 =int(entryA1.get())
    b1 =int(entryB1.get())
    a2 =int(entryA2.get())
    b2 =int(entryB2.get())
    c1 =int(entryC1.get())
    d1 = int(entryD1.get())
    c2 = int(entryC2.get())
    d2 = int(entryD2.get())

    #Crear el círculo usando las coordenadas
    canvas.create_oval(a1,b1,a2,b2,fill="green")
    #Crear el rectángulo usando las coordenadas
    canvas.create_rectangle(c1,d1,c2,d2,outline="yellow",width=3)

#Crear la ventana principal
root=tk.Tk()
root.title("Canvas, Circulo y rectángulo")
root.geometry("400x620")

#Crear un canvas
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=20)

#Crear entrada para las coordenadas
labelA1 = tk.Label(root, text="Coordenada Círculo a1:")
labelA1.pack()
entryA1 = tk.Entry(root)
entryA1.pack()

labelB1 = tk.Label(root, text="Coordenada Círculo b1:")
labelB1.pack()
entryB1 = tk.Entry(root)
entryB1.pack()

labelA2 = tk.Label(root, text="Coordenada Círculo a2:")
labelA2.pack()
entryA2 = tk.Entry(root)
entryA2.pack()

labelB2 = tk.Label(root, text="Coordenada Círculo b2:")
labelB2.pack()
entryB2 = tk.Entry(root)
entryB2.pack()

labelC1 = tk.Label(root, text="Coordenada Rectángulo c1:")
labelC1.pack()
entryC1 = tk.Entry(root)
entryC1.pack()

labelD1 = tk.Label(root, text="Coordenada Rectángulo d1:")
labelD1.pack()
entryD1 = tk.Entry(root)
entryD1.pack()

labelC2 = tk.Label(root, text="Coordenada Rectángulo c2:")
labelC2.pack()
entryC2 = tk.Entry(root)
entryC2.pack()

labelD2 = tk.Label(root, text="Coordenada Rectángulo d2:")
labelD2.pack()
entryD2 = tk.Entry(root)
entryD2.pack()
#Botón para que creen las figuras
boton = tk.Button(root, text="Dibujar figuras", command=dibujar_figuras)
boton.pack(pady=10)
#Ejecita el bucle
root.mainloop()

