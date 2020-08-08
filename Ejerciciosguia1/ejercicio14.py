# Ejercicio 14: Crear un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo 
# guarde en un diccionario. Después debe mostrar por pantalla el mensaje.


nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuál es tu edad? ")
direccion = input("¿Cuál es tu dirección? ")
tel = input("¿Cuál es tu teléfono? ")


# Una forma de hacerlo

datos = {
    "nombre" : nombre,
    "edad" : edad,
    "direccion" : direccion,
    "telefono" : telefono,
}

print(datos)

# Otra forma

datos_usuario = {}
datos_usuario["Nombre"] = nombre
datos_usuario["Edad"] = edad
datos_usuario["Dirreción"] = direccion
datos_usuario["Teléfono"] = tel

print(datos_usuario)