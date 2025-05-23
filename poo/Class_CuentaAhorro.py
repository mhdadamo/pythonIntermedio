from Class_CuentaBancaria import CuentaBancaria

class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self.__tasa_interes = 0.001

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Se ha depositado {monto} a la cuenta de {self._nombre_titular}, saldo actual: {self.obtener_saldo()}")
        else:
            print("El monto a depositar debe ser mayor a 0")

    def extraer(self, monto):
        if monto <= self.obtener_saldo():
            self._saldo -= monto
            print(f"Se ha extraído {monto} de la cuenta de {self._nombre_titular}, saldo actual: {self.obtener_saldo()}")
        else:
            print("No posee saldo suficiente para esta operación")

    def calcular_interes(self):
        interes = self._saldo * self.__tasa_interes
        print(f"El interés generado para {self._nombre_titular} es: {interes}")
        return interes
    
    # Ejemplo de uso
if __name__ == "__main__":
    cuenta = CuentaAhorro("Juan Pérez", "12345678", "1990/05/10", 10000)
    cuenta.depositar(500)
    cuenta.extraer(300)
    cuenta.calcular_interes()
