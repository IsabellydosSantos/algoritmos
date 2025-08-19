hora_atual = int(input("Informe o horário atual (0-23): "))
alarme = int(input("Daqui a quantas horas o alarme deve tocar? "))

hora_alarme = (hora_atual + alarme) % 24

print(f"\nO alarme irá tocar às {hora_alarme}:00 horas")
