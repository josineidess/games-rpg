import pyperclip

palavra = input('palavra: ')
palavra = palavra.upper()
inicio = 1
fim = len(palavra)
inicio_metade = 0
fim_metade = inicio
vezes = fim
variavel = '```'

cont=0
v=0

for e in palavra:
  if e == ' ':
    v+=1
    cont = v
    break
  else:
    v+=1


if cont!=vezes and cont!=0:
  palavra1 = palavra[0:cont-1]
else:
  palavra1 = palavra

variavel += palavra1
variavel += '\n'

for e in palavra1:
  variavel += palavra1[inicio:fim]
  variavel += palavra1[inicio_metade:fim_metade]
  variavel += '\n'
  inicio+=1
  fim_metade = inicio

variavel+='\n'

inicio = 1
fim = len(palavra)
inicio_metade = 0
fim_metade = inicio
vezes = fim

if cont != vezes and cont!=0:
  palavra2 = palavra[cont:fim]
  variavel += palavra2
  variavel += '\n'
  for e in palavra2:
    variavel += palavra2[inicio:fim]
    variavel += palavra2[inicio_metade:fim_metade]
    variavel += '\n'
    inicio+=1
    fim_metade = inicio
variavel+='```'

print(variavel)
pyperclip.copy(variavel)
