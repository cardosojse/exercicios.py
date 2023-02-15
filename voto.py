def voto(ano):
    from datetime import date
    actual = date.today().year
    idade = actual - ano
    if idade < 16:
        return f'Você tem {idade} anos. Não possui idade suficiente para votar.'
    if 16 <= idade < 18 or idade > 65:
        return f'Você tem {idade} anos. Seu voto é opcional.'
    else:
        return f'Você tem {idade} anos. Seu voto é obrigatório.'


print('DESEJA VOTAR? Responda a pergunta abaixo: ')
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
