perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = []

print("Responda as perguntas com 'sim' ou 'não':\n")

for pergunta in perguntas:
    resposta = input(f"{pergunta} ").lower().strip()
    while resposta not in ['sim', 'não', 'nao']:
        print("Responda apenas com sim ou não")
        resposta = input(f"{pergunta} ").lower().strip()
    respostas.append(resposta)

positivas = respostas.count('sim')

if positivas == 5:
    classificacao = "Assassino"
elif positivas >= 3:
    classificacao = "Cúmplice"
elif positivas == 2:
    classificacao = "Suspeita"
else:
    classificacao = "Inocente"


print(f"\nNúmero de respostas positivas: {positivas}")
print(f"Classificação: {classificacao}")

print("\n--- Resumo das respostas ---")
for i, pergunta in enumerate(perguntas):
    print(f"{pergunta} → {respostas[i]}")


