n = input("\nDigite 10 números inteiros separados por espaço:")
vetor = [int(x) for x in n.split()]
    
if len(vetor) != 10:
    print("Digite apenas 10 números")
else:
    maior_diferenca = 0
    posicao_maior = 0
    
    for i in range(len(vetor) - 1):  
        # abs(valor absoluto) garante que a diferença seja sempre positiva
        # vetor[i] e vetor[i+1] garante que sejam consecutivos
        diferenca = abs(vetor[i] - vetor[i + 1])
        if diferenca > maior_diferenca:
            maior_diferenca = diferenca
            posicao_maior = i
    
    print(f"Maior diferença: {maior_diferenca}")
    print(f"Entre vetor[{posicao_maior}] = {vetor[posicao_maior]} e vetor[{posicao_maior + 1}] = {vetor[posicao_maior + 1]}")
