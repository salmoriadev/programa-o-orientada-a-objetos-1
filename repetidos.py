casos = int(input())

for _ in range (casos):
    lista = input().split()
    for j in range (len(lista)):
        for i in range(len(lista), 1):
            if lista[j] == lista[i]:
                lista.pop(j)
                break
print(lista)