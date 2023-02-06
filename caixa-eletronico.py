print('CAIXA ELETRÔNICO')

valor = int(input('Saque: R$'))
total = valor
ced = 100
tCed = 0
while True:
    if total >= ced:
        total -= ced
        tCed += 1
    else:
        if tCed > 0:
            print('')