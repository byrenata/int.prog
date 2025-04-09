#Pedir ao user dois números int
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int

valor3 = valor1
valor1 = valor2
valor2 = valor3
print("Primeiro valor: ",valor1,"Segundo valor: ",valor2)

#troca sem a variável extra
valor1, valor2 = valor2, valor1
print("Valor 1= ",valor1)
print("Valor 2= ",valor2)