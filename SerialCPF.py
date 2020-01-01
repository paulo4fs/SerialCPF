import random

def cpfgenerator():
    while True:
        codigo = '1234567890'
        lista = []
        for i in range(9):
            lista.append(random.choice(codigo))

        dig9 = estado()                     # Escolha do estado
        
        if not dig9 == 99:
            lista[8] = dig9

        dig1 = PrimeiroDigito(lista)        # primeiro digito
        lista.append(dig1)

        dig2 = SegundoDigito(lista)         # Segundo digito
        lista.append(dig2)

        cpf = lista[0:3]+['.']+lista[3:6]+['.'] + \
            lista[6:9]+['-']+lista[9:]      # formatador
        cpf = ''.join(str(a) for a in cpf)
        print(cpf)
        continua = input('Deseja continuar? (s/n) ')

        if continua.lower() == 'n':
            break

    return()

def estado():
    print('''
    ESTADOS
    1 - DF, GO, MS e TO;
    2 - PA, AM, AC, AP, RO e RR;
    3 - CE, MA e PI;
    4 - PE, RN, PA e AL;
    5 - BA e SE;
    6 - MG;
    7 - RJ e ES;
    8 - SP;
    9 - PA e SC;
    0 - RS.\n''')

    dig9 = input('Digite o número correspondente ao estado do CPF: ')

    if dig9 == '':
        dig9 = 99
    return(dig9)

def PrimeiroDigito(lista):
    count = 10
    soma9 = 0
    for i in lista:
        soma9 += int(i)*count
        count -= 1
    resto = soma9 % 11
    if resto < 2:
        dig1 = 0
    else:
        dig1 = 11-resto
    return(dig1)

def SegundoDigito(lista):
    count = 11
    soma10 = 0
    for i in lista:
        soma10 += int(i)*count
        count -= 1
    resto = soma10 % 11
    if resto < 2:
        dig2 = 0
    else:
        dig2 = 11-resto
    return(dig2)

cpfgenerator()