print('Bem vindo ao programa de Empréstimo Bancário do Igor')
print('*=*' * 25)
valor = float(input('Digite o valor da casa R$: '))
sal = float(input('Digite seu salário R$: '))
anos = int(input('Digite em quantos anos você vai pagar: '))
prest = valor / 12 / anos
if prest > (sal * 0.30):
    status = 'REPROVADO'
else:
    status = 'APROVADO'

print(f'A sua prestação mensal será de {prest:.2f} e seu empréstimo foi {status}!')