print('===============================')
print('Em que turno você estuda ????')
print('===============================')

resposta = input('Digitar M-matutino ou V-Vespertino ou N- Noturno : ').upper()

print('-')
print('-'*2)
print('-'*3)
print('-'*4)
print('-'*5)

if resposta == 'M':
    print('Bom Dia !')
elif resposta == 'V':
    print('Boa Tarde !')
elif resposta == 'N':
    print('Boa Noite !')
else:
    print('Não entendi o que você disse =( ...')