import random

def menu():
    print("\n=== SIMULADOR DE DADO ===")
    print("1. Lançar dado uma vez")
    print("2. Simular múltiplos lançamentos")
    print("3. Sair")
    return input("Escolha uma opção: ")

while True:
    opcao = menu()
    
    if opcao == "1":
        resultado = random.randint(1, 6)
        print(f"🎲 Resultado: {resultado}")
        
    elif opcao == "2":
        n = int(input("Quantos lançamentos? "))
        resultados = [random.randint(1, 6) for _ in range(n)]
        
        print(f"\nResultados: {resultados}")
        
        # Estatísticas
        from collections import Counter
        contagem = Counter(resultados)
        
        print("\n📊 Estatísticas:")
        for face in range(1, 7):
            vezes = contagem.get(face, 0)
            percentual = (vezes / n) * 100
            print(f"Face {face}: {vezes} vezes ({percentual:.1f}%)")
            
    elif opcao == "3":
        break
    else:
        print("Opção inválida!")
