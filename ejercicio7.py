try:
    numero1 = int(input("ingrese numero 1:"))

    numero2 = int(input("ingrese numero 2:"))

    if numero1 > numero2:
        print("el numero 1 es mayor que el numero 2")
        
    elif numero1 < numero2:
        print("el numero 2 es mayor que el numero 1")

    elif numero2 == numero1:
        print("numeros iguales")

except ValueError:
      print("ingresa un numero valido")

