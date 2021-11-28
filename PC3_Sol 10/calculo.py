import operaciones


while True:
    print("""Hola. Que deseas hacer? 
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Salir""")

    opcion = input("Opcion: ")

    if opcion == '1':
        a = int(input("Ingrese un numero: "))
        b = int(input("Ingrese un numero: "))
        resultado_suma = operaciones.sumar(a,b)
        print(f"La suma de los numeros es {resultado_suma}")

    if opcion == '2':
        a = int(input("Ingrese un numero: "))
        b = int(input("Ingrese un numero: "))
        resultado_resta = operaciones.restar(a,b)
        print(f"La diferencia de los numeros es {resultado_resta}")

    if opcion == '3':
        a = int(input("Ingrese un numero: "))
        b = int(input("Ingrese un numero: "))
        resultado_multi = operaciones.multiplicar(a,b)
        print(f"El producto de los numeros es {resultado_multi}")

    if opcion == '4':
        a = int(input("Ingrese un numero: "))
        b = int(input("Ingrese un numero: "))
        resultado_div = operaciones.dividir(a,b)
        print(f"La division de los numeros es {resultado_div}")

    elif opcion == '5':
        print("Saliste del menu")
        break