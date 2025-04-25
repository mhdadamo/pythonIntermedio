# CLASE 3 - EJERCICIO 4

'''
Calcular el promedio de una lista usando *args y un operador ternario
'''

def calcular_promedio(*args):
    # Ternario para manejar el caso de lista vacía
    promedio = sum(args) / len(args) if len(args) > 0 else "No se ingresaron números"
    return promedio

# Pedimos números separados por coma
entrada = input("Ingresa los números separados por coma: ")
numeros = [float(n.strip()) for n in entrada.split(",")]

# Llamamos a la función con *args
resultado = calcular_promedio(*numeros)

print("El promedio es:", resultado)
