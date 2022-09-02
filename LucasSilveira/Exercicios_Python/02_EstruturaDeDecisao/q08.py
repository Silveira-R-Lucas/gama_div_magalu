print('=================================================')
print('Vamos descobrir qual é o melhor produto para comprar !')
print('=================================================')
num1 = float(input('Digite o valor do primeiro produto : '))
num2 = float(input('Digite o valor do segundo produto : '))
num3 = float(input('Digite o valor do terceiro produto : '))


print('-')
print('-'*2)
print('-'*3)
print('-'*4)
print('-'*5)
print('-'*6)
print('-'*7)


if num1 < num2 and num1 <num3:
    print('O produto mais barato é R$ %0.2f' %num1)
elif num2 < num1 and num2 < num3:
    print('O produto mais barato é R$ %0.2f' %num2)
else:
    print('O produto mais barato é R$ %0.2f' %num3)

print('=================================================')