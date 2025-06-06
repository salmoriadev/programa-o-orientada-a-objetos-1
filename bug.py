lista_palavras = input().split('-')
nome = 'cobol'
resultado = 'GRACE HOPPER'

for i in range (len(lista_palavras)):
    if lista_palavras[i][0] != nome[i] and lista_palavras[i][-1] != nome[i]:
        resultado = 'BUG'
        break
    
print(resultado)
        