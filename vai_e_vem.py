import pyperclip

palavra = input('palavra:')
palavra = palavra.upper()
quant = len(palavra)
cont = 0
variavel = '```'

for e in palavra:
  variavel += palavra[cont]
  variavel += palavra[quant-1]
  variavel += '\n'
  cont+=1
  quant-=1

variavel += '```'
print(variavel)
pyperclip.copy(variavel)
