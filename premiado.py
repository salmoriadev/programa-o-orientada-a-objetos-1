contador = 0
while True:
    contador += 1
    numero = int(input())
    if numero == 0:
        break
    lista = [int(x) for x in input().split()]
    premiado = 0
    for i in range(numero):
        if lista[i] == i+1:
            premiado = i+1
    print(f"Teste {contador}")
    print(premiado)
    print(' ')