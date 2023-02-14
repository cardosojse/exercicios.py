dados = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    partidas.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    while True:
        total = (int(input(f'Quantas partidas {jogador["Nome"]} jogou? ')))
        if total > 0:
            break
        else:
            print('Número inválido.')
    print('Quantidade de gols por partida:')
    for g in range(0, total):
        partidas.append(int(input(f'    Partida {g+1} - ')))
    jogador['Gols'] = partidas[:]
    jogador['Total de gols'] = sum(partidas)
    dados.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('=-' * 15)
print('cod Nome Gols Total')
print('-' * 25)
for i, v in enumerate(dados):
    print(f' {i}  {v["Nome"]} {v["Gols"]} {v["Total de gols"]}')
print('-' * 25)
while True:
    cod = int(input('Digite o cod do jogador para informações mais detalhadas (999 para sair): '))
    if cod == 999:
        break
    if cod >= len(dados):
        print('Código inválido.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {dados[cod]["Nome"]}')
        for i, g in enumerate(dados[cod]['Gols']):
            print(f'Na partida {i+1}: {g} gols')
