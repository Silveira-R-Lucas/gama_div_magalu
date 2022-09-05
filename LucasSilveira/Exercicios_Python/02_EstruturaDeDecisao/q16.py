print('=================================================')
print('Cálculo de raízes quadradas de segundo grau')
print('=================================================')

a = float(input('Digite o valor da váriavel a: '))
b = float(input('Digite o valor da váriavel b: '))
c = float(input('Digite o valor da váriavel c: '))

delta = b**2 - 4*a*c

if a == 0:
    print('Com o valor de A igual a zero não obtemos uma equação de segundo grau.')
    print('Encerrando programa...')
elif delta < 0:
    print('A equação não possui raizes reais.')
    print('Encerrando programa...')
elif delta == 0:
    resultado = (-b + delta**0.5)/2*a
    print(f'O resultado é {resultado}.')
elif delta > 0:
    resultado = (-b + delta**0.5)/2*a
    resultado2 = (-b - delta**0.5)/2*a
    print(f'Os resultados são {resultado},{resultado2}.')
else:
    print('Algo deu errado, tente novamente...')
 
