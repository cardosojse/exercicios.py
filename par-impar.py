from random import randint
total = 0
print(' ')
print('     VAMOS JOGAR PAR OU IMPAR?')
while True:
    print(' ')
    pc = randint(1, 10)
    valor = int(input('Digite um valor: '))
    total = valor + pc
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou impar?: ')).upper().strip()[0]
    if total % 2 == 0:
        print(f'Você escolheu {valor} e o computador escolheu {pc}. {total} é PAR.')
        if escolha == 'P':
            print('VOCÊ VENCEU! Vamos novamente?')
        else:
            break
    else:
        print(f'Você escolheu {valor} e o computador escolheu {pc}. {total} é IMPAR.')
        if escolha == 'I':
            print('VOCÊ VENCEU! Vamos novamente?')
        else:
            break
print('VOCÊ PERDEU!')
