print('=================================================')
print('Inteiro ou Decimal')
print('=================================================')

num = float(input('Digite um número:'))

if num % 1 == 0:
    print("Este número é inteiro")
else:
    print("Este número é decimal")