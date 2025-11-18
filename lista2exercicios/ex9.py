def contar_ocorrencias(numero, matriz):
    contador = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == numero:
                contador += 1
    return contador

def criar_matriz():
    linhas = int(input("Digite o número de linhas da matriz: "))
    matriz = []
    
    print("Digite os elementos de cada linha (separados por espaço):")
    for i in range(linhas):
        while True:
            try:
                entrada = input(f"Linha {i+1}: ").strip()
                linha = [int(x) for x in entrada.split()]
                matriz.append(linha)
                break
            except ValueError:
                print("Erro: Digite apenas números inteiros separados por espaço!")
    
    return matriz

def main():
    matriz = criar_matriz()
    
    numero = int(input("\nDigite o número inteiro a ser contado: "))
    
    quantidade = contar_ocorrencias(numero, matriz)
    
    print(f"\nMatriz informada:")
    for linha in matriz:
        print(linha)
    
    print(f"\nO número {numero} aparece {quantidade} vezes na matriz")


main()
