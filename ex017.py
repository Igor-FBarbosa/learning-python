import math
opo = float(input('Qual o comprimento do cateto oposto? '))
adj = float(input('Qual o comprimento do cateto adjacente? '))
hip = (opo**2 + adj**2)**(1/2)
# hi=hypot (opo,adj)
print(f'O valor da hipotenusa é {hip}')