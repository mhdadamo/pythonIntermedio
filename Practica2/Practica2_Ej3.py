#EJERCICIOS PRÁCTICA 2 - EJERCICIO 3
'''
Escribe un programa que intente acceder a una clave que no existe en un
diccionario. Si se produce una excepción KeyError, captura la excepción y muestra
'''

diccionarioEdades = {"nombre": "Maximiliano", "Edad": 52}

try:
    print(diccionarioEdades["Apellido"])

except KeyError:
    print("El índice no se encuentra")


else:

    print(diccionarioEdades["Apellido"])

