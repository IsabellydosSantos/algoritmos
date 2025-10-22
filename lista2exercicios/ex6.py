palavra1 = input("\nDigite a primeira palavra: ").lower().replace(" ", "")
palavra2 = input("Digite a segunda palavra: ").lower().replace(" ", "")
    
if sorted(palavra1) == sorted(palavra2):
  print(f" {palavra1.upper()}' e '{palavra2.upper()}' são anagramas!")
else:
  print(f"'{palavra1.upper()}' e '{palavra2.upper()}' não são anagramas!")
