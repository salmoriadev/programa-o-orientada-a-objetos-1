vezes = int(input())
contagem = 0
for i in range (vezes):
    nome = input()
    if 'Maria ' in nome:
        contagem += 1
    elif 'Maria' in nome and nome[-1] == 'a':
        contagem += 1
print(contagem)