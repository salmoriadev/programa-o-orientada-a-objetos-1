numero_grupos = int(input())
dicionario_grupos = dict()
lista_candidatos = []
aprovados = []
vagas_totais = 0

for _ in range (numero_grupos):
    grupo, vagas = input().split()
    vagas = int(vagas)
    vagas_totais += vagas
    dicionario_grupos[grupo] = vagas
    
numero_candidatos = int(input())
for _ in range (numero_candidatos):
    nome, nota, grupo_candidato = input().split()
    lista_candidatos.append([nome, grupo_candidato])
candidatos_nao_selecionados = lista_candidatos.copy()

for i in range (len(lista_candidatos)):
    if lista_candidatos[i][1] !='G' and dicionario_grupos[lista_candidatos[i][1]] != 0:
        dicionario_grupos[lista_candidatos[i][1]] -= 1
        aprovados.append(lista_candidatos[i][0])
        candidatos_nao_selecionados.remove(lista_candidatos[i])
        vagas_totais -= 1
    elif dicionario_grupos['G'] != 0:
        dicionario_grupos['G'] -= 1
        aprovados.append(lista_candidatos[i][0])
        candidatos_nao_selecionados.remove(lista_candidatos[i])
        vagas_totais -= 1
        
if vagas_totais != 0:
    for i in range (min(vagas_totais, len(candidatos_nao_selecionados))):
        aprovados.append(candidatos_nao_selecionados[i][0])

aprovados.sort()
for aprovado in aprovados:
    print(aprovado)