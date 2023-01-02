s1 = int(input('Digite o primeiro lado: '))
s2 = int(input('Digite o segundo lado: '))
s3 = int(input('Digite o terceiro lado: '))
if s1 < s2 + s3 and s2 < s2 + s1 and s3 < s1 + s2:
    print('Pode ser formado um triângulo!')
    if (s1 == s2) and (s2 == s3):
        print('Este triângulo é equilátero!')
    elif (s1 == s2) or (s2 == s3) or (s1 == s3):
        print('Este triângulo é Isósceles!')
    else:
        print('Este triângulo é Escaleno!')
else:
    print('Não pode ser formado um triângulo!')