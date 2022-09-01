input('Bem vindo à calculadora de peso ideal')
genero = input('Qual é o seu gênero? (h/m): ')
altura = float(input('Qual é a sua altura em metros? (substitua a vírgula pelo ponto): '))

if genero == 'h':
    print(f'Seu peso idel é {round((72.7* altura) - 58)} kgs')
elif genero == 'm':
    print(f'Seu peso idel é {round((62.1*altura) - 44.7)} kgs')
else :
    print('Não entendi o que você disse =( \n reinicie o programa')