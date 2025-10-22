n = input("\nDigite 10 números inteiros separados por espaço:")
vetor = [int(x) for x in n.split()]
    
if len(vetor) != 10:
    
    # Calcula a maior diferença
    maior_diferenca = 0
    posicao_maior = 0
    
    for i in range(9):  # 9 comparações para 10 elementos
        diferenca = abs(vetor[i] - vetor[i + 1])
        if diferenca > maior_diferenca:
            maior_diferenca = diferenca
            posicao_maior = i
    
    # Exibe o resultado
    print(f"\nVetor: {vetor}")
    print(f"Maior diferença: {maior_diferenca}")
    print(f"Entre vetor[{posicao_maior}] = {vetor[posicao_maior]} e vetor[{posicao_maior + 1}] = {vetor[posicao_maior + 1]}")
