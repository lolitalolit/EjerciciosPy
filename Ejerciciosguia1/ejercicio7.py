#Ejercicio 7: Crear un programa que calcule el sueldo bruto de una persona que trabaja de lunes a viernes 8 hs 
# y su pago por hora es de 400 pesos. Devolver el sueldo por pantalla.

hora = 400
hs_semanales = 40
hs_mensuales = hs_semanales * 4
sueldo = hora * hs_mensuales

print("$" + str(sueldo))