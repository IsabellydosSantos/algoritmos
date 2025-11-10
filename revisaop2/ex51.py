frase = input("Digite uma frase: ").lower().strip()
caract = input("Digite um caractere: ").lower()

quant = frase.count(caract)
posicao = []

for i in range(len(frase)):
    if frase[i] == caract:
        posicao.append(i + 1)

print(f"O caractere {caract} aparece {quant} vezes na frase nas posições {posicao}")