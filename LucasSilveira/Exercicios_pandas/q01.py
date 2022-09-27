import pandas as pd
import numpy as np
import csv

estados_brasileiros = [
'São Paulo',
'Paraná',
'Santa Catarina',
'Rio Grande do Sul',
'Mato Grosso do Sul',
'Rondônia',
'Acre',
'Amazonas',
'Roraima',
'Pará',
'Amapá',
'Tocantins',
'Maranhão',
'Rio Grande do Norte',
'Paraíba',
'Pernambuco',
'Alagoas',
'Sergipe',
'Bahia',
'Minas Gerais',
'Rio de Janeiro',
'Mato Grosso',
'Goiás',
'Distrito Federal',
'Piauí',
'Ceará',
'Espírito Santo']



idade = np.random.randint(0,101,size=(1000,))
nota = np.random.uniform(low=0.0, high=1001.0, size=(1000,))
sexo = np.random.choice(["Masculino", "Feminino"], size=(1000,))
estado = np.random.choice(estados_brasileiros, size=(1000,))


dados_alunos_enem = pd.DataFrame({
    'idade': idade,
    'nota': nota,
    'sexo': sexo,
    'estado': estado
})

dados_alunos_enem['nota'] = dados_alunos_enem['nota'].sample(frac= 0.8)
dados_alunos_enem['nota'] = dados_alunos_enem['nota'].fillna(0)

maiores_dezoito = (dados_alunos_enem['idade'] > 18)
aprovados = dados_alunos_enem[maiores_dezoito]

aprovados.loc[aprovados['nota'] > 600, 'situacao'] = 'Aprovado'

aprovados['situacao'] = aprovados['situacao'].fillna('Reprovado')

print(aprovados['situacao'].value_counts())




