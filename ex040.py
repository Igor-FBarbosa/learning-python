n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
if (n1+n2)/2 < 5:
    print('REPROVADO!')
elif (n1+n2)/2 == 5 or (n1+n2)/2 <= 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')