sexo = str(input("Insira seu sexo (F ou M): ")).upper
idade = int(input("Insira sua idade: "))
tempo_contrib = int(input("Insira seus anos de contribuição: ")) 

if sexo == "M":
  if idade >= 65 and tempo_contrib >= 10:
    print("Aposentável")
  elif idade >= 63 and tempo_contrib >= 15:
    print("Aposentável")
elif sexo == "F":
  if idade >= 63 and tempo_contrib >= 10:
    print("Aposentável")
  elif idade >= 61 and tempo_contrib >= 15:
    print("Aposentável")
else:
  print("Não Aposentável")
