print('=================================================')
print('Calculadora')
print('=================================================')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
opcao = ''
opcoes_validas = ['x','/','+','-']

while opcao not in opcoes_validas:
    opcao = input('''
        Qual operação deseja realizar ?
        Multiplicação - marque \'x\'
        Divisão - marque \'/\' 
        Soma - marque \'+\'
        Subtração - marque \'-\'
        ''').lower()
    print('')
    if opcao == 'x':
        resultado = num1 * num2
    elif opcao == '/':
        resultado = num1 / num2
    elif opcao == '+':
        resultado = num1 + num2
    elif opcao == '-':
        resultado = num1 - num2
    else :
        print('Entrada Inválida')
    par = resultado % 2
    print(f'O resultada operação : {num1} {opcao} {num2} = {resultado}')
    print('Este número é par,') if par == 0 else print('Este número é ímpar,')
    print('Negativo') if resultado < 0 else print('Positivo')
    print('E inteiro') if resultado % 1 == 0 else print('Decimal')