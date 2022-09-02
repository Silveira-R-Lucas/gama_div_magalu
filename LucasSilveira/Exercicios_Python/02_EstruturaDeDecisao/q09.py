print('=================================================')
print('Este programa irá organizar os números para você !')
print('=================================================')

array1 = input('Digite os números a ser organizados separando-os por vírgula :').split(',')
array_convertido_e_organizado = []

for x in (array1):
  array_convertido_e_organizado.append(int(x))
  array_convertido_e_organizado.sort()


print(array_convertido_e_organizado)