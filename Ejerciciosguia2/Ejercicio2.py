# Ejercicio 2: Crear una lista con 10 números enteros cualquiera. Indicar cuál es el número mayor y cuál es el número menor. 
# Si al menos hay 3 números mayores a 100, imprimir esos números, si no, imprimir los números menores a 50 que formen parte de 
# la lista.

lista = [10, 50, 75, 205, 176, 5, 23, 8, 19, 56]

print(max(lista))
print(min(lista))

lista_de_numeros_mayores_a_cien = []
lista_de_numeros_menores_a_cincuenta = []

for i in lista:
    if i >= 100:
        lista_de_numeros_mayores_a_cien.append(i)
    if i <= 50:
        lista_de_numeros_menores_a_cincuenta.append(i)

if len(lista_de_numeros_mayores_a_cien) == 3:
    print(lista_de_numeros_mayores_a_cien)
else:
    print(lista_de_numeros_menores_a_cincuenta)
