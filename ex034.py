sal = float(input('Qual o salário do funcionário? '))
if sal > 1250:
    print(f'O salário com aumento é R$ {sal*1.1:.2f}')
else:
    print(f'O salário com aumento é R$ {sal*1.15:.2f}')