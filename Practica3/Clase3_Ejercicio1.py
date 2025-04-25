# CLASE 3 - EJERCICIO 1

'''
Calcular el mayor de dos números ingresados por teclado usando un operador ternario
'''

# Pedimos los números al usuario
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Usamos el operador ternario
mayor = num1 if num1 > num2 else num2

# Mostramos el resultado
print("El número mayor es:", mayor)
