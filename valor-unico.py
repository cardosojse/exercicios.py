valor = []
while True:
    n = int(input('Digite um número: '))
    if n not in valor:
        valor.append(n)
        print('Adicionei um novo número.')
    else:
        print('Valor duplicado. Não irei adicioná-lo.')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]: ')).upper().strip()
    if resp == 'N':
        break
print(f'Valores adicionados: {valor}')
