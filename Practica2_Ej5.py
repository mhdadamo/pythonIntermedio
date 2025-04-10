#EJERCICIOS PRÁCTICA 2 - EJERCICIO 5

'''
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario
'''

try:
    # Pedimos al usuario que ingrese dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Intentamos hacer la división
    resultado = num1 / num2
    print("El resultado de la división es:", resultado)

except ValueError:
    # Si el usuario no ingresa un número válido
    print("Error: Debe ingresar un número válido.")

except ZeroDivisionError:
    # Si el segundo número es cero
    print("Error: No se puede dividir por cero.")
