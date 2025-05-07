def tautograma(frase):
    palavras = frase.split()
    for i in range(len(palavras)):
        palavra = palavras[i]
        if palavra[0] != frase[0]:
            return print('N')
            break 
    return print('Y')
while True:
    frase = input().lower()
    if frase == '*':
        break
    tautograma(frase)