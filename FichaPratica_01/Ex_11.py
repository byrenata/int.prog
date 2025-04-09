saldo = float(input("Introduza um saldo médio: "))
valor = float (input("Introduza o valor a movimentar: "))

tot = saldo + valor

if tot > 0:
    print (f"Saldo atual: {tot}")
else:
    print (f"Operação inválida. Saldo insuficiente: {saldo} ")