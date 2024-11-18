import tkinter as tk
from tkinter import simpledialog, Toplevel
from PIL import Image, ImageTk


class GameView:
    def __init__(self, on_card_click_callback, update_move_count_callback, update_time_callback):
        self.window=None
        self.labels={}
        self.on_card_click_callback = on_card_click_callback
        self.update_move_count_callback=update_move_count_callback
        self.update_time_callback=update_time_callback

    def create_board(self, model):
        #Creamos la ventana de la vista del juego
        self.window = Toplevel()
        self.window.title("Juedo de Memoria")

        #Tamaño del tablero según el modelo
        board_size= model.board_size

        #Creamos el tablero con las celdas de las cartas
        for row in range(model.board_size):
            for col in range(model.board_size):
                pos = row * model.board_size + col
                label = tk.Label(self.window, text="t", width=10, height=5,bg="gray")
                label.grid(row=row, column=col)
                label.bind("<Button-1>", lambda event, pos=pos: self.on_card_click_callback(event, pos))

                self.labels[pos]=label
        # Añadir las etiquetas para el contador de movimientos
        self.move_count_label = tk.Label(self.window, text="Movimientos: 0", font=("Arial", 14))
        self.move_count_label.grid(row=board_size, column=0, columnspan=board_size//2, padx=10, pady=5)

        # Añadir las etiquetas para el temporizador
        self.timer_label = tk.Label(self.window, text="Tiempo: 0", font=("Arial", 14))
        self.timer_label.grid(row=board_size + 1, column=0, columnspan=board_size//2, padx=10, pady=5)
    def on_card_click(self, pos):
        # Llamar al callback del controlador al hacer clic en una carta
        self.on_card_click_callback(pos)

    def update_board(self, pos, image_id):
        # Actualizar la imagen de una carta específica en el tablero
        if pos in self.labels:
            label = self.labels[pos]
            image_path = f"images/{image_id}.jpg"  # Cambia esto según tu estructura de archivos
            image = Image.open(image_path)

            # Convertir la imagen al formato PhotoImage para Tkinter
            tk_image = ImageTk.PhotoImage(image)

            # Actualizar el label con la imagen
            label.config(image=tk_image)
            label.image = tk_image

    def reset_cards(self, pos1, pos2):
        # Restaurar las cartas a su imagen oculta
        if pos1 in self.labels and pos2 in self.labels:
            self.labels[pos1].config(text="t", bg="gray")
            self.labels[pos2].config(text="t", bg="gray")

    def update_move_count(self, moves):
        # Actualizar el contador de movimientos en la interfaz
        self.move_count_label.config(text=f"Movimientos: {moves}")

    def update_time(self, time):
        # Actualizar el temporizador en la interfaz
        self.timer_label.config(text=f"Tiempo: {time}s")

    def destroy(self):
        # Cerrar la ventana del juego y limpiar las etiquetas
        if self.window:
            self.window.destroy()
            self.labels.clear()

class MainMenu:
    def __init__(self,root, start_game_callback, show_stats_callback, quit_callback):

        #Ventana principal
        self.root = root
        self.root.title("Menú principal")

        #Botón jugar
        self.jugar_button= tk.Button(self.root, text="Jugar", command=start_game_callback)
        self.jugar_button.pack(pady=10)
        #Botón estadísticas
        self.est_button= tk.Button(self.root, text="Estadísticas", command=show_stats_callback)
        self.est_button.pack(pady=10)
        #Botón salir
        self.quit_button= tk.Button(self.root, text="Salir", command=quit_callback)
        self.quit_button.pack(pady=10)

    def start_game(self):
       #Solicita el nombre del jugador y comienza el juego.
        player_name = self.ask_player_name()
        if player_name:
            self.start_game_callback(player_name)

    def ask_player_name(self):
        #Muestra un cuadro de diálogo para pedir el nombre del jugador.
        return simpledialog.askstring("Nombre del Jugador", "Por favor, ingrese su nombre:")

    def show_stats(self,stats):
        # Crear una nueva ventana Toplevel para mostrar las estadísticas
        stats_window = Toplevel()
        stats_window.title("Estadísticas de Jugadores")
        stats_window.geometry("400x400")
        stats_window.resizable(False, False)

        # Título principal
        title_label = tk.Label(stats_window, text="Mejores Puntuaciones", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Crear una sección para cada nivel de dificultad
        for difficulty in ["facil", "medio", "dificil"]:
            # Añadir subtítulo para el nivel de dificultad
            difficulty_label = tk.Label(stats_window, text=f"Dificultad: {difficulty.capitalize()}",
                                        font=("Arial", 14, "bold"))
            difficulty_label.pack(anchor="w", padx=20, pady=(10, 5))

            # Obtener las puntuaciones para el nivel de dificultad
            difficulty_stats = stats.get(difficulty, [])

            # Verificar si hay puntuaciones disponibles para esta dificultad
            if difficulty_stats:
                for record in difficulty_stats:
                    # Mostrar el nombre del jugador y el número de movimientos
                    player_label = tk.Label(
                        stats_window,
                        text=f"{record['name']} - Movimientos: {record['moves']}",
                        font=("Arial", 12)
                    )
                    player_label.pack(anchor="w", padx=30)
            else:
                # Mensaje en caso de que no haya puntuaciones en ese nivel
                no_record_label = tk.Label(stats_window, text="Sin puntuaciones disponibles",
                                           font=("Arial", 12, "italic"))
                no_record_label.pack(anchor="w", padx=30)

        # Botón de cerrar
        close_button = tk.Button(stats_window, text="Cerrar", command=stats_window.destroy)
        close_button.pack(pady=20)
