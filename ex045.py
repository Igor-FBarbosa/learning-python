import random
player = int(input('Escolha [1] para Pedra\nEscolha [2] para papel\nEscolha [3] para tesoura\n'))
comp = random.randint(1,3)
if player <=3:
    print ('JO\nKEN\nPO!')
    if player == 1:
        print('Você escolheu PEDRA!')
    elif player == 2:
        print('Você escolheu PAPEL!')
    elif player == 3:
        print('Você escolheu TESOURA!')

    if comp == 1:
        print('O PC escolheu PEDRA!')
    elif comp == 2:
        print('O PC escolheu PAPEL!')
    elif comp == 3:
        print('O PC escolheu TESOURA!')

    if player == 1 and comp == 1:
        print('EMPATE!')
    elif player == 2 and comp == 1:
        print('PARABÉNS VOCÊ GANHOU!')
    elif player == 3 and comp == 1:
        print('QUE PENA! VOCÊ PERDEU!')
    elif player == 2 and comp == 2:
        print('EMPATE!')
    elif player == 3 and comp == 3:
        print('EMPATE!')
    elif player == 2 and comp == 3:
        print('QUE PENA! VOCÊ PERDEU!')
    elif player == 1 and comp == 2:
        print('QUE PENA VOCÊ PERDEU!')
    elif player == 1 and comp == 3:
        print('PARABÉNS VOCÊ GANHOU!')
    elif player == 3 and comp == 2:
        print('PARABÉNS VOCÊ GANHOU!')
else:
    print('Digite uma opção válida (1 a 3)')