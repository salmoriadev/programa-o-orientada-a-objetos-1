casos_testes = int(input())
for _ in range (casos_testes):
    quantidade_alunos, num_secreto = map(int, input().split())
    numeros = [int(x) for x in input().split()]
    mais_proximo = 100 # valor impossivel
    contador = 1
    indice_proximo = 0
    distancia_mais_proxima = 100 # valor impossivel

    for chute in numeros:
        distancia = abs(num_secreto - chute)
        if distancia == 0:
            indice_proximo = contador
            break
        elif distancia < distancia_mais_proxima:
            indice_proximo = contador
            mais_proximo = chute
            distancia_mais_proxima = distancia
        elif distancia == distancia_mais_proxima:
        	indice_proximo == mais_proximo
        contador += 1
    print(indice_proximo)