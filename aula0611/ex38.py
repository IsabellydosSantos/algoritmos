def contar_zeros_matriz():
    """
    Versão super simples com entrada do usuário.
    """
    print("Digite a matriz linha por linha.")
    print("Exemplo para 3x3:")
    print("1 0 3")
    print("0 5 0") 
    print("7 0 9")
    print()
    
    matriz = []
    print("Digite cada linha separada por espaços:")
    
    # Lê a primeira linha para saber o tamanho
    primeira_linha = input("Linha 1: ").split()
    n = len(primeira_linha)
    matriz.append([int(x) for x in primeira_linha])
    
    # Lê as demais linhas
    for i in range(1, n):
        linha = input(f"Linha {i+1}: ").split()
        if len(linha) != n:
            print("Erro: Todas as linhas devem ter o mesmo tamanho!")
            return
        matriz.append([int(x) for x in linha])
    
    # Conta os zeros
    zeros = 0
    for linha in matriz:
        for num in linha:
            if num == 0:
                zeros += 1
    
    # Mostra resultados
    print(f"\nMatriz {n}x{n}:")
    for linha in matriz:
        print(linha)
    
    print(f"\nZeros: {zeros} de {n*n} elementos ({(zeros/(n*n))*100:.1f}%)")


contar_zeros_matriz()
