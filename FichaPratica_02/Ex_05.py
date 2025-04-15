ini = int(input("Digite o 1º número : "))
fim = int(input("Digite o 2º número : "))

# não é boa prática usar o contador com variável que não sejaapenas dele,
# aaqui a variável que o utilizador imprime um valor coé usada como contador 

cont=1
while ini <= fim:
    print(ini)
    ini += cont

   