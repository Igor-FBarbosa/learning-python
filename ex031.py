dist = float(input('Qual a distância da viagem (km): '))
menos200 = (0.50*dist)
mais200 = (0.40*dist)
if dist>200:
    print(f'O valor da viagem é: {mais200:.2f}')
else:
    print(f'O valor da viagem é: {menos200:.2f}')