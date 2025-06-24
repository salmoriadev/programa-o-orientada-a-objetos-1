lista_medias = []
for _ in range (12):
    valores = [int(x) for x in input().split()]
    media = round(sum(valores) / len(valores), 2)
    lista_medias.append(media)
print(*lista_medias)