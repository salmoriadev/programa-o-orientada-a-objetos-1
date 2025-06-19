while True:
    lista_dominios = []
    lista_imagem = []
    resultado = ''
    relacoes = int(input())
    if relacoes == 0:
        break
    for _ in range (relacoes):
        dominio, imagem = input().split(' -> ')
        lista_dominios.append(dominio)
        lista_imagem.append(imagem)

    if len(set(lista_dominios)) != len(lista_dominios):
        resultado = 'Not a function.'
    elif len(set(lista_imagem)) != len(lista_imagem):
        resultado = 'Not invertible.'
    else:
        resultado = 'Invertible.'
        
    print(resultado)