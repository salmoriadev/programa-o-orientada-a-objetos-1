teste = 0
while True:
    x1, y1, x2, y2 = [int(w) for w in input().split()]
    if x1 +x2 + y1 + y2 == 0:
        break
    menor_x = min(x1, x2)
    maior_x = max(x1,x2)
    menor_y = min(y1, y2)
    maior_y = max(y1, y2)
    cairam_dentro = 0
    numero_meteoritos = int(input())
    for i in range (numero_meteoritos):
        x_meteoro, y_meteoro = [int(w) for w in input().split()]
        if x_meteoro >= menor_x and x_meteoro <= maior_x and y_meteoro >= menor_y and y_meteoro < maior_y:
            cairam_dentro += 1
    teste += 1
    print(f"Teste {teste}")
    print(cairam_dentro)