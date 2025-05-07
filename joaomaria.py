mary = 0
john = 0

while True:
    vezes = int(input())
    if vezes == 0:
        break
    lista = input()
    mary += int(lista.count('0'))
    john += int(lista.count('1'))
    print(f'Mary won {mary} times and John won {john} times')
    mary = 0
    john = 0