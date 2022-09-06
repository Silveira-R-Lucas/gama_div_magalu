nome = input('Nome: ')
while not (len(nome) > 3): 
    print('Nome inválido! O nome deve conter mais de 3 caracteres.')
    nome = input('Nome: ')

print('Nome válido!')

idade = int(input('Idade: '))
while idade < 0 or idade > 150: 
    print('Idade inválida! A idade deve estar entre 0 e 150.')
    idade = int(input('Idade: '))

print('Idade válida!')

salario = float(input('Salário: '))
while salario <= 0:
    print('Salário inválido! O salário tem que ser maior que 0.')
    salario = float(input('Salário: '))
print('Salário válido!')

genero = input('Sexo (f ou m): ').lower()
while genero != 'f' and genero != 'm':
    print("Gênero inválido! letras permitidas 'f', 'm'")
    genero = input('Sexo (f ou m): ')
print('Gênero válido!')

estado = input('Estado civil (s, c, v, ou d): ').lower()
while estado not in 'scvd':
    print("Estado Civil inválido! letras permitidas 's', 'c', 'v', 'd'")
    estado = input('Estado civil (s, c, v, ou d): ')
print('Estado Civil válido!')