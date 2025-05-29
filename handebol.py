num_jogadores, num_partidas = map(int, input().split())

contador = 0

for _ in range (num_jogadores):
    gols = [int(x) for x in input().split()]
    for gol in gols:
        if gol == 0:
            contador -= 1
            break
    contador += 1
    
print(contador)