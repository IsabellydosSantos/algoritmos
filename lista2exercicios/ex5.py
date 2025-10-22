primeira = str(input("\nDigite a primeira string (caracteres a eliminar): "))
segunda = str(input("Digite a segunda string (texto original): "))
    
resultado = segunda
for char in primeira: 
  resultado = resultado.replace(char, '')
    
print(f"String resultante: '{resultado}'")
