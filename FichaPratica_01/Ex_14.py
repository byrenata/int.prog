num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

if num1 < num2 and num1 <num3:
    menor = num1
    if num2 < num3:
        maior = num3
    else:
        maior = num2
        print(f"A ordem crescente dos números: {menor}, {num2} e {maior}. ")    
elif num2 < num1 and num2 < num3:
    menor = num2 
    if num1 < num3:
        maior = num3
    else:
        maior = num1
        print(f"A ordem crescente dos números: {menor}, {num1} e {maior}. ")
else:
    menor = num3
    if num1 < num2:
        maior = num2
    else:
        maior = num1
        print(f"A ordem crescente dos números: {menor}, {num1} e {maior}. ")   