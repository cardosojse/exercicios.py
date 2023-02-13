total = count = average = more = less = 0
while True:
    number = int(input('Digite um número: '))
    total += number
    count += 1
    if count == 1:
        more = less = number
    else:
        if number > more:
            more = number
        if number < less:
            less = number
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]: ')).upper().strip()
    if resp == 'N':
        break
average = total / count
print('ACABOU :(')
print(f'''Soma total dos números digitados = {total}
Media dos números digitados = {average:.1f}
Maior número digitado = {more} 
Menor número digitado = {less}''')
