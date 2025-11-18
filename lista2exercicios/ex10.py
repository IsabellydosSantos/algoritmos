def calcular_soma(matriz):
    # zip(*matriz) transpoe a matriz, agrupando elementos por coluna
    return [sum(coluna) for coluna in zip(*matriz)]

def main():
    m = int(input("Digite o número de linhas (m): "))
    n = int(input("Digite o número de colunas (n): "))
    
    matriz = []
    print(f"\nDigite a matriz {m}x{n}:")
    for i in range(m):
        linha = [int(x) for x in input(f"Linha {i+1}: ").split()]
        matriz.append(linha)
    
    vetor_soma = calcular_soma(matriz)
    
    print("\nMatriz:")
    for linha in matriz:
        print(linha)
    
    print(f"\nSoma das colunas: {vetor_soma}")

main()
