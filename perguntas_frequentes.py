while True:
	num_perguntas, frequente = [int(x) for x in input().split()]
	if num_perguntas == 0 and frequente == 0:
		break
	conjunto = set()
	perguntas = input().split()
	for i in range (len(perguntas)):
		if perguntas.count(perguntas[i]) >= frequente:
			conjunto.add(perguntas[i])
	print(len(conjunto))