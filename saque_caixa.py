qntd_valores = int(input())
dicionario = dict()
lista_valores = []
for _ in range (qntd_valores):
	valor = float(input())
	qntd = int(input())
	dicionario[valor] = qntd
	lista_valores.append(valor)
saque = float(input())
valores = sorted(dicionario.keys(), reverse=True)
notas_utilizadas = []
for valor in valores:
    qntd = min(int(saque // valor), dicionario[valor])
    notas_utilizadas.append(qntd)
    saque -= qntd * valor
    
notas_utilizadas.reverse()
print(*notas_utilizadas)