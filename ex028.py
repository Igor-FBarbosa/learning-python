import random
rdm = random.randint(0,5)
escolha = int(input('Adivinhe o número inteiro que eu pensei: '))
if rdm == escolha:
    print(f'ACERTOU! Você escolheu o número {escolha} e foi exatamente o que eu pensei!')
else:
    print(f'ERROU! Você escolheu o número {escolha} e eu pensei no número {rdm}')
