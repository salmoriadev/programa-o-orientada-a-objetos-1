caixa = dict()
tipos_notas = int(input())

for i in range (tipos_notas):
    valor = float(input())
    qntd_notas = int(input())
    caixa[valor] = caixa.get(valor, qntd_notas)

valor_saque = float(input())

    multiplica_ultimo = valor_saque // max(caixa.values())