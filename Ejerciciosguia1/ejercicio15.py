# Ejercicio 15: Crear un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
# {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura 
# en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, 
# y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

creditos = {
    "Matemáticas": 6,
    "Física": 4,
    "Química": 5,
}


# Primer forma de resolverlo:

total = 0
for materia in creditos:
    print(f"La asignatura {materia} tiene {creditos[materia]} créditos")
    #print("La asignatura " + materia + " tiene " +  str(creditos[materia]) + " créditos")
    #print("La asignatura {} tiene {} créditos".format(materia, creditos[materia]))
    total = total + creditos[materia]

print(f"El total de créditos del curso es: {total}")
print()


# Segunda forma de resolverlo:

totalsegforma = 0
for materia, credito in creditos.items():
    print(f"La asignatura {materia} tiene {credito} créditos")
    totalsegforma += credito

print(f"El total de créditos del curso es: {totalsegforma}")




"""mates = creditos["Matemáticas"]
fisis = creditos["Física"]
quim = creditos["Química"]"""

#creditos["Matemáticas"]
#print(f"Matemáticas tiene {mates} créditos")