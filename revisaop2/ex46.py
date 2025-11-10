def conversao(valor_seg):
    horas = valor_seg // 3600
    minutos = (valor_seg % 3600) // 60
    segundos = valor_seg % 60
    return horas, minutos, segundos


def main():
    try:
        valor_seg = int(input("Insira um valor em segundos: "))

        horas, minutos, segundos = conversao(valor_seg)

        print(f"Esse valor é igual a {horas:02d} horas {minutos} minutos e {segundos} segundos")

    except ValueError:
        print("Insira apenas valores inteiros")


main()
