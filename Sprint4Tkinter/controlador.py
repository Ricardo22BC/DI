import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel
import time
from modelo import GameModel
from vista import MainMenu, GameView


class GameController:
    def __init__(self, root):
        self.root = root
        self.player_name=None
        self.difficulty=None
        self.model = None
        self.view = None
        self.selected = []
        self.timer_started = False
        self.main_menu = MainMenu(
            self.root,
            start_game_callback=self.start_game_callback,
            show_stats_callback=self.show_stats_callback,
            quit_callback=self.quit_game_callback
        )
    def start_game_callback(self):
        messagebox.showinfo("Jugar","Botón jugar")
        self.show_difficulty_selection()
    def show_stats_callback(self):
        if self.model:
            stats = self.model.load_scores()
            self.main_menu.show_stats(stats)
        else:
            messagebox.showinfo("Estadísticas","Botón estadísticas")
    def quit_game_callback(self):
        messagebox.showinfo("Saliendo","Botón salir")
        self.root.quit()

    # def start_game_callback(self):
    #     self.show_difficulty_selection()
    def show_difficulty_selection(self):
        #Solicitamos dificultad
        difficulty=simpledialog.askstring("Elección de dificultad",
                                          "Seleccione (fácil, medio, difícil)",
                                          parent=self.root)
        #Validamos la entrada
        if difficulty not in ["fácil", "medio", "difícil"]:
            messagebox.showerror("Error","Dificultad no válida")
            return
        #guardamos la dificultad seleccionada
        self.difficulty=difficulty
        #solicitamos el nombre
        self.ask_player_name()

    def ask_player_name(self):
        self.player_name=simpledialog.askstring("Nombre",
                                           "Introduce tu numbre",
                                           parent=self.root)
        if self.player_name:
            self.start_game(self.difficulty)

    def start_game(self, difficulty):
        self.model = GameModel(difficulty, self.player_name)
        self.show_loading_window()
        self.check_images_loaded()

    def show_loading_window(self,message="Cargando imágenes, por favor espere..."):
        # Crear ventana de carga
        self.loading_window = Toplevel(self.root)
        self.loading_window.title("Cargando...")
        tk.Label(self.loading_window, text=message).pack(padx=20, pady=20)

        # Iniciar la descarga de imágenes
        self.model._load_images()
        # Verificar si las imágenes están cargadas
        self.root.after(100, self.check_images_loaded)

    def check_images_loaded(self):
        if self.model.images_are_loaded():
            # Cerrar ventana de carga
            self.loading_window.destroy()
            # Crear el tablero en la vista
            self.view= GameView(
                self.root,
                on_card_click_callback=self.on_card_click,
                update_move_count_callback=self.update_move_count,
                update_time_callback=self.update_time
            )
            self.view.create_board(self.model)
        else:
            # Volver a comprobar en 100 ms
            self.root.after(100, self.check_images_loaded)


    def on_card_click(self, pos):
        # Maneja el evento de clic en una carta del tablero
        if not self.timer_started:
            self.model.start_timer()
            self.timer_started = True
            self.update_time()

        # Almacena la posición de la carta seleccionada
        self.selected.append(pos)
        self.view.update_board(pos, self.model.board[pos])

        # Verifica si se seleccionaron dos cartas
        if len(self.selected) == 2:
            self.handle_card_selection()


    def handle_card_selection(self):
        # Verifica si las cartas seleccionadas coinciden
        pos1, pos2 = self.selected
        if self.model.check_match(pos1, pos2):
            self.view.update_board(pos1, self.model.board[pos1])
            self.view.update_board(pos2, self.model.board[pos2])
            if self.check_game_complete():
                messagebox.showinfo("¡Victoria!", "¡Has encontrado todas las parejas!")
                self.return_to_main_menu()
        else:
            # Espera brevemente antes de ocultar las cartas
            self.root.after(500, lambda: self.view.reset_cards(pos1, pos2))

        # Actualiza el contador de movimientos en la interfaz y limpia la selección
        self.update_move_count(self.model.moves)
        self.selected.clear()


    def update_move_count(self, moves):
        # Actualiza el contador de movimientos en la vista del juego
        if self.view:
            self.view.update_move_count(moves)


    def check_game_complete(self):
        # Verifica si el juego ha sido completado
        return self.model.is_game_complete()


    def return_to_main_menu(self):
        # Vuelve al menú principal y cierra la vista de juego
        if self.view:
            self.view.destroy()
            self.view = None
        self.main_menu = MainMenu(
            self.root,
            start_game_callback=self.show_difficulty_selection,
            show_stats_callback=self.show_stats,
            quit_callback=self.root.quit
        )


    def show_stats(self):
        # Obtiene las estadísticas del modelo y las muestra en la interfaz de estadísticas
        stats = self.model.load_scores()
        self.main_menu.show_stats(stats)


    def update_time(self):
        # Actualiza el temporizador en la interfaz
        if self.view and self.timer_started:
            elapsed_time = self.model.get_time()
            self.view.update_time(elapsed_time)
            # Llama a sí misma cada segundo para mantener el temporizador actualizado
            self.root.after(1000, self.update_time)