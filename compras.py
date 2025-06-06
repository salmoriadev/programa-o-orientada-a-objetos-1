'''vezes = int(input())

for _ in range(vezes):
    lista = input().split()
    nova_lista = []

    for palavra in lista:
        if palavra not in nova_lista:
            nova_lista.append(palavra)

    print(' '.join(nova_lista))'''
n = int(input())
for _ in range(n):
    print(*sorted(set(input().split())))