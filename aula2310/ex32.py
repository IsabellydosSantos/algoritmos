n = int(input("Informe o número de pessoas a serem adicionadas: "))

# Dicionário para armazenar as pessoas (CPF como chave)
pessoas = {}

# Recebe as informações de cada pessoa
for i in range(n):
    print(f"{i+1}° pessoa:")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    idade = int(input("Idade: "))
    
    # Usa CPF como chave - se já existir, mantém o primeiro registro
    if cpf not in pessoas:
        pessoas[cpf] = {"nome": nome, "idade": idade, "cpf": cpf}

# Imprime a lista de pessoas sem repetições
print("\nLista de pessoas sem repetições:")
for pessoa in pessoas.values():
    print(f"{pessoa['nome']} {pessoa['cpf']} {pessoa['idade']}")
