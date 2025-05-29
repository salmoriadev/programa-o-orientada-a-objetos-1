entrada_1 = input().split()
entrada_2 = input().split()

def compativel(entrada_1, entrada_2):
    resultado = 'Y'
    for i in range (len(entrada_1)):
        if entrada_1[i] == '1' and entrada_1[i] == entrada_2[i]:
            resultado = 'N'
            return resultado
            break
    return resultado

print(compativel(entrada_1, entrada_2))