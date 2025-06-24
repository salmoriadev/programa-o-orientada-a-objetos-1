def eh_magico(matriz):
    contador = 0
    contador_2 = 0
    for i in range(tam_matriz):
        for j in range(tam_matriz):
            contador += matriz[i][j]
            contador_2 += matriz[i][j]
        if contador != contador_2 or contador != referencia:
            return False
        contador = 0
        contador_2 = 0

    else:
        contador = 0
        contador_2 = 0
        for i in range (tam_matriz):
            contador += matriz[i][i]
            contador_2 += matriz[i][tam_matriz - i - 1]
        if contador != contador_2 or contador != referencia:
            return False
        else:
            return True

tam_matriz = int(input())
matriz = []

for _ in range (tam_matriz):
    linha = [int(x) for x in input().split()]
    referencia = sum(linha)
    matriz.append(linha)
    
print(eh_magico(matriz))