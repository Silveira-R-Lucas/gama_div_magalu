print('=================================================')
print('Posto Juma Marruá')
print('=================================================')

tipo_combustivel = 'x'
litros = 0

while tipo_combustivel != 'a' and tipo_combustivel != 'g':
    tipo_combustivel = input('Qual o tipo de combustivel que gostaria de abastecer ? (A-álcool, G-gasolina)').lower()
    print('') if tipo_combustivel == 'a' or tipo_combustivel == 'g' else print('Entrada Inválida')


while litros == 0:
    litros = float(input('Quantos litros gostaria de abastecer ? : '))
     


