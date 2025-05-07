vezes = int(input())
for i in range(vezes):
    codigo = input()
    numero1 = int(codigo[0])
    numero2 = int(codigo[2])
    if numero1 == numero2:
        numero_final = numero1 * numero2
    elif codigo[1] == codigo[1].lower():
        numero_final = numero1 + numero2
    else:
        numero_final = numero1 - numero2
    print(numero_final)