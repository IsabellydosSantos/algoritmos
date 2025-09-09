#classifica o número inserido como par ou ímpar e se é menor, maior ou igual a 100

a = int(input("Insira um número: "))
#"a % 2 == 0" verifica se o número é par
#para um número ser par é necessário que a divisão do número por 2 tenha resto igual a 0
if a % 2 == 0 and a < 100: #se o numero é par e  menor que 100
    print("O número é par e menor que 100")
elif a % 2 == 0 and a >= 100:  #se o numero é par e menor ou igual a 100
    print("O número é par e maior ou igual a 100")

if a % 2 != 0 and a < 100: #se o número é ímpar e menor que 100
    print("O número é ímpar e menor que 100")
elif a % 2 != 0 and a > 100: #se o número é ímpar e maior que 100
    print("O número é ímpar e maior que 100")
