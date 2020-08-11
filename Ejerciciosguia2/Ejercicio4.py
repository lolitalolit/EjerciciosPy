# Ejercicio 4: Ingresar 6 números por teclado, preferentemente enteros, ordenarlos de manera creciente e imprimirlos por pantalla.

lista = []


for i in range(6):
    numero_ingresado = int(input("Ingrese un número: "))
    lista.append(numero_ingresado)
    

lista.sort()

for numero_ingresado in lista:
    print(numero_ingresado)
