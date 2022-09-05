from curses.ascii import isdigit


print('=================================================')
print('Sintaxe matemática')
print('=================================================')

num= input('Digite um número inteiro maior que 0 e menor que 1000: ')

if num.isdigit() == False:
    print("Digite apenas números, inicie o programa novamente")
    exit()

def matematica_escrita(numero):
    if len(num) == 3:
        print(f'Temos {numero[0]} centenas, {numero[1]} dezenas e {numero[2]} unidades !')
    elif len(num) == 2:
        print(f'Temos {numero[0]} dezenas e {numero[1]} unidades !')
    elif len(num) ==1:
        print(f'Temos {numero[0]} unidades !')


if int(num) < 1000 and int(num) > 0:
    matematica_escrita(num)
else:
    print('Algo deu errado, tente novamente ...')


