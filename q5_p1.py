while True:
    x, y = [int(w) for w in input().split()]
    if x == 0 or y == 0:
        break
    elif x > 0 and y > 0:
        quadrante = "primeiro"
    elif  x < 0 and y > 0:
        quadrante = "segundo"
    elif  x < 0 and y < 0:
        quadrante = "terceiro"
    elif  x > 0 and y < 0:
        quadrante = "quarto"
    print(quadrante)