quantidade = int(input())
coelhos = 0
ratos = 0
sapos = 0

for i in range (quantidade):
    numero_de_animais, inicial_animal = input().split()
    match inicial_animal:
        case "C":
            coelhos += int(numero_de_animais)
        case "R":
            ratos += int(numero_de_animais)
        case "S":
            sapos += int(numero_de_animais)

total_cobaias = coelhos + ratos + sapos
percentual_coelhos = coelhos / total_cobaias * 100
percentual_ratos = ratos / total_cobaias * 100
percentual_sapos = sapos / total_cobaias * 100

print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")