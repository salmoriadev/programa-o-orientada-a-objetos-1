vezes = int(input())
for _ in range(vezes):
    print(*sorted(set(input().split())))