import numpy as np

array = np.arange(81).reshape([9,9])
filtro_impar = array[array % 2 != 0]
filtro_par = array[array % 2 == 0]
filtro_multi_sete = array[array % 7 == 0]
filtro_multi_dez = array[array % 10 == 0]
linhas = [3,3,4,4]
colunas = [5,6,6,7]
filtro_num_select = array[linhas,colunas]
print(array)
print(filtro_impar)
print(filtro_par)
print(filtro_multi_sete)
print(filtro_multi_dez)
print(filtro_num_select)