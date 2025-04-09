nota1 = float(input("Digite a primeira nota[0 a 20]:"))
nota2 = float(input("Digite a segunda nota [0 a 20]: "))
nota3 = float(input("Digite a segunda nota[0 a 20]: "))

nf1 = nota1 * 0.25
nf2 = nota2 * 0.35
nf3 = nota3 * 0.40

mf = (nf1 + nf2 + nf3)/(0.25+0.35+0.40)
print(f"Média final: {mf}")