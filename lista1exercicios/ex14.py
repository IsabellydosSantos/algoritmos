# Lendo uma sequência de números e determina o maior e menor número 

# input(): Função que captura entrada do usuário como string
# "Digite números separados por espaço: ": Mensagem exibida ao usuário
# .split(): Método que divide a string em uma lista de substrings usando espaço como separador
# map(): Função que aplica a função float() a cada elemento da lista
# float(): Função que converte string para número decimal
# list(): Converte o objeto map resultante em uma lista
numeros = list(map(float, input("Digite números separados por espaço: ").split()))

# Inicializando com o primeiro número
# numeros[0]: Acessa o primeiro elemento da lista (índice 0)
# Atribuímos o primeiro número como maior e menor inicialmente
maior = numeros[0]
menor = numeros[0]

# Percorrendo a lista a partir do segundo elemento
# numeros[1:]: Slice que pega todos os elementos a partir do índice 1 (segundo elemento)
# for numero in: Loop que itera sobre cada elemento da lista
for numero in numeros[1:]:
    # if numero > maior:: Verifica se o número atual é maior que o maior registrado
    if numero > maior:
        # Se verdadeiro, atualiza a variável maior com o número atual
        maior = numero
    
    # if numero < menor:: Verifica se o número atual é menor que o menor registrado  
    if numero < menor:
        # Se verdadeiro, atualiza a variável menor com o número atual
        menor = numero

# print(): Função que exibe output no console
# f-string: Formatação de string que permite incluir variáveis dentro de {}
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
