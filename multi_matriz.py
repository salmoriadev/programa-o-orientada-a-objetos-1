tam_matriz = int(input())
a = 0
b = 0
C = 0
P, Q, R, S, X, Y = [int(x) for x in input().split()]
I, J = [int(x) for x in input().split()]

A = [(P * I + Q * j) % X for j in range (1,tam_matriz+1)]
B = [(R * i + S * J) % Y for i in range (1,tam_matriz+1)]

for i in range (tam_matriz):
    C += A[i] * B[i]
print(C)