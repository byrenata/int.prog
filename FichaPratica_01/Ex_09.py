num1 = (input("Digite um número: "))
num2 = (input("Digite um número: "))
num3 = (input("Digite um número: "))

if num1 < num2 and num1 < num3:
    menor = num1
elif num1 > num2 and num2 <num3:
    menor = num2
else:
    menor = num3

print(f"Menor número: {menor}")
