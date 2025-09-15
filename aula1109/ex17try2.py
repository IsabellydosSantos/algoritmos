alunos = int(input("Insira a quantidade de alunos na sala: "))

print("Digite as notas da P1 separadas por espaço:")
p1 = list(map(float, input().split()))

print("Digite as notas da P2 separadas por espaço:")
p2 = list(map(float, input().split()))

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
