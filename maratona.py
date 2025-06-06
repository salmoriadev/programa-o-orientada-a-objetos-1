numero_postos, distancia_maxima = [ int(x) for x in input().split() ]
posicao_atual = 0
termina_prova = 'S'
posicao_posto = [ int(x) for x in input().split() ]

for i in range (len(posicao_posto)):
    if posicao_posto[i] - posicao_atual > distancia_maxima:
        termina_prova = 'N'
    posicao_atual = posicao_posto[i]

print(termina_prova)
    