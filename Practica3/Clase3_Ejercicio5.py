# CLASE 3 - EJERCICIO 5

'''
Imprimir un mensaje de error si no se pasan suficientes argumentos
'''


def verificar_argumentos(*args):
    mensaje = "La cantidad de argumentos esta OK" if len(args) >= 2 else "Error: no se pasaron suficientes argumentos"
    print(mensaje)

# Ejemplos de prueba:
verificar_argumentos(10, 20)     # Debería imprimir: Suficientes argumentos
verificar_argumentos(5)          # Debería imprimir: Error: no se pasaron suficientes argumentos
verificar_argumentos()           # También error
