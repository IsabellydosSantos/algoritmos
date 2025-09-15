alunos = int(input("Insira a quantidade de alunos na sala: "))

p1 = []
p2 = []

print("Insira as notas da P1: ")
for i in range(alunos):
  p1.append(float(input()))

print("Insira as notas da P2: ")
for i in range(alunos):
  p2.append(float(input()))

media_p1 = sum(p1) / alunos
media_p2 = sum(p2) / alunos

print(f"Média da turma na Prova 1: {media_p1:.2f}")
print(f"Média da turma na Prova 2: {media_p2:.2f}")

if media_p1 > media_p2:
    print("A turma obteve a melhor média na Prova 1")
elif media_p2 > media_p1:
    print("A turma obteve a melhor média na Prova 2")
else:
    print("As duas provas tiveram a mesma média")
