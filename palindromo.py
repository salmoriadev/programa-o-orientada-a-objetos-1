def eh_palindromo(frase):
    limpa = ''
    for letra in frase.lower():
        if letra.isalpha():
            limpa += letra
    return limpa == limpa[::-1]

frase = input()
print(eh_palindromo(frase))