def maior_palavra(texto):
  for palavra in  ".,!?:;":
    texto = texto.replace(palavra,"")
  p = texto.split()
  if not p:
    return ""
  maior = ""
  for contador in p:
    if len(contador) >= len(maior)
     maior = contador
   return maior
print(maior_palavra("digite uma frase aleatoria: "))
