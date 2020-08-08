# Ejercicio 13: Crear un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

monedas = {
    "Euro" : "€",
    "Dollar" : "$",
    "Yen" : "¥",
}

divisa = str(input("¿Cuál es su divisa?: "))


if divisa == "€":
    print("€")
elif divisa == "$":
    print("$")
elif divisa == "¥":
    print("¥")
else:
    print("No se reconoce la divisa")


#otra forma

monedas = {
    "Euro" : "€",
    "Dollar" : "$",
    "Yen" : "¥",
}

divisa = str(input("""
Elija una divisa y luego pulse enter:
    - presione E o e para Euro 
    - presione D o d para Dollar
    - presione Y o y para Yen
"""))


if divisa.lower() == "e":
    print(monedas["Euro"])
elif divisa.lower() == "d":
    print(monedas["Dollar"])
elif divisa.lower() == "y":
    print(monedas["Yen"])
else:
    print("No se reconoce la divisa")

