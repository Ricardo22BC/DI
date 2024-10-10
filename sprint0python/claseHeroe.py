
class Heroe:
    def __init__(self, nombre): #Establecemos un estado para inicialiar los atributos
        self.nombre = nombre  #Atributos ->self :Es para referirse al objeto mismo.
        self.ataque = 20
        self.defensa = 10
        self.salud = 200
        self.salud_maxima = 200

    def atacar (self, enemigo): #Método para atacar
        print(f"Héroe ataca a {enemigo.nombre}.")
        damage = self.ataque - enemigo.defensa   #el daño es igual al ataque - la defensa del enemigo.
        if damage > 0:   # si el daño es mayor que 0
            enemigo.salud -=damage  # Restamos a la salud del enemigo el daño que hacemos.
            print (f"El enemigo {enemigo.nombre} ha recibido {damage} puntos de daño.")
        else: # si es menor o igual a la defensa del enemigo
            print(f"El enemigo ha bloqueado el ataque ")

    def curarse (self): #Método para curarse
        curacion = 40
        self.salud = min(self.salud + curacion, self.salud_maxima)#Controla que la salud + la curación no supere la salud máxima.
        print(f"Héroe se ha curado. Salud actual: {self.salud}")

    def defenderse(self): #Método para defendersa
        self.defensa += 5 #Aumenta la defensa += a 5
        print(f"Héroe aumenta temporalmente su defensa a {self.defensa}")

    def reset_defensa(self): #Método para volver a la defensa inical
        self.defensa = 10 #devolvemos el valor inical de la defensa
        print(f"La defensa de {self.nombre} vuelve a la normalidad")

    def esta_vivo(self): #Método para decir si esta vivo el héroe
        return self.salud > 0 #Esto es un true o false, donde retornamos si salud es mayor que 0.

