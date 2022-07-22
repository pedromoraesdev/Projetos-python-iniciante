from random import randint
jogadas = 0
computador = randint(0, 10)
jogador = int(input('Estou pensando em um número de 0 a 10, tente adivinhar!: '))
while jogador != computador:
    jogadas += 1
    if jogador < computador:
        jogador = int(input('Mais, continue tentando: '))
    elif jogador > computador:
        jogador = int(input('Menos, tente outra vez: '))
print('Parabéns! Você acertou com {} tentativas'.format(jogadas + 1))