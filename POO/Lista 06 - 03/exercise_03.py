from class_03 import ContaBancaria

conta_1= ContaBancaria('Juliana', 1000000)
print (f"Saldo atual: {conta_1.saldo} (antes do deposito)")

deposito = int(input("Deposito:"))
conta_1.depositar(deposito)
print (f"Saldo atual: {conta_1.saldo} (depois do deposito)")


saque = (int(input("Saque:")))
conta_1.sacar(saque)
print (f"Saldo atual: {conta_1.saldo} (depois do saque)")