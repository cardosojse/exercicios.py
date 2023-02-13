from time import sleep
jogador = {'Nome': str(input('Nome do jogador: '))}
total = int(input('Quantas partidas ele jogou? '))
print('Quantos gols ele marcou? ')
sleep(1)
partidas = []
for n in range(0, total):
    partidas.append(int(input(f'Partida {n+1}: ')))
jogador['Gols'] = partidas[:]
jogador['Total de Gols'] = sum(partidas)
print()
print(jogador)
print()
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print()
print(f'O jogador {jogador["Nome"]} jogou {total} partidas.')
for i, v in enumerate(partidas):
    print(f'  - Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["Total de Gols"]} gols.')
