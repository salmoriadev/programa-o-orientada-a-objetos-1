linha = int(input())
operacao = input()
lista = []
matriz = []
resultado = 0

for _ in range (12):
    for _ in range (12):
        elemento = float(input())
        lista.append(elemento)
    matriz.append(lista)
    lista = []
        
match (operacao):
    case 'S':
        resultado += matriz[linha][i] for i in range (12)
    case 'M':
        resultado += 1
        resultado *= matriz[linha][i] for i in range (12)
        
print(resultado)
    