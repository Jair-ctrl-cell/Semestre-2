class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial   # atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def obtener_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria(100)
cuenta.depositar(50)
print("Saldo actual:", cuenta.obtener_saldo())
