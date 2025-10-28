texto = input("Digite um texto: ").lower()

vogais = ['a', 'e', 'i', 'o', 'u']

espacos = texto.count(' ')
a = texto.count('a')
e = texto.count('e')
i = texto.count('i')
o = texto.count('o')
u = texto.count('u')

print(f"espacos: {espacos} a: {a} e: {e} i: {i} o: {o} u: {u}")
