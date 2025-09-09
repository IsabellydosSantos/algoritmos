#recebe um número e o converte em sua base binária com uma função simples

numero = int(input("Digite um número decimal: "))
print(f"O número {numero} em binário é: {bin(numero)[2:]}")
