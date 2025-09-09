#lê um ano e informa se é bissexto ou não 
ano = int(input("Insira um ano para saber se ele é bissexto: "))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0): 
#um ano é bissexto se for divisível por 400 ou se for divisível por 4 mas não por 100
#para um número ser divisível por outro, o resto da divisão deve ser 0
  print("Esse ano é bissexto")
else:
  print("Esse ano não é bissexto")


