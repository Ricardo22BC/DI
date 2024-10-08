from operaciones import suma,resta,multi,div
def solicitar_numeros():
    while True:
        try:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))
            return num1, num2
        except ValueError:
            print("Introduce un número válido")

def seleccionar_operacion():
    print("\nSelecciona la operación.")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        opcion = input("Número de la operación (1-2-3-4). ")
        if opcion in ["1","2","3","4"]:
            return opcion
        else:
            print("No válido")

def calculadora():
    otra="s"
    while otra == "s":
        num1, num2 = solicitar_numeros()
        operacion =seleccionar_operacion()

        if operacion == "1":
            result = suma(num1,num2)
            print(f"La suma es: {result}")
        elif operacion == "2":
            result = resta(num1,num2)
            print(f"La resta da: {result}")
        elif operacion == "3":
            result = multi(num1,num2)
            print(f"La multiplicación es:{result}")
        elif operacion == "4":
            result = div(num1,num2)
            print(f"La división da: {result}")

        otra = input("Otra operación ? (s/n)")
        while otra not in ["s","n"]:
            otra = input("Respuesta incorrecta.")

if __name__ == "__main__":
    calculadora()



