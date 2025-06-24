casos = int(input())
especies = []
for _ in range(casos):
    especies_numero = dict()
    while True:
        especie = input()
        especies.append(especie)
        if especie == "":
            break
    for i in range(len(especies)):
        contador = 0
        for j in range(len(especies)):
            if especies[i] == especies[i - j]:
                contador += 1
        especies_numero.get(especies[i], contador)

print(especies_numero)
    
