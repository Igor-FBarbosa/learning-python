s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos de reta escolhidos podem formar um triângulo')
else:
    print('Esses segmentos de reta não são capazes de formar um triângulo!')
