import random
a1 = input('Digite o nome 1: ')
a2 = input('Digite o nome 2: ')
a3 = input('Digite o nome 3: ')
a4 = input('Digite o nome 4: ')
lista = [a1,a2,a3,a4]
print(f'O aluno escolhido foi... {random.choice(lista)}')