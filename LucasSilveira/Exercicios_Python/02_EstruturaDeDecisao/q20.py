from statistics import mean


nota1 = int(input('Digite a nota da primeira prova : '))
nota2 = int(input('Digite a nota da segunda prova : '))
nota3 = int(input('Digite a nota da terceira prova : '))

media = mean([nota1,nota2,nota3])

if nota1 >10 or nota2 > 10 or nota3 > 10 or nota1 < 0 or nota2 < 0 or nota3 < 0:
    print('entrada inválida.')
    exit()

if media == 10:
    print ('Aprovado com Distinção')
    print(f'Sua média foi {media}')
elif media >= 7:
    print('Aprovado')
    print(f'Sua média foi {media}')
else:
    print('Reprovado')
    print(f'Sua média foi {media}')
