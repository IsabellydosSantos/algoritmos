def conversao(valor_seg):
    horas = valor_seg // 3600
    minutos = (valor_seg % 3600) // 60
    segundos = valor_seg % 60
    return
def main():
    try:
        valor_seg = int(input("Insira um valor em segundos: "))
        
        conv = conversao(valor_seg)
        
        print(f"Esse valor é igual a {horas:2f} horas {} minutos e {} segundos")
