ano=int(input('seu ano'))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('seu ano é bissexto')
else:
    print('não é bissexto')