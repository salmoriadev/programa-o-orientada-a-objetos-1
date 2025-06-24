while True:
    
    numero_pessoas = int(input())
    if numero_pessoas == 0:
        break
    tempo = input().split()
    tempo_ligado = 0
    for i in range (len(tempo)):
        if i == (len(tempo)-1):
            tempo_ligado += 10
            break
        elif int(tempo[i+1]) - int(tempo[i]) >= 10:
            tempo_ligado += 10
        else:
            tempo_ligado += int(tempo[i+1]) - int(tempo[i])
    
    print(tempo_ligado)