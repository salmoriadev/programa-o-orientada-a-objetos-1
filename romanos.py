valores_romanos = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
numero_romano = input()
                   
decimal = 0
for i in range(len(numero_romano) - 1):
    dr = numero_romano[i]
    dr_seguinte = numero_romano[i+1]
    if valores_romanos[dr] >= valores_romanos[dr_seguinte]:
        decimal += valores_romanos[dr]
    else:
        decimal -= valores_romanos[dr]
decimal += valores_romanos[numero_romano[-1]]
                   
print(decimal)