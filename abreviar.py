nome_completo = input().split()
nome_abreviado = list()
primeiro_nome = nome_completo[0]
ultimo_nome = nome_completo[-1]

if len(nome_completo) > 2:
    for palavra in nome_completo[1:-1]:
        if palavra != primeiro_nome and palavra != ultimo_nome and len(palavra) > 3:
            nome_abreviado.append(palavra[0] + ".")
        else:
            nome_abreviado.append(palavra)
    nome_abreviado_str = " ".join(nome_abreviado)
    nome_abreviado_completo = primeiro_nome + " " + nome_abreviado_str + " " + ultimo_nome
else:
    nome_abreviado_completo = " ".join(nome_completo)

print(nome_abreviado_completo)