#recebe um número e o converte em sua base binária com uma função simples

numero = int(input("Digite um número decimal: "))
#em python o resultado é mostrado com um "0b" antes para indicar que está em base binária 
#a função "[2: ]" indica que é para excluir esses dois primeiros dígitos
print(f"O número {numero} em binário é: {bin(numero)[2:]}")
