

print("============")
print("Escolha uma operação:")
print("[+] Adição")
print("[-] Subtração")
print("[*] Multiplicação")
print("[/] Divisão")
print("============")
resp = "S"
while resp == "S":
    num1 = int(input("Digite um número inteiro: "))
    num2 = int(input("Digite outro número inteiro: "))
    char = input("Defina a operação: [+ - * /]: ")
    match(char):
        case '+':
            res = num1 + num2
        case '-':
            res = num1 - num2
        case '*':
            res = num1 * num2
        case '/':
            res = num1 / num2
        case _:
            print("Operação inválida!")
            exit()  
    print(f"Resultado: {res}")
    resp = input("Deseja continuar? [S/N]: ").upper()





