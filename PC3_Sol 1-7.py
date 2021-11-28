from math import pi

#Solucion 1

def longitud():
    cadena = input("Ingrese una oracion: ")
    c_lista = cadena.strip().split(" ")
    return print(f"Longitud de la última palabra: {len(c_lista[-1])}")

longitud()

#Solucion 2

def primera_mayu():
    oracion = input("Ingrese una oracion: ")
    return print(oracion.title().split(" "))

primera_mayu()

#Solucion 3 

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        
    def area_circulo(self):
        area_cir = pi * self.radio ** 2
        print("El area es {:.2f}".format(area_cir))

Circulo1 =  Circulo(7)
Circulo1.area_circulo()

#Solucion 4

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
        
    def area_rectangulo(self):
        area_rec = self.largo * self.ancho
        print("El area del rectángulo es {}".format(area_rec))

Rectangulo1 =  Rectangulo(12, 18)
Rectangulo1.area_rectangulo()

#Solucion 5

class Alumno:
    def __init__(self, nombre, nro_registro):
        self.nombre = nombre
        self.nro_registro = nro_registro
        
    def Display(self):
        print("Nombre: {}".format(self.nombre))
        print("Numero de registro: {}".format(self.nro_registro))

    def setAge(self):
        edad = input("Ingrese la edad del estudiante: ")
        print("Edad: {}".format(edad))

    def setNota(self):
        nota = input("Ingrese la nota del estudiante: ")
        print("Nota: {}".format(nota))

Alumno1 = Alumno('Juan Hernandez', 3456)
Alumno1.Display()
Alumno1.setAge()
Alumno1.setNota()

#Solucion 6

try:
    calificaciones = input("Ingrese sus calificaciones separadas por coma: ")
    lista_cali = calificaciones.split(",")

    for x in lista_cali:
        entero = int(x)
        print(f"Su calificacion es {entero}")
except:
    print("Error de tipeo. Sus calificaciones no pueden ser convertidas.")

#Solucion 7

def pascal(filas):
    fila = [1]
    cero = [0]

    for i in range(filas):
        print(fila)

        fila = [i + d for i, d in zip(fila + cero, cero + fila)]

f = int(input("Ingresa el numero de filas de tu triangulo: "))
pascal(f)


