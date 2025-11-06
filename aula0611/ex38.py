def analisar_zeros_matriz():
    """
    Função completa para receber matriz e contar zeros.
    """
    import ast
    
    print("Contador de Zeros em Matriz Quadrada")
    print("=" * 40)
    print("Digite a matriz quadrada no formato: [[a11, a12], [a21, a22]]")
    print("Exemplos:")
    print("  [[1, 0, 3], [0, 5, 0], [7, 0, 9]]")
    print("  [[0, 2], [3, 0]]")
    print()
    
    try:
        entrada = input("Digite a matriz: ")
        matriz = ast.literal_eval(entrada)
        
        # Tenta contar com ambas as funções
        zeros_numpy, porcentagem_numpy = contar_zeros_numpy(matriz)
        zeros_simples, porcentagem_simples = contar_zeros_simples(matriz)
        
        # Exibe resultados
        print(f"\nMatriz {len(matriz)}x{len(matriz)}:")
        for linha in matriz:
            print(f"  {linha}")
        
        print(f"\nResultados:")
        print(f"Com NumPy: {zeros_numpy} zeros ({porcentagem_numpy:.2f}%)")
        print(f"Sem NumPy: {zeros_simples} zeros ({porcentagem_simples:.2f}%)")
        
        return matriz, zeros_simples, porcentagem_simples
        
    except ValueError as e:
        print(f"Erro: {e}")
    except SyntaxError:
        print("Erro: Formato inválido. Use o formato: [[1, 0], [0, 2]]")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    
    return None, 0, 0


def contar_zeros_simples(matriz):
    """
    Conta o número de zeros em uma matriz quadrada sem usar NumPy.
    
    Args:
        matriz: Lista de listas representando a matriz quadrada
    
    Returns:
        tuple: (quantidade_zeros, porcentagem_zeros)
    
    Raises:
        ValueError: Se a matriz não for quadrada
    """
    # Verifica se é uma matriz quadrada
    if not isinstance(matriz, list) or len(matriz) == 0:
        raise ValueError("Matriz inválida")
    
    if not all(isinstance(linha, list) for linha in matriz):
        raise ValueError("Matriz inválida")
    
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    
    if num_linhas != num_colunas:
        raise ValueError("A matriz fornecida não é quadrada")
    
    if not all(len(linha) == num_colunas for linha in matriz):
        raise ValueError("Matriz com linhas de tamanhos diferentes")
    
    # Conta os zeros
    zeros = 0
    total_elementos = num_linhas * num_colunas
    
    for linha in matriz:
        for elemento in linha:
            if elemento == 0:
                zeros += 1
    
    porcentagem = (zeros / total_elementos) * 100
    
    return zeros, porcentagem
