def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def primos_contiguos(n):
    if n < 2:
        raise ValueError("O número deve ser ≥ 2")
    
    primo_anterior = n - 1
    while primo_anterior >= 2:
        if eh_primo(primo_anterior):
            break
        primo_anterior -= 1
    
    primo_posterior = n + 1
    while True:
        if eh_primo(primo_posterior):
            break
        primo_posterior += 1
    
    return primo_anterior, primo_posterior

def main():
    try:
        n = int(input("Digite um número inteiro ≥ 2: "))
        
        anterior, posterior = primos_contiguos(n)
        
        print(f"Para o número {n}:")
        print(f"Primo anterior: {anterior}")
        print(f"Primo posterior: {posterior}")
        
    except ValueError as e:
        print(f"Erro: {e}")


    main()
    
