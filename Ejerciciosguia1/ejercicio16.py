# Ejercicio 16: Crear un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada 
# un nuevo dato debe imprimirse el contenido del diccionario.

diccionario = {}

continuar = "si"

while continuar.lower() == "si":
    clave = input("¿Qué dato querés ingresar?: ")
    valor = input(f"Ingrese valor para {clave}: ")
    diccionario[clave] = valor
    print(diccionario)
    continuar = input("¿Quiere continuar?: ")
    


    
