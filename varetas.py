while True:
    n = int(input())
    if n == 0:
        break
    soma = 0
    for _ in range(n):
        comprimento, num_varetas = [int(w) for w in input().split()]
        soma += num_varetas // 2 * 2
    num_retangulos = soma // 4
    print(num_retangulos)