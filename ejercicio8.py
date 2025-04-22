try:

    peso = float(input("ingrese tu peso en kg:"))

    altura = float(input("ingresa tu altura en metros:"))

    IMC = peso / (altura ** 2)

    if IMC < 18.5:
        print("bajo de peso")

    elif IMC >= 18.5 and IMC <= 24.9:
        print("peso normal")

    elif IMC >= 25 and IMC <= 29.9:
        print("sobrepeso")

    elif IMC >= 30:
        print("obesidad")
        
except ValueError:
    print("ingresa un numero correcto")
