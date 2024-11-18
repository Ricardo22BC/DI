import tkinter as tk
from controlador import GameController
from modelo import GameModel
if __name__ == "__main__":
    #Inicializa la ventana principal de Tkinter
    root=tk.Tk()
    root.title("Juego de memoria")
    root.geometry("600x700")
    #Inicia el controlador
    controller = GameController(root)
    #Crea el menú principal y pasa las funciones del controlador
    #menu = MainMenu(root,controller.start_game_callback,controller.show_stats_callback,controller.quit_game_callback)
    #Ejecuta el bucle principal Tkinter
    root.mainloop()