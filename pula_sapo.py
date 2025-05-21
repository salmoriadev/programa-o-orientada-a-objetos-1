altura_pulo, qtdade = [int(x) for x in input().split()]
alturas = [int(x) for x in input().split()]
resultado = "YOU WIN"

for i in range (qtdade):
    if len(alturas) == i+1:
        break
    dif_alt = abs(alturas[i] - alturas[i+1])
    if dif_alt > altura_pulo:
        resultado = "GAME OVER"
        break
    
print(resultado)