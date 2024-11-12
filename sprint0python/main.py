from claseHeroe import Heroe            #|importamos las clases que necesitamos para correr el programa
from claseMazmorra import Mazmorra      #|____|
from claseMonstruo import Monstruo      #|


def main(): #declaramos el main
    nombre_heroe = input("Introduce el nombre de tu héroe: ") #ponemos las instrucciones que vamos a pedir al jugador al jugar, como introducir el nombre del héroe.
    heroe = Heroe(nombre_heroe) #Crea una instancia del héroe usando el nombre que el usuario introdujo.
    monstruos = [ #ponemos los monstruos que van a aparecer.
        Monstruo("Creeper", 15, 5, 80),    #Le damos valores a los atributos de  monstruos
        Monstruo("Pillager", 20, 10, 100),
        Monstruo("Wither", 30, 15, 150)
    ]
    mazmorra = Mazmorra(heroe,monstruos) #Crea una instancia de la mazmorra con el héroe y los monstruos.
    mazmorra.jugar() #Llama al método jugar() de la mazmorra, que gestiona el flujo del juego.

if __name__ == "__main__":#Se asegura de que el código dentro del bloque solo se ejecute si el archivo es ejecutado directamente
    main()