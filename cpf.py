def eh_valido(cpf,novo_cpf):
    if cpf == cpf[0] * 11:
        return False
    if len(cpf) != 11 and cpf.isdigit() is False:
        for i in cpf:
            if i.isdigit():
                novo_cpf += i
        cpf = novo_cpf
    elif len(cpf) != 11 and cpf.isdigit():
        return False
    penultimo_numero = (int(cpf[0])*1 + int(cpf[1])*2 + int(cpf[2])*3 + int(cpf[3])*4 + int(cpf[4])*5 + int(cpf[5])*6 + int(cpf[6])*7 + int(cpf[7])*8 + int(cpf[8])*9) % 11
    ultimo_numero = (int(cpf[0])*0 + int(cpf[1])*1 + int(cpf[2])*2 + int(cpf[3])*3 + int(cpf[4])*4 + int(cpf[5])*5 + int(cpf[6])*6 + int(cpf[7])*7 + int(cpf[8])*8 + penultimo_numero*9) % 11
    if penultimo_numero == int(cpf[9]) and ultimo_numero == int(cpf[10]):
        return True
    else:
        return False
novo_cpf = ''
cpf = input()
print(eh_valido(cpf,novo_cpf))