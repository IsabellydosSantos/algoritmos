def verificar_matriz_direta():
    """
    Recebe a matriz diretamente do usuário e verifica se é quadrada.
    """
    print("Verificador de Matriz Quadrada")
    print("=" * 30)
    print("Digite a matriz no formato: [[a11, a12, ...], [a21, a22, ...], ...]")
    print("Exemplo: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
    print()
    
    try:
        # Recebe a matriz diretamente
        entrada = input("Digite a matriz: ")
        
        # Converte a string para lista usando eval (cuidado: usar com entrada confiável)
        # Em produção, considere usar ast.literal_eval para maior segurança
        matriz = eval(entrada)
        
        # Verifica se é uma lista de listas
        if not isinstance(matriz, list) or not all(isinstance(linha, list) for linha in matriz):
            raise ValueError("Formato inválido. Digite uma matriz no formato de lista de listas.")
        
        # Exibe a matriz
        print("\nMatriz informada:")
        for linha in matriz:
            print(linha)
        
        # Verifica se é quadrada
        resultado_numpy = eh_matriz_quadrada_numpy(matriz)
        resultado_simples = eh_matriz_quadrada_simples(matriz)
        
        print(f"\nDimensões: {len(matriz)}x{len(matriz[0])}")
        
        if resultado_simples:
            print("✓ A matriz é QUADRADA")
        else:
            print("✗ A matriz NÃO é quadrada")
            
        print(f"Verificação com NumPy: {resultado_numpy}")
        print(f"Verificação sem NumPy: {resultado_simples}")
        
        return matriz, resultado_simples
        
    except Exception as e:
        print(f"Erro: {e}")
        return None, False

# Versão alternativa mais segura (recomendada)
def verificar_matriz_direta_segura():
    """
    Versão mais segura usando ast.literal_eval
    """
    import ast
    
    print("Verificador de Matriz Quadrada (Versão Segura)")
    print("=" * 40)
    print("Digite a matriz no formato: [[1, 2], [3, 4]]")
    print()
    
    try:
        entrada = input("Digite a matriz: ")
        
        # Usa literal_eval que é mais seguro que eval
        matriz = ast.literal_eval(entrada)
        
        # Verifica se é uma lista de listas
        if not isinstance(matriz, list) or not all(isinstance(linha, list) for linha in matriz):
            raise ValueError("Formato inválido. Digite uma matriz no formato de lista de listas.")
        
        # Resto do código igual...
        print("\nMatriz informada:")
        for linha in matriz:
            print(linha)
        
        resultado_numpy = eh_matriz_quadrada_numpy(matriz)
        resultado_simples = eh_matriz_quadrada_simples(matriz)
        
        print(f"\nDimensões: {len(matriz)}x{len(matriz[0])}")
        
        if resultado_simples:
            print("✓ A matriz é QUADRADA")
        else:
            print("✗ A matriz NÃO é quadrada")
            
        return matriz, resultado_simples
        
    except (ValueError, SyntaxError) as e:
        print(f"Erro na formatação: {e}")
        print("Exemplo correto: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    
    return None, False
