vezes_primeira_lista = int(input())
lista = list()
for i in range (vezes_primeira_lista):
    nome = input()
    lista.append(nome)

vezes_segunda_lista = int(input())
for i in range (vezes_segunda_lista):
    nome = input()
    lista.append(nome)
    
lista.sort()
for i in range (len(lista)):
    print(lista[i])
    
