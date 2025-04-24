#EJERCICIOS PRÁCTICA 2 - EJERCICIO 4
'''
Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
embargo, también intenta crear el archivo si no existe.
'''

try:
    # Intentamos abrir un archivo que no existe
    with open("archivo_que_no_existe.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    # Si ocurre un error porque no existe, mostramos un mensaje
    print("Error: El archivo no existe.")
    
    # Intentamos crear el archivo
    try:
        with open("archivo_que_no_existe.txt", "w") as nuevo_archivo:
            nuevo_archivo.write("Este es un archivo recién creado.\n")
        print("Se ha creado el archivo correctamente.")
    except Exception as e:
        print("Ocurrió un error al crear el archivo:", e)
