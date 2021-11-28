from random import randint

x = []

def random_num():
    for r in range(20):
        num_aleatorios = randint(0, 100)
        x.append(num_aleatorios)
    return x

def mostrar():
    return print(x)

def ordenar():
    x.sort()
    return print(x)

