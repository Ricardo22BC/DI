import tkinter as tk

def mostrar_seleccion():
    # funcion para mostrar el estado de las 3 casillas de verificación
    selection1 = "Seleccionada" if var_check1.get() else " No seleccionado"
    selection2 = "Seleccionada" if var_check2.get() else " No seleccionado"
    selection3 = "Seleccionada" if var_check3.get() else " No seleccionado"
    #Actualiza la etiqueta con el estado de las casillas
    etiqueta.config(text=f"Checkbutton: {selection1},{selection2},{selection3}")
#Crear ventana
root = tk.Tk()
root.title("Checkbutton")
root.geometry("300x200")
#Crear variables para el Checkbutton
var_check1 = tk.IntVar()
var_check2 = tk.IntVar()
var_check3 = tk.IntVar()
#Crear checkbuttons
check1 = tk.Checkbutton(root, text="Leer",variable=var_check1, command=mostrar_seleccion)
check1.pack(pady=10)

check2 = tk.Checkbutton(root, text="Deporte",variable=var_check2, command=mostrar_seleccion)
check2.pack(pady=10)

check3 = tk.Checkbutton(root, text="Música",variable=var_check3, command=mostrar_seleccion)
check3.pack(pady=10)
#Etiqueta del estado
etiqueta = tk.Label(root, text="Checkbutton: ")
etiqueta.pack(pady=10)
#Ejecutar
root.mainloop()