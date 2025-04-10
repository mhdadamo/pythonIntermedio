#EJERCICIOS PRÁCTICA 2 - EJERCICIO 1
'''
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
'''

numeroUno = 20
numeroDos = 0
numeroTres = 55
numeroCuatro = 5


try:
    resultado1 = (numeroUno/numeroDos)

except ZeroDivisionError:
    print(f"Ha ocurrido un error No se puede dividir por 0")


else:

    print(f"El resultado de {numeroUno} dividido {numeroDos} es: {resultado1}")



try:
    resultado2 = (numeroTres/numeroCuatro)

except ZeroDivisionError:
    print(f"Ha ocurrido un error No se puede dividir por 0")

else:

    print(f"El resultado de {numeroTres} dividido {numeroCuatro} es: {resultado2}")