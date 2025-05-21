def primo(i):
    if i < 2:
        return False
    # Verifica se o número é divisível por qualquer número entre 2 e i-1
    for b in range(2, int(i ** 0.5) + 1):  # O número não precisa ser testado até i-1, apenas até a raiz quadrada de i
        if i % b == 0:  # Se encontrar algum divisor, o número não é primo
            return False
    return True  # Se não encontrar divisores, é primo

inicio = int(input("Digite o início do intervalo: "))  
fim = int(input("Digite o fim do intervalo: "))
num_primos = 0
for i in range(inicio, fim + 1):  # Inclui o número 'fim' no intervalo
    if primo(i):
        num_primos += 1

print(num_primos)  # Exibe o número primo