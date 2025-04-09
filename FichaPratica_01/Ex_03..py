sal = float(input("Insira o salário: "))


if sal <= 15000:
    imp = sal*0.2
    imp = 20
elif sal > 15000 and sal < 20000:
    imp = sal*0.3
    imp = 30
elif sal > 20000 and sal < 25000:
    imp = sal * 0.35
else: sal > 25000
imp = sal *0.4

print(f"Salário = {sal} e imposto anual = {imp} €.")