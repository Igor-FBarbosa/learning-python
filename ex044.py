valor = float(input('Digite o valor do produto: '))

print('*-' * 20)
print('Escolha a opção de pagamento:')
cond = int(input('1 - À vista (dinheiro ou cheque)\n2 - À vista (cartão)\n3- 2x no cartão\n4- 3x ou mais no cartão\n>>>> '))
print('*-' * 20)
if cond == 1:
    print(f'O valor final à vista é de R${valor*0.9:.2f}')
elif cond == 2:
    print(f'O valor final 1x no cartão é de R${valor*0.95:.2f}')
elif cond == 3:
    print(f'O valor final em 2x no cartão é de R${valor:.2f}')
elif cond == 4:
    print(f'O valor final em 3x ou mais no cartão é de R${valor*1.2:.2f}')
else:
    print('Digite uma opção válida')
