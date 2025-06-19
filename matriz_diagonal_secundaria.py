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
        for i in range (11):
            for j in range (11-i):
                resultado += matriz[i][j]
    case 'M':
        for i in range (11):
            for j in range (11-i):
                resultado += matriz[i][j]
                contador += 1
        resultado /= contador
        
print(f"{resultado:.1f}")