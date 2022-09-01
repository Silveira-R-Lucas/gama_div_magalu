import math
print('=========================================================')
print('Vamos calcular quantas latas precisa para sua pintura.')
m2 = float(input('Quantos metros ² tem a  área ? : '))

equipara_metro_por_litro = (m2 / 6) * 1.1
quantidade_de_latas = math.ceil(equipara_metro_por_litro/18)
quantidade_de_galoes = math.ceil(equipara_metro_por_litro/3.6)
valor_lata = quantidade_de_latas * 80
valor_galao = quantidade_de_galoes * 25


melhor_compra_latas = equipara_metro_por_litro//18
melhor_compra_galoes = math.ceil((equipara_metro_por_litro%18)/3.6)
preco_melhor_compra = (math.ceil(melhor_compra_latas)*80)+(math.ceil(melhor_compra_galoes)*25)




print('\n')
print(f"""Comprando apenas latas de 18 litros
você vai precisar de {quantidade_de_latas} unidades
Preço total: R$ {valor_lata:0.2f}""")
print('')
print(f"""Comprando apenas galões de 3,6 litros
você vai precisar de {quantidade_de_galoes} unidades
Preço total: R$ {valor_galao:0.2f}""")
print('\n')

print('A melhor forma de compra é:')

if m2 <= 21.6:
    print('Apenas 1 galão de 3.6 litros, preço total: R$ 25.00')
elif preco_melhor_compra > valor_lata:
    print(f'{quantidade_de_latas} latas de 18lts, preço total: R$ {valor_lata}')
else:
    print(f""" Você vai precisar de:
    {math.ceil(melhor_compra_latas)} latas de 18lts,
    {math.ceil(melhor_compra_galoes)} galões de 3,6lts
    Preço total: R$ {preco_melhor_compra:.2f}""")
print('=========================================================')
