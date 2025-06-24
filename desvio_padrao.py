def desvio_padrao(lista, media, n):
    soma = 0
    for x in lista:
        soma += (x - media) ** 2
    final = (soma / (n -1)) ** (1/2)
    print(final)


vezes = int(input())
acumulado = 0
n = 0
lista = list()

for i in range (vezes):
    num = float(input())
    acumulado += num
    n += 1
    lista.append(num)
media = acumulado/n

desvio_padrao(lista, media, n)

    