from claseTesoro import Tesoro #importamos Tesoro de la clase Tesoro


class Mazmorra:
    def __init__(self, heroe,monstruos): #Establecemos un estado para inicialiar los atributos
        self.heroe = heroe #Atributos ->self:Es para referirse al objeto mismo.
        self.monstruos = monstruos
        self.tesoro = Tesoro()

    def jugar(self): #Método jugar
        #Mensaje para decir que el héroe entra en la mazmorra
        print(f"Héroe {self.heroe.nombre} entra en la mazmorra")

        for monstruo in self.monstruos:  #Hacemos un bucle en el que vamos a estar hasta que acabemos con todos los monstruos.
            print(f"Te has encontrado con un {monstruo.nombre}")
            self.enfrentar_enemigo(monstruo) #Llamamos al método enfrentar_enemigo

            if not self.heroe.esta_vivo(): # Si no está vivo, (llamando al método esta vivo)
                print(f"Héroe ha sido derrotado en la mazmorra.") #Si no está vivo mensaje que fue derrotado.
                return

            self.buscar_tesoro() # Si acabamos con todos los monstruos llamamos al método buscar_tesoro.
            #Mensaje que hemos derotado a todos los monstruos.
        print(f"{self.heroe.nombre} ha derrotado a todos los monstruos y ha conquistado la mazmorra!")

    def enfrentar_enemigo(self, enemigo): #Método para una lista donde tenemos opciones para enfrentarnos a los enemigos.
        while enemigo.esta_vivo() and self.heroe.esta_vivo(): #Mientras enemigo siga vivo y heroe este vivo. Tenemos estas opciones.
            print("¿Qué deseas hacer")
            print("1.Atacar")
            print("2.Defender")
            print("3.Curarse")
            accion = input("Elige una opción ")  #accion, mensaje para elegir acción

            if accion == "1":  #opciones
                self.heroe.atacar(enemigo) #Llamamos al metodo atacar de la clase heroe
            elif accion =="2":
                self.heroe.defenderse()#Llamamos al metodo defenderse de la clase heroe
            elif accion == "3":
                self.heroe.curarse() #Llamamos al metodo curarse de la clase heroe
            else: # Si no ponemos el número correspondiente salta mensaje.
                print ("Opción no válida")
                continue # continuamos

            if enemigo.esta_vivo(): # si el enemigo sigue vivo en en el método esta_vivo
                enemigo.atacar(self.heroe)  # Enemigo ataca a heroe
                self.heroe.reset_defensa() #Llamamos al método de heroe , reset_defensa.

    def buscar_tesoro(self): #Método buscas tesoro que se inicia cuando acabamos con todos los monstruos
        print("Buscando tesoro...")
        self.tesoro.encontrar_tesoro(self.heroe) #Llamamos al metodo encontrar tesoro de Tesoro, que lo hace el heroe.
