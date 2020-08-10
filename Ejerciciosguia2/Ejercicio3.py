# Ejercicio 3: Pedir al usuario que ingrese por teclado 2 números, si el primero es menor que el segundo imprimir 
# la resta entre el segundo y el primero, si el primero es mayor que el segundo imprimir la suma de ambos, y si son iguales
#  imprimir su producto.

numero_uno = int(input("Ingrese un número: "))
numero_dos = int(input("Ingrese otro número: "))


if numero_uno < numero_dos:
    print(numero_dos - numero_uno)
elif numero_uno > numero_dos:
    print(numero_uno + numero_dos)
else:
    print(numero_uno * numero_dos)
