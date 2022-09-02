import statistics
from tracemalloc import Statistic

print('=================================================')
print('Bem vindo a calculadora de nota do Colégio Python')
print('=================================================')

nota1 = float(input('Digite a primeira nota parcial do semestre: '))
nota2 = float(input('Digite a segunda nota parcial do semestre: '))

media = statistics.mean([nota1,nota2])

if media <= 4.0:
    conceito = ['E','REPROVADO']
elif media > 4.0 and media <= 6.0:
    conceito = ['D','REPROVADO']
elif media > 6.0 and media <= 7.5:
    conceito = ['C','APROVADO']
elif media > 7.5 and media <= 9.0:
    conceito = ['B','APROVADO']
elif media > 9.0 and media <= 10.0:
    conceito = ['A','APROVADO']
else:
    print('Algo deu errado, tente novamente.')
    exit()

print(f'''
    sua primeira nota foi {nota1}
    a segunda nota foi {nota2}
    a média é {media}
    conceito {conceito[0]}
    situação {conceito[1]}
    ''')
