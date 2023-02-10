valor = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valor[-1]:
        valor.append(n)
        print('Valor adicionado no fim da lista.')
    else:
        pos = 0
        while pos < len(valor):
            if n <= valor[pos]:
                valor.insert(pos, n)
                print(f'Valor digitado na posição {pos} da lista')
                break
            pos += 1
print(valor)
