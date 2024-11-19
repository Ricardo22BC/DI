import threading
import time
import random
import datetime

import recursos
from recursos import descargar_imagen

class GameModel:
    def __init__(self, difficulty, player_name, cell_size=100):
        self.difficulty=difficulty
        self.player_name= player_name
        self.cell_size = cell_size
        self.moves = 0
        self.pairs_found = 0
        self.start_time = None
        self.images_loaded = False

        #Determina el tamaño en función a la dificultad elegida.
        #"facil" se asocia con 4 que representa un tablero de 4x4 celdas
        #Después devolvemos el tablero correspondiente a la dificultad
        self.board_size={"fácil":4,"medio":6,"difícil":8}.get(difficulty)
        self.total_pairs = (self.board_size ** 2) // 2
        self.board={}
        self.images={}
        self.hidden_image = None
        self.images_loaded = threading.Event()

        # self.pairs_found=0
        self.url_base = "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/images/"
        # Debug: Verifica que self.url_base está correctamente asignado
        print(f"URL Base: {self.url_base}")

        self._generate_board()
       # self._load_images()

        self.start_time=None
        self.moves=0


    def _generate_board(self):
        #Calcula la cantidad de pares de cartas que se necesitan para llenar el tablero
        #self.board_size representa el tamaño de un lado del tablero el cual
        #elevamos al cuadrado para obtener el número total de celdas.
        #Cada carta tiene una pareja,se divide entre 2, obteniendo el total de pares de cartas.
        num_pairs = (self.board_size ** 2) // 2

        #Crea una lista que contiene identificadores para cada parte en el tablero.
        #Objetivo tener pares, de modo que cada número aparezca dos veces.
        #'range(num_pairs * 2)'-> genera una secuencia de números desde 0 hasta num_pairs
        #*2-1. Esto representa el número total de cartas(doble de num_pairs).
        #'i//2'->Toma cada número de la secuencia y lo divide por 2 para crear pares idéticos.
        self.board = [i // 2 for i in range(num_pairs * 2)]
        #Mezcla la disposición de las cartas
        random.shuffle(self.board)

    #Definimos la función y su hilo interno
    def _load_images(self):
         #funcion interna que será ejecutada en un hilo independiente
        def load_images_thread(model):
            try:
                # Usa el atributo url_base para cargar la imagen oculta
                hidden_image = descargar_imagen(f"{model.url_base}OIP.jpeg", (model.cell_size, model.cell_size))

                # Verificar que la imagen oculta se ha descargado
                if hidden_image is None:
                    print("Error: No se pudo descargar la imagen oculta")
                    return

                # Obtener identificadores únicos de las imágenes del tablero
                unique_image_ids = list(set(model.board))  # Usar set para evitar duplicados

                # Descargar cada imagen con los identificadores únicos
                for image_id in unique_image_ids:
                    image_url = f"{model.url_base}{image_id}.png"
                    print(image_url)
                    # Asegúrate de que el tamaño sea una tupla
                    size = (model.cell_size, model.cell_size) if isinstance(model.cell_size, int) else model.cell_size
                    self.images[image_id] = descargar_imagen(image_url, size)

                    if self.images[image_id] is None:
                    #if self.images is None:
                        print(f"Error: No se pudo descargar la imagen {image_id}.png")
                        continue  # Si falla la descarga, pasa a la siguiente imagen


                # Indicar que todas las imágenes se han descargado y están listas
                print("Todas las imágenes han sido cargadas correctamente.")
                model.images_loaded.set()
            except Exception as e:
                print(f"Error en el hilo de carga de imágenes: {e}")
                model.images_loaded.set()  # Asegurarse de que el evento se marque aunque ocurra un error

                # Iniciar el hilo de carga de imágenes en segundo plano
        threading.Thread(target=load_images_thread, args=(self,), daemon=True).start()

        # Esperar explícitamente hasta que todas las imágenes estén cargadas
        self.images_loaded.wait()  # Esto bloquea el hilo principal hasta que se termine de cargar todo
        print("Todas las imágenes han sido cargadas.")


    def images_are_loaded(self):
        #Verifica si todas las imágenes del juego han sido cargadas.
        # print(len(self.images)== {"fácil":4,"medio":6,"difícil":8}.get(self.difficulty)**2//2)
        # return len(self.images)== {"fácil":4,"medio":6,"difícil":8}.get(self.difficulty)

        print(f"Cantidad de imágenes cargadas: {len(self.images)}")  # Depuración
        # Aquí verificamos si realmente se han cargado imágenes en el diccionario
        if len(self.images) == {"fácil": 4, "medio": 6, "difícil": 8}.get(self.difficulty) ** 2 // 2:
            print("Las imágenes están completamente cargadas.")
            return True
        else:
            print("Las imágenes aún no están completamente cargadas.")
            return False

    def start_timer(self):
        #Reinicia el temporizador del juego
        self.start_time= time.time()

    def get_time(self):
        #Devuelve el tiempo en segudnos desde que comenzó el juego
        if self.start_time is None:
            return 0
        return int(time.time()-self.start_time)

    def check_match(self,pos1,pos2):
        #Verifica si dos posiciones del tablero contiene la misma imagen indicando una coincidencia.
        self.moves +=1 #Incrementa el contador de movimientos
        if self.board[pos1] == self.board[pos2]: #pos1 es = a pos2 del tablero coinciden
           self.pairs_found +=1 #Incrementamos el contador si se encuentra coincidencia y devolvemos True.
           return True
        return False

    def is_game_complete(self):
        #Verifica si se encontraron toda las parejas del tablero
        #El número de parejas encontrado equivale a la mitad del tamaño total
        #del tablero, el juego se considera completado.
        return self.pairs_found == (self.board_size ** 2) //2

    def save_score(self):
        #Guardamos la puntuación del juador en un .txt
        score_data={
            "name": self.player_name,
            "difficulty": self.difficulty,
            "moves": self.moves,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        scores = self.load_scores()

        scores[self.difficulty].append(score_data)
        scores[self.difficulty]= sorted(scores[self.difficulty], key=lambda x: x["moves"])[:3]

        # Guardar las mejores puntuaciones en el archivo
        with open("ranking.txt", "w") as f:
            for diff, records in scores.items():
                for record in records:
                    f.write(f"{record['name']},{diff},{record['moves']},{record['date']}\n")

    def load_scores(self):
        #carga y devuelve las puntuaciones desde el archivo ranking.txt.
        scores = {"facil": [], "medio": [], "dificil": []}
        try:
            with open("ranking.txt", "r") as f:
                for line in f:
                    name, difficulty, moves, date = line.strip().split(",")
                    scores[difficulty].append({
                        "name": name,
                        "difficulty": difficulty,
                        "moves": int(moves),
                        "date": date
                    })
        except FileNotFoundError:
            pass  # Si el archivo no existe, devuelve un diccionario vacío
        return scores
