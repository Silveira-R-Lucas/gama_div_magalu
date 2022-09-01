import math
print('Vamos calcular quantas latas precisa para sua pintura.')
print('Vendemos apenas latas de 18lts e cada lata pinta aproximadamente 54m²')
m2 = int(input('Quantos metros ² tem a  área ? : '))

equipara_metro_por_litro = m2 / 3 
## cada litro pinta 3 m²
quantidade_de_latas = equipara_metro_por_litro/18



print(f'Você precisa de {math.ceil(quantidade_de_latas)} latas de 18 litros')
print('Preço total: R$', math.ceil(quantidade_de_latas)*80)

