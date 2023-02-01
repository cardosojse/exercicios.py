media = 0
sI = 0  # sI é a soma das idades.
mI = 0  # mI é a maior idade entre os homens.
sM = 0  # sM é a soma de mulheres com menos de 20 anos.
nM = 0  # nM é o nome do homem com maior idade.

n = int(input('Quantas pessoas você irá entrevistar? '))
for c in range(1, n+1):
    print(f'=-=-= {c}º PESSOA =-=-=')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('SEXO [M/F]: ')).upper()
    sI += idade
    if sexo == 'M':
        if c == 1:
            mI = idade
            nM = nome
        elif idade > mI:
            mI = idade
            nM = nome
    else:
        if idade < 20:
            sM += 1
media = sI / n
print(f'A média de idade do grupo é {media:.1f} anos')
print(f'O homem mais velho do grupo tem {mI} anos e se chama {nM}.')
print(f'Ao todo são {sM} mulheres com menos de 20 anos.')