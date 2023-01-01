ano = int(input('Digite um ano: '))
v1 = (ano%4)
v1a = (ano%400)
v2 = str(ano)
u = ano // 1 % 10
d = ano // 10 % 10
#print(v1)
#print(v2[-1])
#print(v2[-2])
#print(v1a)
#if v1 == 0:
   # print(f'O ano {ano} é bissexto')
#else:
    #print(f'O ano {ano} não é bissexto')
#if (v2[-1] and v2[-2]) == "0":
    #print('É bissexto' if v1a==0 else 'O ano não é bissexto')
#else:
    #print('É bissexto' if v1==0 else 'O ano não é bissexto')

if (u and d) == 0:
    print('É bissexto' if v1a==0 else 'O ano não é bissexto')
else:
    print('É bissexto' if v1==0 else 'O ano não é bissexto')