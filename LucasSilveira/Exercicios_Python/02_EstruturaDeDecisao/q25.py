from re import S


print('=================================================')
print('Detetive Virtual')
print('=================================================')

resposta1 = ''
resposta2 = ''
resposta3 = ''
resposta4 = ''
resposta5 = ''

while resposta1.lower() != 's' and resposta1.lower() != 'n':
    resposta1 = input('Telefonou para a vítima? (S/n)').lower()
    print('ok') if resposta1 == 's' or resposta1 == 'n' else print('Resposta Inválida')
    print('=================================================')

while resposta2.lower() != 's' and resposta2.lower() != 'n':
    resposta2 = input('Esteve no local do crime? (S/n)').lower()
    print('ok') if resposta2 == 's' or resposta2 == 'n' else print('Resposta Inválida')
    print('=================================================')

while resposta3.lower() != 's' and resposta3.lower() != 'n':
    resposta3 = input('Mora perto da vítima? (S/n)').lower()
    print('ok') if resposta3 == 's' or resposta3 == 'n' else print('Resposta Inválida')
    print('=================================================')

while resposta4.lower() != 's' and resposta4.lower() != 'n':
    resposta4 = input('Devia para a vítima? (S/n)').lower()
    print('ok') if resposta4 == 's' or resposta4 == 'n' else print('Resposta Inválida')
    print('=================================================')

while resposta5.lower() != 's' and resposta5.lower() != 'n':
    resposta5 = input('Já trabalhou com a vítima? (S/n)').lower()
    print('ok') if resposta5 == 's' or resposta5 == 'n' else print('Resposta Inválida')
    print('=================================================')

resposta_concatenada = resposta1 + resposta2 + resposta3 + resposta4 + resposta5

julgamento = resposta_concatenada.count('s')

print('-')
print('-'*2)
print('-'*3)
print('-'*4)
print('-'*5)
print('-'*6)
print('-'*7)

if julgamento == 2:
    print('Suspeita...')
elif julgamento >= 3 and julgamento <= 4:
    print('Cúmplice !')
elif julgamento == 5:
    print('Assasino !')
else:
    print('Inocente.')
