from random import randint
from time import sleep

print('     ROCK PAPER SCISSORS!')

itens = ('ROCK', 'PAPER', 'SCISSORS')
pc = randint(0, 2)

print("""
CHOOSE YOUR OPTION:

[0] ROCK
[1] PAPER
[2] SCISSORS
""")

player = int(input('YOUR OPTION: '))

print(' ')

print('ROCK...')
sleep(1)
print('PAPER...')
sleep(1)
print('SCISSORS...')
sleep(1)

print(' ')

print('=-' * 11)
print(f'PLAYER CHOSE {itens[player]}')
print(f'PC CHOSE {itens[pc]}')
print('=-' * 11)

print(' ')

if pc == 0:
    if player == 0:
        print('DRAW')
    elif player == 1:
        print('PLAYER WINS')
    elif player == 2:
        print('PC WINS')
elif pc == 1:
    if player == 0:
        print('PC WINS')
    elif player == 1:
        print('DRAW')
    elif player == 2:
        print('PLAYER WINS')
elif pc == 2:
    if player == 0:
        print('PC WINS')
    elif player == 1:
        print('PLAYER WINS')
    elif player == 2:
        print('DRAW')

