dados = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Digite M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    dados.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('=-=-=DADOS CADASTRAIS=-=-=')
print(f'Ao todo {len(dados)} pessoas foram cadastradas.')
media = soma / len(dados)
print(f'A media de idade entre as pessoas é de {media:.1f} anos.')
print('Lista com todas as mulheres:', end=' ')
for p in dados:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]};', end=' ')
print('\nPessoas com idade acima da média:')
for p in dados:
    if p['Idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
