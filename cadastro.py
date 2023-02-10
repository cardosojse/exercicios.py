data = []
register = []
count = maior = menor = 0

while True:
    count += 1
    print(f'{count}º PESSOA')
    register.append(str(input('NOME: ')))
    register.append(float(input('PESO: ')))
    if len(data) == 0:
        maior = menor = register[1]
    else:
        if register[1] > maior:
            maior = register[1]
        if register[1] < menor:
            menor = register[1]
    data.append(register[:])
    register.clear()

    awnser = ' '
    while awnser not in 'SN':
        awnser = str(input('Deseja continuar?[S/N]: ')).upper()
    if awnser == 'N':
        break

print(f'Você cadastrou {len(data)} pessoas.')

print(f'O maior peso foi {maior}kg. Peso de:', end=' ')
for p in data:
    if p[1] == maior:
        print(f'{p[0]}')

print(f'O menor peso foi {menor}kg. Peso de:', end=' ')
for p in data:
    if p[1] == menor:
        print(f'{p[0]}')
