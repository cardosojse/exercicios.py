from time import sleep

print('CAIXA ELETRÔNICO')
print(' ')

valor = int(input('Saque: R$'))
total = valor
ced = 100
tCed = 0

print(' ')
print('Por favor, aguarde...')
sleep(2)
print(' ')

print('Total sacado:')

while True:

    if total >= ced:
        total -= ced
        tCed += 1

    else:
        if tCed > 0:
            print(f'{tCed} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5

        tCed = 0
        if total == 0:
            break

print(' ')
print('Agradecemos a sua preferência. Volte sempre!')
