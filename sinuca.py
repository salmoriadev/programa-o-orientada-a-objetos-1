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
print(bolas)

'''num_bolas = int(input())
bolas = [int(x) for x in input().split() ]
proximas_bolas = []

for _ in range 
bolas = proximas_bolas
proximas_bolas = []'''