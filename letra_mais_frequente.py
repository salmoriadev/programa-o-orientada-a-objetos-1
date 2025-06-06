frase = input().lower().split()
letras = []
letra_mais_frequente = ''

for i in range (len(frase)):
	for j in range (len(frase[i])):
		letras.append(frase[i][j])

for i in range (len(letras)):
	if letras.count(letras[i]) > letras.count(letra_mais_frequente):
		letra_mais_frequente = letras[i]

print(letra_mais_frequente)