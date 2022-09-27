from statistics import mean
import pandas as pd
import numpy as np


alunos_infos = pd.read_csv('Exercicio_estatistica - Sheet1.csv')
alunos_infos['Altura']= alunos_infos['Altura'].str.replace(',', '.')
alunos_infos['Altura']= pd.to_numeric(alunos_infos['Altura'],errors = 'coerce')
colunas_numéricas = alunos_infos.select_dtypes(include='number')
colunas_texto = alunos_infos.select_dtypes(exclude='number')
colunas_texto['Formação'] = colunas_texto['Formação'].str.upper()
colunas_texto['Estado'] = colunas_texto['Estado'].str.upper()

nomes = colunas_texto['Nome'].str.upper().str.strip().str.split(' ', expand=True)
colunas_texto['Nome'] = nomes[0]

def tipo_moda(serie):
    qtd = serie.mode().shape[0]
    if qtd == 0:
            return 'Sem Moda'
    elif qtd == 1:
            return 'Unimodal'
    elif qtd == 2:
            return 'Bimodal'
    elif qtd > 2:
            return 'Multimodal'



print(f'''

A moda das colunas numéricas é :

{colunas_numéricas.mode()}


A mediana é :

{colunas_numéricas.median()}


A média é : 

{colunas_numéricas.mean()}


Os Quartis são:

{colunas_numéricas.quantile([.25,.5,.75])}


Os 10% maiores números são:

{colunas_numéricas.nlargest(4, ['Idade', 'Filhos', 'Altura'])}


Os 5% menores são:

{colunas_numéricas.nsmallest(2, ['Idade', 'Filhos', 'Altura'])}


O valor máximo é:

{colunas_numéricas.max()}


O valor mínimo é:

{colunas_numéricas.min()}


''')

for coluna in colunas_texto:
    print(f'''
A frequência absoluta dos {coluna} é:

{colunas_texto[coluna].value_counts()}


A frequência relativa dos {coluna} é:     % ( por cento )

{colunas_texto[coluna].value_counts()/len(colunas_texto)*100}


A moda de {coluna} é:

{colunas_texto[coluna].mode()}


o tipo de moda é:

{tipo_moda(colunas_texto[coluna])}


O valor máximo é:

{colunas_texto[coluna].sort_values().head(1)}

O valor mínimo é:

{colunas_texto[coluna].sort_values().tail(1)}
    ''')

print(colunas_texto.isnull().sum())