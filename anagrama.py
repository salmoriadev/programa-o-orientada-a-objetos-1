def anagrama(frase1, frase2):
    if frase1 == frase2:
        return False
    elif len(frase1) == len(frase2):
        for letra in frase1:
            if frase1.count(letra) != frase2.count(letra):
                return False
        return True
    else:
        return False
    
frase1 = input()
frase2 = input()
print(anagrama(frase1, frase2))
