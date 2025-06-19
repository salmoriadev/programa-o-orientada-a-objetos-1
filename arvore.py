vezes = int(input())
lista = []
quantas_arvores = dict()
espaco = input() # como o vpl adiciona um espaco a mais antes dos testes coloquei o input para não haver problemas

for _ in range (vezes):
	while True:
		arvore = input()
		if arvore == '':
			break
		lista.append(arvore)
		lista.sort()
	
	for especie_arvore in lista:
		if especie_arvore not in quantas_arvores:
			quantas_arvores[especie_arvore] = round((lista.count(especie_arvore) / len(lista)) * 100, 4)
			print(f"{especie_arvore} {quantas_arvores[especie_arvore]:.4f}")
	lista.clear()
	quantas_arvores.clear()