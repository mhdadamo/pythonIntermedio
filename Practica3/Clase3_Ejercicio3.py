# CLASE 3 - EJERCICIO 3

'''
Determinar si un número es par o impar.
'''

def es_par_o_impar(*args):
    numero = args[0]  # Tomamos el primer número de los argumentos
    resultado = "Es par" if numero % 2 == 0 else "Es impar"
    return resultado

# Pedimos el número
n = int(input("Ingresa un número: "))

# Llamamos a la función pasando el número como *args
print(es_par_o_impar(n))
