

def sumar(a,b):
    try:
        return a+b
    except(TypeError, ValueError, NameError):
        print("Tipo de dato no valido")

def restar(a,b):
    try:
        return a-b
    except(TypeError, ValueError, NameError):
        print("Tipo de dato no valido")

def multiplicar(a,b):
    try:
        return a*b
    except(TypeError, ValueError, NameError):
        print("Tipo de dato no valido")

def dividir(a,b):
    try:
        return a/b
    except(TypeError, ValueError, NameError):
        print("Tipo de dato no valido")
    except(ZeroDivisionError):
        print("No es posible dividir entre 0")



