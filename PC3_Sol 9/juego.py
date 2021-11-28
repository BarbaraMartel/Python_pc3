#Importar modulos
from random import randint

#Variables
x = randint(1, 100)

#Funciones
def adivina(a):
    try:
        b = int(input("Adivine el numero: "))
        if b == a:
            print("HAS GANADO")
        elif b > a:
            print("El numero es INFERIOR al ingresado")
            return adivina(a)
        elif b < a:
            print("El numero es SUPERIOR al ingresado")
            return adivina(a)
    except:
        print("ERROR. Debe ingresar un numero entero")
        return adivina(a)


