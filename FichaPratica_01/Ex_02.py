#Pedir ao user 
sal = float(input("Insira o salário: "))
desc = 0

if sal < 15000:
    imp = (sal * 0.2)
    print(f"Taxa a pagar:{imp}")
else:
    imp = (sal * 0.3)
print(f"Taxa a pagar:{imp}")
