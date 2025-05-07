# João e Maria, desenvolveram um novo método para comunicação criptografada que implica a necessidade de obter-se o produto de dois número primos a partir de dois número aleatórios utilizados como semente. O cálculo consiste dos seguintes passos:

#Obtem-se dois números aleatórios N e M maiores ou iguais a 2, N ≤ M;
#Procura-se dois números primos P1 e P2 de tal forma que eles sejam o mais próximo possível dos números N e M, respectivamente, sendo que P1 ≤ N e P2 ≥ M.
#O valor procurado correspondente à multiplicação de P1 por P2.
#Faça um programa que dado os números N e M imprima o produto dos números primos P1 e P2.

#Entrada:
#Uma linha contendo dois valores inteiros N e M:

#10 15

#Saída:
#O produto dos primos computados conforme passos acima:

#119

#OBS: No tópico de "Exercícios Resolvidos" está implementada uma função que permite verificar se um dado número é primo ou não.


import math

def eh_primo(n):
    if n == 1:
        eh_primo = False
    elif n != 2 and n % 2 == 0:
        eh_primo = False
    else:
        eh_primo = True
        raiz = int(math.sqrt(n))
        for i in range(3, raiz+1, 2):
            if n % i == 0:
                eh_primo = False
                break
        
    return eh_primo


n, m = [int(x) for x in input().split()]

while True:
    if eh_primo(n) is False:
        n -= 1
    else:
        break

while True:
    if eh_primo(m) is False:
        m += 1
    else:
        break

print(m * n)