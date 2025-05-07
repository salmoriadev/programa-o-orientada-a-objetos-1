parenteses = input()
if count(')') == count('('):
    print('Partiu RU!')
else:
    numero = count('(') - count(')')
    print('Ainda falta(m) {} assunto(s) pendente(s)!'.format(numero))