class Monstruo:
    def __init__(self, nombre, ataque, defensa, salud):#Establecemos un estado para inicialiar los atributos
        self.nombre = nombre #Atributos ->self :Es para referirse al objeto mismo.
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud

    def atacar(self, heroe): #Método para el ataque del mosntruo
        print(f"El monstruo {self.nombre} ataca a {heroe.nombre}")
        damage = self.ataque - heroe.defensa #El daño es igual, al ataque del monstruo - la defensa de heroe.
        if damage > 0: #Si el daño es mayor a 0
            heroe.salud -= damage #Restamos a la salud del heroe el daño que recibimos del monstruo.
            print(f"El héroe {heroe.nombre} ha recibido {damage} puntos de daño")
        else: #Si es menor que 0, hemos bloqueado el ataque
            print(f"El héroe ha bloqueado el ataque.")

    def esta_vivo(self): # Método para saber si sigue vivo el monstruo
        return self.salud >0 #Esto es un true o false, donde retornamos si salud es mayor que 0.
