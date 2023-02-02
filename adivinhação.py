from random import randint
pc = randint(0, 10)
sP = 0  # sP é a soma dos palpites.

print("""
Olá! Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?""")

palpite = int(input('Qual o seu palpite? '))
while palpite != pc:
    if palpite > pc:
        print('Menos... Tente mais uma vez.')
        palpite = int(input('Qual o seu palpite? '))
        sP += 1
    elif palpite < pc:
        print('Mais... Tente mais uma vez.')
        palpite = int(input('Qual o seu palpite? '))
        sP += 1
print(f'Parabéns! Você precisou de {sP} palpites para acertar.')
