#lê um numero n e imprime os primeiros n números ímpares 

n = int(input("Digite um número inteiro positivo: "))

print(f"Os {n} primeiros números ímpares são: ")

#loop que repete 'n' vezes (de 0 até n-1)
for i in range(n):
    #fórmula matemática para gerar números ímpares:
    numero_impar = 2 * i + 1
    
    #end=" " → substitui a quebra de linha padrão por espaço
    print(numero_impar, end=" ")


