print('=================================================')
print('Vou descobrir qual é o maior número que digitar !')
print('=================================================')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))


print('-')
print('-'*2)
print('-'*3)
print('-'*4)
print('-'*5)
print('-'*6)
print('-'*7)

if num1 > num2 and num1 >num3:
    print('O maior número é:', num1)
elif num2 > num1 and num2 > num3:
    print('O maior número é:', num2)
else:
    print('O maior número é:', num3)

print('=================================================')