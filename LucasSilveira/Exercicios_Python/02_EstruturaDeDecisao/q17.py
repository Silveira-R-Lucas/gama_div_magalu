from calendar import isleap
print('=================================================')
print('Consulta de anos bissextos')
print('=================================================')


ano = int(input('Digite o ano que gostaria de pesquisar: '))

if isleap(ano):
    print('É bissexto')
else:
    print('Não é bissexto')
