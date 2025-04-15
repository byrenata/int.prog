

print("1- Criar")
print("2- Atualizar")
print("3- Eliminar")
print("4- Sair")
print("============")
op = int(input("Escolha uma operação:"))

if op >= 5:
    print("Opção inválida!")

if op == 1:
    print("Criando...")
elif op == 2:
        print("Atualizando...")
elif op == 3:
        print("Eliminando...")
else:
        print("Saindo...")