pais_a = (input('Digite a população total do primeiro país: '))
tx_a = (input('Digite a taxa de crescimento do primeiro país: '))
pais_b = (input('Digite a população total do segundo país: '))
tx_b = (input('Digite a taxa de crescimento do segundo país: '))

ano = 0 
while not (pais_a >= pais_b):
    pais_a = round(pais_a * tx_a + pais_a)
    pais_b = round(pais_b * tx_b + pais_b)
    ano = ano + 1

print(f'''
A população do País A de {pais_a} habitantes
ultrapassou o País B de {pais_b} habitantes
após {ano} anos.
''')