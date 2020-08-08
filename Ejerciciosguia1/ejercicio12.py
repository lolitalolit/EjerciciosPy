# Ejercicio 12: Crear un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y 
# muestre por pantalla su producto escalar.

vector1 = (1, 2, 3)
vector2 = (-1, 0, 2)

# Primer forma de resolverlo

resultado = 0
longitud_vector = len(vector1)

for i in range(longitud_vector):
    resultado = resultado + vector1[i] * vector2[i]
    #resultado += vector1[i] * vector2[i]
  
print(resultado)
print()

# Segunda forma de resolverlo


c = vector1[0] * vector2[0] #-1
d = vector1[1] * vector2[1] #0
e = vector1[2] * vector2[2] #6

producto_escalar = c + d + e

print(producto_escalar)
