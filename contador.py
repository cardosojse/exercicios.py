from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(2)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            cont += p
            sleep(0.5)
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            cont -= p
            sleep(0.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

print()
print('CONTAGEM PERSONALIZADA')
i = int(input('Digite o número inicial: '))
f = int(input('Digite o número final: '))
p = int(input('Digite o passo: '))
print()
contador(i, f, p)
