veloc = int(input('Digite a velocidade do carro: '))
#limite = int(input('Digite o limite de velocidade da via: '))
multa = float(veloc-80)*7
if veloc>80:
    print(f'Você estava andando a {veloc} km/h, {veloc-80} km/h acima do limite da via!\nSerá multado em R${multa:.2f}')
else:
    print('Continue obedecendo as leis de trânsito!')