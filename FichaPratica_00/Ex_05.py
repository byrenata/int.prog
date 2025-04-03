#Pedir ao user três números int
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

medArit = (num1+num2+num3)/3
print("Média aritmética: ",medArit)

medPond = (num1*0.2) + (num2*0.3) + (num3*0.5)/(0.2 + 0.3 + 0.5)
print("Média ponderada: ",medPond)