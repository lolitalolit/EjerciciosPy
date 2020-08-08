#Ejercicio 10: Escribir un programa que almacene todas las letras del abecedario y luego elimine las vocales 
# y nos devuelva una lista sin las vocales, sin modificar la original.

abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v",
 "w", "x", "y", "z"]


#creo copia
abecedario2 = abecedario.copy()

#quiero modificar abecedario2 y no la original. asi que operaré en la copia. Hay que iterar.

for i in abecedario2:
    vocales = ["a", "e", "i", "o", "u"]
    for vocal in vocales:
        if i == vocal:
            abecedario2.remove(i)
print(abecedario)
print()
print(abecedario2)

