def substituir_valores(vetor):
    return [1 if valor > 0 else 0 for valor in vetor]

def main():
    vetor = []
    
    print("Digite 30 números:")
    
    for i in range(30):
        while True:
            try:
                numero = float(input(f"Número {i+1}/30: "))
                vetor.append(numero)
                break
            except ValueError:
                print("Digite um número válido!")
    
    print(f"\nVetor original: {vetor}")
    
    vetor_modificado = substituir_valores(vetor)
    
    print(f"Vetor modificado: {vetor_modificado}")

main()
