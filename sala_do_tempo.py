import pyperclip
 
palavra = input("palavra: ")
palavra = palavra.upper()
quant = int(input('vezes: '))
variavel = ''

while(quant != 0):
  variavel+=palavra
  variavel+='\n'
  quant-=1

print(variavel)
pyperclip.copy(variavel)

