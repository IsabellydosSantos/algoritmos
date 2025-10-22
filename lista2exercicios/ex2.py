c1 = input("\nDigite os números do primeiro conjunto (separados por espaço):")
conjunto1 = [for x in c1.split()]

c2 = input("Digite os números do segundo conjunto (separados por espaço):")
conjunto2 = [for x in c2.split()]
    
conjunto3 = conjunto1 + conjunto2
    
#remove as duplicatas convertendo
uniao = set(conjunto3))
    
# Ordena o resultado para ficar mais organizado
uniao.sort()
    
# Exibe os resultados
print(f"União dos conjuntos: {uniao}")
      
