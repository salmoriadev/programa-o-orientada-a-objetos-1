num_testes = 1
while True:
	num_aeroporto, num_voo = [int(x) for x in input().split()]

	if num_aeroporto == 0 and num_voo == 0:
		break
	lista = []
	for i in range (num_voo):
		aeroporto_um, aeroporto_dois = [ int(x) for x in input().split() ]
		lista.append(aeroporto_um)
		lista.append(aeroporto_dois)
	maior_transito = 0
	aeroporto_maior_transito = 0
	for i in range (1, num_aeroporto):
		transito_aeroporto_i = lista.count(i)
		if transito_aeroporto_i > maior_transito:
			maior_transito = transito_aeroporto_i
			aeroporto_maior_transito = i
			aeroporto_maior_transito_impressao = str(i)
		elif transito_aeroporto_i == maior_transito:
		    aeroporto_maior_transito_impressao += ' ' + str(i)
			
	print(f"Teste {num_testes}")
	print(aeroporto_maior_transito_impressao)
	print(' ')
	num_testes += 1