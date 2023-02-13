from datetime import date
atual = date.today().year

dados = {'Nome': str(input('Nome: ')),
         'Nascimento': int(input('Ano de nascimento: '))}

dados['Idade'] = atual - dados['Nascimento']
del dados['Nascimento']

while True:
    dados['CTPS'] = int(input('Carteira de Trabalho(Digite 0 se não tiver): '))
    if dados['CTPS'] == 0:
        break
    else:
        dados['Contratação'] = int(input('Ano de contratação: '))
        dados['Salário'] = float(input('Salário: R$'))
        dados['Aposentadoria'] = 70 - dados['Idade']
        break
print('=-' * 20)
for k, v in dados.items():
    print(f' - {k} tem valor {v}.')
