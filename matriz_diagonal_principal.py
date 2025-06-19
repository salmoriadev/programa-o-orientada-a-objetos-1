operacao = input()
lista = []
matriz = []
resultado = 0
contador = 0

for _ in range (12):
    for _ in range (12):
        elemento = float(input())
        lista.append(elemento)
    matriz.append(lista)
    lista = []
        
match (operacao):
    case 'S':
        for i in range (1,12):
            for j in range (i):
                resultado += matriz[i][j]
    case 'M':
        for i in range (1,12):
            for j in range (i+1):
                resultado += matriz[i][j]
                contador += 1
        resultado /= (contador) * 2
        
print(f"{resultado:.1f}")