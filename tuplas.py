num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {num[n]}.')
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
        if resp == 'N':
            break
    else:
        print('Tente novamente.', end=' ')
print('Obrigado')

# O código escrito abaixo foi o meu "rascunho" do código atual:
# n = ' '
# while n not in range(0, 21):
#     n = int(input('Digite um número entre 0 e 20: '))
#     if n not in range(0, 21):
#         print('Tente novamente.', end=' ')
# print(f'Você digitou o número {num[n]}.')
