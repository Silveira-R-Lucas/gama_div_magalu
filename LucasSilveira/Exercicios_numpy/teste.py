import numpy as np

mes_31 = np.arange(1,32)
mes_30 = np.arange(1,31)
fevereiro = array = np.arange(1,29)
ano = np.hstack([mes_31, mes_30])
ano = np.tile(ano,3)
ano[32:60] = fevereiro
ano = np.delete(ano,[32,60])
ano = np.hstack([ano, mes_31])
ano = np.hstack([ano, mes_31])
ano = np.hstack([ano, mes_30])
ano = np.hstack([ano, mes_31])
ano = np.hstack([ano, mes_30])
ano = np.hstack([ano, mes_31])
dias_do_outro_ano = np.arange(1,7)
ano = np.hstack([ano, dias_do_outro_ano]).reshape([53,7])

print(ano)


