notas = input().split()
notas.sort()
notas.pop(0)
notas.pop(-1)
numeros = [float(x) for x in notas]
total = sum(numeros)
print(total)