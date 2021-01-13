import pyperclip

palavra = input("palavra:")
palavra = palavra.upper()
palavras = palavra.split()
variavel_global = ''

def beco(palavra):
  variavel = ''
  quant = len(palavra)
  espacos = 0
  letra = palavra[0]
  for e in palavra:
    variavel += (letra*espacos)
    variavel += e
    espacos+=1
    variavel+= (letra*(quant - espacos))
    variavel += '\n'
  return variavel


for e in range(len(palavras)):
  variavel_global += beco(palavras[e])
  variavel_global += '\n'

print(variavel_global)
pyperclip.copy(variavel_global)
