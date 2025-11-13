def calcular_frequencia(lista):
    frequencias = {}
    
    for numero in lista:
        if numero in frequencias:
            frequencias[numero] += 1
        else:
            frequencias[numero] = 1
    
    # key=frequencias.get significa: ordenar pelas frequências (valores do dicionário)
    elemento_maior_freq = max(frequencias, key=frequencias.get)
    
    elemento_menor_freq = min(frequencias, key=frequencias.get)
    
    return (elemento_menor_freq, elemento_maior_freq)

def le_lista():
    print("Digite os números inteiros separados por espaço:")
    
    try:
        entrada = input("Lista: ").strip()
        lista = [int(x) for x in entrada.split()]
        return lista
    except ValueError:
        prit("Digite apenas números inteiros!")
        return []

def mostrar_analise_final(lista, resultado):
    if not lista:
        return
    
    # Calcula frequências para mostrar detalhes
    frequencias = {}
    for numero in lista:
        frequencias[numero] = frequencias.get(numero, 0) + 1
    
    print(f"Lista original: {lista}")
    print(f"Total de elementos: {len(lista)}")
    print(f"Elementos únicos: {len(frequencias)}")
    print(f"\nFrequências:")
    
    for numero, freq in sorted(frequencias.items()):
        print(f"  {numero}: aparece {freq} vez(es)")
    
    menor_freq, maior_freq = resultado
    print(f"\nResultado")
    print(f"• Elemento com menor frequência: {menor_freq} (aparece {frequencias[menor_freq]} vez(es))")
    print(f"• Elemento com maior frequência: {maior_freq} (aparece {frequencias[maior_freq]} vez(es))")

# Programa principal
def main():
    lista = le_lista()
    
    # Verifica se a lista não está vazia
    if not lista:
        print("Lista vazia. Nada para analisar.")
        return
    
        resultado = calcular_frequencia(lista)
        menor_freq, maior_freq = resultado
        
        print(f"\n=== Resultado ===")
        print(f"Elemento com menor frequência: {menor_freq}")
        print(f"Elemento com maior frequência: {maior_freq}")
        print(f"Tupla retornada: {resultado}")
        
        # Mostra análise detalhada
        mostrar_analise_final(lista, resultado)
        

    main()
