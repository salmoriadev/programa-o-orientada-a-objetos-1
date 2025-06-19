numero_cartas, limite_repeticao = input().split()
numero_cartas = int(numero_cartas)
limite_repeticao = int(limite_repeticao)
lista_numeros = []
lista_naipe = []
eh_embaralhado = True
contador_numero = 1
contador_naipe = 1

for _ in range (numero_cartas):
    numero, naipe = input().split()
    lista_numeros.append(numero)
    lista_naipe.append(naipe)

for i in range (numero_cartas - limite_repeticao +1):
    if lista_numeros[i] == lista_numeros[i+1]:
        contador_numero += 1
    else:
        contador_numero = 1
    if lista_naipe[i] == lista_naipe[i+1]:
        contador_naipe += 1
    else:
        contador_naipe = 1
    if contador_numero == limite_repeticao or contador_naipe == limite_repeticao:
        eh_embaralhado = False

print(eh_embaralhado)