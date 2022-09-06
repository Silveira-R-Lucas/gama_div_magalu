pais_a = 8e4
tx_a = 0.03
pais_b = 2e5
tx_b = 0.015

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