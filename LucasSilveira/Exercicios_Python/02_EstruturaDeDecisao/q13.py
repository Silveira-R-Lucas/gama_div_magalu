print('=================================================')
print('Bem vindo')
print('=================================================')

dia_da_semana = ['domingo','segunda','terça','quarta','quinta','sexta','sábado']

num = int(input('Digite um nṹmero entre 1 e 7: '))

if num >= 1 and num <= 7:
    print ('O dia da semana correspondente é', dia_da_semana[num-1])
else:
    print('Valor inválido.')