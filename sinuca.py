num_bolas = int(input())
bolas = [int(x) for x in input().split() ]
for _ in range (num_bolas-1):
	for _ in range (len(bolas)-1):
		if bolas[0] + bolas[1] == 0:
			bolas.pop(0)
			bolas.append(-1)
		else:
			bolas.pop(0)
			bolas.append(1)
		if len(bolas) == 2:
			break
	bolas.pop(0)
	if bolas[0] == -1:
	    resultado = 'branca'
	else:
	    resultado = 'preta'
print(resultado)