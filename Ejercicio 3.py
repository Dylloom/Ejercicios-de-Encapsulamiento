class CuentaBancaria:
    def __init__(self, titular, saldo, numero_cuenta):
        self._titular = titular
        self._saldo = saldo
        self._numero_cuenta = numero_cuenta

    def mostrar_informacion(self):
        return f"Titular: {self._titular}, Saldo: {self._saldo}, Numero de cuenta: {self._numero_cuenta}"

    def depositar(self):
        deposito = int(input("Cantidad de dinero a ingresar: "))
        self._saldo += deposito

    def retirar(self):
        retiro = int(input("Cantidad de dinero a retirar: "))
        if retiro <= self._saldo:
            self._saldo -= retiro
        else:
            print("Cantidad que quiere retirar es mayor al saldo de la cuenta")


if __name__ == "__main__":
    prueba1 = CuentaBancaria("Jorge", 100, 123456789)
    print(prueba1.mostrar_informacion())
    prueba1.depositar()
    print(prueba1.mostrar_informacion())
    prueba1.retirar()
    print(prueba1.mostrar_informacion())
    prueba1.retirar()
