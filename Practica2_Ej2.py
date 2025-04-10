#EJERCICIOS PRÁCTICA 2 - EJERCICIO 2
'''
Escribe un programa que intente sumar un número y una cadena. Si se produce un error
de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
'''

variable1 = "hola"
variable2 = 5

try:
    resultado1 = (variable1 + variable2)

except TypeError:
    print(f"Ha ocurrido un error en uno de los datos")


else:

    print(f"El resultado de {variable1} + {variable2} es: {resultado1}")
