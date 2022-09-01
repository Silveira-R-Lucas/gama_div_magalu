print('Bem vindo a calculadora de salário !')
valor_hora =  float(input('Digite o valor da sua hora de trabalho: '))
horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas neste mês: '))
salario_bruto = horas_trabalhadas*valor_hora
ir = salario_bruto* 0.11
inss = salario_bruto* 0.08
sind = salario_bruto* 0.05
print (f"""+ Salário Bruto : R$ {salario_bruto}
- IR (11%) : R$ {ir}
- INSS (8%) : R$ {inss}
- Sindicato ( 5%) : R$ {sind}
= Salário Liquido : R$ {salario_bruto - ir - inss - sind}""")


