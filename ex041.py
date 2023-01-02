from datetime import date
atual = date.today().year
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
ano = int(input('Digite o ano de nascimento: '))
idade = atual - ano
if idade <= 9:
    print('CATEGORIA MIRIM')
elif idade > 9 and idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade >14 and idade <= 19:
    print('CATEGORIA JUNIOR')
elif idade > 19 and idade <=20:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER!')
