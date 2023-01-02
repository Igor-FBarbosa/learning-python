import datetime
ano = int(input('Qual o ano do seu nascimento? '))
anoatual = datetime.date.today().year
if anoatual-ano < 18:
    print(f'Você ainda não precisa se alistar ao serviço militar! Ainda faltam {18-(anoatual-ano)} anos!')
elif anoatual-ano > 18:
    print(f'Você já passou do tempo do alistamento. Tens {(anoatual-ano)-18} anos em atraso!')
else:
    print('Está na hora de se alistar!')