#Pedir ao user três valores
preco1 = float(input("Digite o primeiro valor: "))
preco2 = float(input("Digite o segundo valor: "))
preco3 = float(input("Digite o terceiro valor: "))


Desc = (preco1 + preco2 + preco3) *0.10 
Tot = (preco1 + preco2 + preco3) - Desc
print("Total: ",Tot)