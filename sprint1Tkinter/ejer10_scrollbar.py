import tkinter as tk

def insertar_texto():
    cuadro_texto.insert(tk.END,
    """    En el vasto universo del desarrollo web,
    una herramienta que destaca por su versatilidad 
    y eficiencia es tkinter en Python. Esta librería,
    que forma parte de la biblioteca estándar
    de Python, brinda a los desarrolladores la capacidad
    de crear interfaces gráficas 
    de usuario de manera sencilla y elegante.
     
    Al adentrarse en el mundo de tkinter, 
    se descubre un sinfín de posibilidades para dar vida 
    a aplicaciones interactivas y funcionales.
     
    A través de sus numerosos widgets y funciones, 
    es posible diseñar desde simples ventanas 
    emergentes hasta complejos sistemas con botones, 
    menús desplegables, cuadros de texto y mucho más.
    Una de las características más destacadas de tkinter
    es su capacidad para vincular funciones a los distintos
    elementos de la interfaz, lo que permite crear interacciones 
    dinámicas y personalizadas. Mediante la asignación de eventos 
    a botones o campos de entrada, es posible controlar el flujo 
    de la aplicación y responder a las acciones del usuario de manera eficaz.
    
    Además, gracias a su integración con Python, tkinter ofrece
    una amplia gama de posibilidades para el desarrollo de 
    aplicaciones completas. Desde programas simples hasta 
    proyectos más ambiciosos, esta potente herramienta 
    proporciona las bases necesarias para materializar 
    ideas creativas y funcionales.""")

#Crear la ventana principal
root=tk.Tk()
root.title("Scrollbar")
root.geometry("400x300")

#Crear un Frame para contener el Text y el Scrollbars
frame = tk.Frame(root)
frame.pack(fill='both', expand=True)

#Crear el text
cuadro_texto = tk.Text(frame, wrap='none') #wrap='none' para evitar salto de línea automático
cuadro_texto.grid(row=0, column=0, sticky='nsew') #Usamos grid para mejor control del layout

#Scrollbar vertical
scroll_vert = tk.Scrollbar(frame,orient='vertical', command=cuadro_texto.yview)
scroll_vert.grid(row=0, column=1, sticky='ns') #Alineamos a la derecha del Text
cuadro_texto.config(yscrollcommand=scroll_vert.set)

# Scrollbar horizontal
scroll_hor = tk.Scrollbar(frame, orient='horizontal', command=cuadro_texto.xview)
scroll_hor.grid(row=1, column=0, sticky='ew')  # Alineamos abajo del Text
cuadro_texto.config(xscrollcommand=scroll_hor.set)

#Ajustar el tamaño del frame y el Text al tamaño de la ventana
frame.grid_rowconfigure(0,weight=1)
frame.grid_columnconfigure(0,weight=1)

insertar_texto()

#Ejecutar el bucle
root.mainloop()