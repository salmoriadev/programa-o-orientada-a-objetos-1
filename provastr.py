gabarito = input()
respostas = input()
acertos = 0
for i in range(len(respostas)):
    if respostas[i] == gabarito[i]:
        acertos += 1
print(acertos)