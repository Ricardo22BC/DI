import tkinter as tk
#Función para cambiar el color de la pantalla según la sección que escojamos.
def seleccion_color():
    color = var_color.get()
    if color == "rojo":
        root.config(bg="red")
    if color == "verde":
        root.config(bg="green")
    if color == "azul":
        root.config(bg="blue")
#Creamos ventana
root = tk.Tk()
root.title("Selecciona tu color favorito")
root.geometry("300x200")
#Crear una variable para los Radiobuttons
var_color = tk.StringVar()
var_color.set("rojo")

# Crear los Radiobuttons para seleccionar el color
radio_rojo = tk.Radiobutton(root, text="Rojo", variable=var_color, value="rojo", command=seleccion_color)
radio_rojo.pack(pady=5)

radio_verde = tk.Radiobutton(root, text="Verde", variable=var_color, value="verde", command=seleccion_color)
radio_verde.pack(pady=5)
radio_azul = tk.Radiobutton(root, text="Azul", variable=var_color, value="azul", command=seleccion_color)
radio_azul.pack(pady=5)

# Ejecutar el bucle principal de la ventana
root.mainloop()