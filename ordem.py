entrada_strings = input().split()
ordem = ''
lista_numeros = [int(item) for item in entrada_strings]
if lista_numeros == sorted(lista_numeros):
    ordem = 'C'
elif lista_numeros == sorted(lista_numeros, reverse=True):
    ordem = 'D'
else:
    ordem = 'N'

print(ordem)