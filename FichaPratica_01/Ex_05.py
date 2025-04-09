num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

if num1 < num2: 
    menor = num1
    maior = num2
else:
    menor = num2
    maior = num1

    print (f"Menor número: {menor} e maior número: {maior}")