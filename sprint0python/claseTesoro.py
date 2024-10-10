import random


class Tesoro:
    def __init__(self): #Establecemos un estado para inicialiar los atributos
        self.beneficios = ["aumento de ataque","aumento de defensa","restauración de salud"] #Atributos ->self :Es para referirse al objeto mismo.
    def encontrar_tesoro(self,heroe): #Método para encontrar el tesoro
        beneficio = random.choice(self.beneficios) #declaramos beneficio que coje un objeto random de lo declarado en beneficios.
        print(f"Héroe ha encontrado un tesoro {beneficio}")  #Si el jugador encuentra un tesoro salta mensaje
        if beneficio == "aumento de ataque ":  # si es un benefico de aumento de ataque recibe + 5 en ataque.
            heroe.ataque +=5
            print(f"El ataque de {heroe.nombre}  aumenta a {heroe.ataque}")#Mensaje que decimos lo que aumenta el ataque
        elif beneficio == "aumento de defensa":# si es un benefico de aumento de defensa recibe + 5 en defensa.
            heroe.defensa += 5
            print(f"La defensa de {heroe.nombre} aumenta a {heroe.defensa}")#Mensaje para la defensa.
        elif beneficio == "restauración de salud":# si es un benefico de restauración de salud, restaura por completo su salud.
            heroe.salud = 200
            print(f"La salud de {heroe.nombre} ha sido restaurada a {heroe.salud}")#Mensaje para decir que fue resturada la salud.
