#Pedir ao user dois números int
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    maior = num1
else:
    maior = num2
    print(f"Maior número = {maior}")