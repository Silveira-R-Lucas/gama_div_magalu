print('''
=============
   Tabuada
=============
''')

numero = int(input('Número: '))
while numero < 0 or numero > 10:
    print('Número inválido, digite um valor entre 0 e 10')
    numero = int(input('Numero: '))

print('Calculando a tabuada...')
'''
fator = 0 #contador
while fator <= 10:
    print(f'{fator} X {numero} = {numero*fator}')
    fator = fator + 1
    #fator +=1
'''

for fator in 0,1,2,3,4,5,6,7,8,9,10:
    print(f'{fator} X {numero} = {numero*fator}')
                                                                                          
print('Fim do programa!')