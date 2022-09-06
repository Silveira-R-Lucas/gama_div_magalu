from genericpath import isdir


print('=================================================')
print('Posto Juma Marruá')
print('=================================================')

tipo_combustivel = 'x'
litros = ''
preco = 0
desconto = 0

while tipo_combustivel != 'a' and tipo_combustivel != 'g':
    tipo_combustivel = input('Qual o tipo de combustivel que gostaria de abastecer ? (A-álcool, G-gasolina)').lower()
    print('') if tipo_combustivel == 'a' or tipo_combustivel == 'g' else print('Entrada Inválida')


while type(litros) == str:
    litros = input('Quantos litros gostaria de abastecer ? (Digite apenas números): ')       
    if litros.isdigit() != True:
        print('Entrada Inválida')
    else:
        litros = float(litros)

if tipo_combustivel == 'a' and litros < 20:
    preco = litros * 1.90
    desconto = 0.03
elif tipo_combustivel == 'a' and litros > 20:
    preco = litros * 1.90
    desconto = 0.05
elif tipo_combustivel == 'g' and litros < 20:
    preco = litros * 2.50
    desconto = 0.04
elif tipo_combustivel == 'g' and litros > 20:
    preco = litros * 2.50
    desconto = 0.06

print(f'''
Valor a ser pago................R$ {preco:.2f}
Desconto({desconto*100}%).................R$ {(preco * desconto):.2f}
Total...........................R$ {(preco - (preco*desconto)):.2f}
''')





