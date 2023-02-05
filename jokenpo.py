from random import randint
from time import sleep

print('     JO-KEN-PÔ!')

itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)

print("""
ESCOLHA SUA OPÇÃO

[0] PEDRA
[1] PAPEL
[2] TESOURA
""")

player = int(input('SUA OPÇÃO: '))

print(' ')

print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ!')
sleep(1)

print(' ')

print('=-' * 11)
print(f'JOGADOR ESCOLHEU {itens[player]}')
print(f'COMPUTADOR ESCOLHEU {itens[pc]}')
print('=-' * 11)

print(' ')

if pc == 0:
    if player == 0:
        print('EMPATE.')
    elif player == 1:
        print('O JOGADOR VENCEU!')
    elif player == 2:
        print('O COMPUTADOR VENCEU!')
elif pc == 1:
    if player == 0:
        print('O COMPUTADOR VENCEU!')
    elif player == 1:
        print('EMPATE.')
    elif player == 2:
        print('O JOGADOR VENCEU!')
elif pc == 2:
    if player == 0:
        print('O COMPUTADOR VENCEU')
    elif player == 1:
        print('O JOGADOR VENCEU!')
    elif player == 2:
        print('EMPATE')

