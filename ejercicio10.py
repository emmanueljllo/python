try:

    numero = int(input("ingresa un numero:"))

    if 1 <= numero <= 10: 
        print("numero dentro del rango")

    else: 
        print("numero fuera del rango")

except ValueError:
        print("ingresa un nunero correcto")
