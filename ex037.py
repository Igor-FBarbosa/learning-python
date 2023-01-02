num = int(input('Digite qualquer número inteiro: '))
print('Escolha a forma de conversão: ')
conv = int(input('1 para binário\n2 para octal\n3 para hexadecimal\n>>> '))
if conv == 1:
    print(f'O número {num} binário é: {bin(num)}')
elif conv == 2:
    print(f'O número {num} octal é: {oct(num)}')
elif conv == 3:
    print(f'O número {num} hexadecimal é: {hex(num)}')
else:
    print('Opção inexistente!')