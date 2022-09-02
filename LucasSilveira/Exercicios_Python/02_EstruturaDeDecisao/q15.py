print('=================================================')
print('Tipos de triângulo')
print('=================================================')

lado1 = float(input('Digite o tamanho de um dos lados: '))
lado2 = float(input('Agora digite o tamanho de outro lado: '))
lado3 = float(input('Finalmente digite o tamanho do último lado: '))

if lado1 != lado2 and lado1 !=  lado3:
    print('Este triângulo é Escaleno')
elif lado1 == lado2 and lado1 == lado3:
    print('Este trinângulo é Equilátero')
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print ('Este triângulo é Isósceles')
else:
    print('Algo deu errado, tente novamente...')