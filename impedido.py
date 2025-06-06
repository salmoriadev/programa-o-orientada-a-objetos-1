while True:
    num_atacantes, num_zagueiros = [ int(x) for x in input().split() ]
    
    if num_atacantes == 0 and num_zagueiros == 0:
        break

    posicao_ataque = [ int(x) for x in input().split() ]
    distancia_ataque = min(posicao_ataque)
            
    posicao_defesa = [ int(x) for x in input().split() ]
    posicao_defesa.pop(posicao_defesa.index(min(posicao_defesa)))
    distancia_defesa = min(posicao_defesa)
    
    if distancia_ataque < distancia_defesa:
        print('Y')
    else:
        print('N')