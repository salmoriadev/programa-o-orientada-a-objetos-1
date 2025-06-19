quantidade_casos = int(input())

for casos in range (quantidade_casos):
    numero_bolas = int(input())
    x_bola_branca, y_bola_branca = [int(w) for w in input().split()]
    menor_distancia = 3176  # maior que o valor maximo que a distancia pode assumir
    for i in range(numero_bolas):
        x_bola, y_bola = [int(w) for w in input().split()]
        distancia = ((x_bola - x_bola_branca) ** 2 + (y_bola - y_bola_branca) ** 2) ** (1/2)
        if distancia < menor_distancia: # ira atualizar a menor distancia possivel sempre que aparecer um valor menor
            menor_distancia = distancia
            bola = i + 1
    print(bola)