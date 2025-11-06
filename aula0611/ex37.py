def verificar_matriz_quadrada():
    """
    Função completa que recebe matriz do usuário e verifica se é quadrada.
    """
    print("Verificador de Matriz Quadrada")
    print("=" * 30)
    
    try:
        # Solicita as dimensões da matriz
        linhas = int(input("Digite o número de linhas da matriz: "))
        colunas = int(input("Digite o número de colunas da matriz: "))
        
        # Solicita os elementos da matriz
        print("\nDigite os elementos da matriz linha por linha:")
        matriz = []
        
        for i in range(linhas):
            linha = []
            print(f"Linha {i + 1}:")
            for j in range(colunas):
                elemento = float(input(f"  Elemento [{i+1},{j+1}]: "))
                linha.append(elemento)
            matriz.append(linha)
        
        # Exibe a matriz
        print("\nMatriz informada:")
        for linha in matriz:
            print(linha)
        
        # Verifica se é quadrada
        if linhas == colunas:
            print(f"\n✓ A matriz é QUADRADA ({linhas}x{colunas})")
        else:
            print(f"\n✗ A matriz NÃO é quadrada ({linhas}x{colunas})")
            
        # Verificação adicional com as funções
        print(f"\nVerificação com NumPy: {eh_matriz_quadrada_numpy(matriz)}")
        print(f"Verificação sem NumPy: {eh_matriz_quadrada_simples(matriz)}")
        
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")

# Para testar a função com entrada do usuário, descomente a linha abaixo:
# verificar_matriz_quadrada()
