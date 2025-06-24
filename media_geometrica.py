quantos_numeros = int(input())
produto = 1

for _ in range (quantos_numeros):
    num = float(input())
    produto = num * produto
    
num_final = (produto) ** (1 / quantos_numeros)
print(num_final)