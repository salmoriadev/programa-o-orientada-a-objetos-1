frase_cifrada = input()
frase_cifrada_em_ordem = ''
frase_decifrada = ''
for i in range (len(frase_cifrada)):
    frase_cifrada_em_ordem += frase_cifrada[len(frase_cifrada)-i-1]  #frase fica na ordem correta
    
frase_separada = frase_cifrada_em_ordem.split() #separo a frase em uma lista para desconsiderar o espaco
for i in range (len(frase_separada)):
    for j in range (2,len(frase_separada[i]),3):  #pula a letra e numero indesejado
        frase_decifrada += frase_separada[i][j]
    if i != len(frase_separada)-1:
        frase_decifrada += ' '

print(frase_decifrada)