while True:
    num_suspeitos = int(input())
    if num_suspeitos == 0:
        break
    suspeitos = [int(x) for x in input().split() ]
    suspeitos_ordenados = suspeitos.copy()
    suspeitos_ordenados.sort(reverse = True)
    print(suspeitos.index(suspeitos_ordenados[1])+1)