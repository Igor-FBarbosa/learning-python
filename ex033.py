import math
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
menor = n1
maior = n3
if n2 < n1:
    menor = n2
if n3 < n2:
    menor = n3
if n2 > n3:
    maior = n2
if n1 > n2:
    maior = n1
print(f'O menor número é: {menor} e o maior é: {maior}')
