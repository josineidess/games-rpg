import pyperclip

palavra = input('palavra: ')
variavel = ''
palavra2 = ''


for e in palavra:
  palavra2+=e
  palavra2+=e


quant = len(palavra2)
fim = 2
for e in palavra:
  variavel += palavra2[0:fim]
  variavel += '\n'
  fim+=2

variavel += palavra2
variavel += '\n'

for e in palavra:
  variavel += palavra2[0:quant-2]
  variavel += '\n'
  quant-=2

print(variavel)
pyperclip.copy(variavel)


