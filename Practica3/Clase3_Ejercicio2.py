# CLASE 3 - EJERCICIO 2

'''
Buscar una palabra en una lista ingresada por teclado usando *args y un operado ternario.
'''

def buscar_palabra(palabra_buscada, *args):
    # Operador ternario para ver si la palabra está en la lista
    resultado = "Palabra encontrada" if palabra_buscada in args else "Palabra no encontrada"
    return resultado

# Pedimos al usuario que ingrese palabras separadas por coma
entrada = input("Ingresa una lista de palabras separadas por comas: ")
palabras = [palabra.strip() for palabra in entrada.split(",")]  # quitamos espacios

# Pedimos la palabra a buscar
palabra = input("¿Qué palabra querés buscar? ").strip()  # quitamos espacios también

# Llamamos a la función pasando la lista como *args
print(buscar_palabra(palabra, *palabras))
