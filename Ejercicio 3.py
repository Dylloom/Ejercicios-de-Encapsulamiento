class CuentaBancaria:
    def __init__(self, titular, saldo, numero_cuenta):
        self.titular = titular
        self.saldo = saldo
        self.numero_cuenta = numero_cuenta

    def mostrar_informacion(self):
        return f"Nombre: {self.titular}, Saldo: {self.saldo}, Numero de cuenta: {self.numero_cuenta}"

    def depositar(self):
        deposito = float(input("Cantidad que quiera depositar: "))
        self.saldo += deposito

    def retirar(self):  
        retiro = float(input("Cantidad que quiera retirar: "))
        if retiro <= self.saldo:
            self.saldo = self.saldo - retiro
        else:
            print("La cantidad a retirar es mayor que el saldo de la cuenta")
        

# Ejemplo de uso
if __name__ == "__main__":
    Objeto = CuentaBancaria("Carol", 100.0, 123456789)
    print(Objeto.mostrar_informacion())
    Objeto.depositar()
    Objeto.retirar()
    print(Objeto.mostrar_informacion())
