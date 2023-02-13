from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador Um': randint(1, 6),
        'Jogador Dois': randint(1, 6),
        'Jogador Três': randint(1, 6),
        'Jogador Quatro': randint(1, 6)}
ranking = []

print('CADA JOGADOR LANÇARÁ UM DADO!')
print()
sleep(1)

for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(2)
print()
print('=-' * 15)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')
print('=-' * 15)
