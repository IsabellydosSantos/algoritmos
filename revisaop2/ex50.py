def num_tri(n):

    if n < 0:
        return False
    elif n == 0:
        return True

    i = 0
    while i * (i+1) * (i+2) <= n:
        if i * (i+1) * (i+2) == n:
            return True
        i += 1
    return False


def main():
    try:
        n = int(input("Insira um número inteiro positivo: "))

        if n < 0:
            print("Digite apenas números positivos")

        resultado = num_tri(n)

        if resultado:
            print(f"O número {n} é triangular e é formado por {i} * {i+1} * {i+2}")
        else:
            print(f"O número {n} não é triangular")

    except ValueError:
        print("Digite apenas números inteiros")



main()
