# Ejercicio 1: Pedir al usuario que ingrese un mensaje cualquiera, si el mensaje tiene más de 100 caracteres imprimirlo 
# por pantalla, si tiene entre 50 y 100 caracteres imprimirlo al revés, si no se cumple ninguna de las opciones anteriores, 
# por pantalla devolver un mensaje que diga "su mensaje es demasiado corto".


mensaje = input("Ingrese aquí su mensaje: ")


if len(mensaje) >= 100:
    print(mensaje)
elif len(mensaje) > 50 and len(mensaje) < 100:
    print(mensaje[::-1])
else: 
    print("Su mensaje es demasiado corto")

# Otra forma

if len(mensaje) > 100:
    print(mensaje)
elif 50 <= len(mensaje) < 100:
    print(mensaje[::-1])
else: 
    print("Su mensaje es demasiado corto")

# Otra forma


MAX_CHARS = 100
MIN_CHARS = 50 


if len(mensaje) > MAX_CHARS:
    print(mensaje)
elif MIN_CHARS <= len(mensaje) < MAX_CHARS:
    print(mensaje[::-1])
else: 
    print("Su mensaje es demasiado corto")