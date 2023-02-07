homem = mulher = total = 0

while True:
    print('=-' * 15)
    print('     CADASTRO DE PESSOAS')
    print('=-' * 15)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if idade >= 18:
        total += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
    if resp in 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total} ')
print(f'Ao todo, tivemos {homem} homens cadastrados,', end=' ')
print(f'e {mulher} mulheres com menos de 20 anos.')
