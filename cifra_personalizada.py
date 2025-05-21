alfabeto = input().lower()
alfabeto_cifrado = input().lower()
mensagem_cifrada = input().lower()
mensagem_decifrada = ""
for letra in mensagem_cifrada:
    if not letra.isalpha():
        mensagem_decifrada += letra
    else:
        for i in range (len(alfabeto_cifrado)):
            if letra == alfabeto_cifrado[i]:
                mensagem_decifrada += alfabeto[i]
                break
        
print(mensagem_decifrada)