x=7
y=input("Adivine un número entre 0 y 10 ")
y=int(y)



if y==x:
    print("Adivinaste")
else:
    if y>x:
        print("Tu numero es mayor al que debes adivinar ")

    if y<x:
        print("Tu número es menor al que debes adivinar")    