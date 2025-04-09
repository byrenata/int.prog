num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resp = input("Qual a operação a ser realizada? ")

if resp == '+':
    print (f"Resultado = {num1 + num2}")
elif resp == '-':
    print(f"Resultado = {num1 - num2}")
elif resp == '*':
    print (f"Resultado = {num1 * num2}")
elif resp == '/':
    print (f"Resultado = {num1/num2}")
else:
    print ("** ERRO **")