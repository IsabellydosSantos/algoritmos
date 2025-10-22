c1 = input("\nDigite os números do primeiro conjunto (separados por espaço):")
conjunto1 = [int(x) for x in c1.split()]

c2 = input("Digite os números do segundo conjunto (separados por espaço):")
conjunto2 = [int(x) for x in c2.split()]
    
conjunto3 = conjunto1 + conjunto2
    
#remove as duplicatas e converte de volta para lista 
uniao = list(set(conjunto3))
    
#ordena em ordem crescente
uniao.sort()
    
print(f"União dos conjuntos: {uniao}")
