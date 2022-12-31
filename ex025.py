nome = str(input('Qual seu nome completo? ')).strip()
verif = 'LIMA' in nome.upper()
print(f'Seu nome tem Lima? {verif}')

nome = str(input('Qual seu nome completo? ')).strip()
print('Seu nome tem Lima? {}' .format('LIMA' in nome.upper()))