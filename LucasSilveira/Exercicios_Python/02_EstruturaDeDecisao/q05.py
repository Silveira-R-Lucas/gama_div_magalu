nota1 = int(input('Digite a nota da primeira prova : '))
nota2 = int(input('Digite a nota da segunda prova : '))

media = (nota1 + nota2) / 2

if media == 10:
    print ('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')
