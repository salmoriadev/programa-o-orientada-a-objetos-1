texto, dinic = input().split()
dinic = int(dinic)
hinic, minic, sinic = [int(x) for x in input().split(" : ")]

texto, dfim = input().split()
dfim = int(dfim)
hfim, mfim, sfim = [int(x) for x in input().split(" : ")]

segundos = (dfim - dinic - 1) * 24 * 3600 + \
           hfim * 3600 + mfim * 60 + sfim + \
           24 * 3600 - (hinic * 3600 + minic * 60 + sinic)

dias = segundos // (24 * 3600)
segundos -=  dias * 24 * 3600
horas = segundos // 3600
segundos -=  horas * 3600
minutos = segundos // 60
segundos -= minutos * 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")