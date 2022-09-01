import math
tamanho_do_arquivo = int(input('Qual o tamanho do arquivo em \'MB\' a baixar?: '))
velocidade_internet = int(input('Qual a velocidade da sua internet (Mbps)?: '))

tempo_de_download = (tamanho_do_arquivo/(velocidade_internet/8))/60

print(f'Você baixará o arquivo em aproximadamente {math.ceil(tempo_de_download)} minutos')