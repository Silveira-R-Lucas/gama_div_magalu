print('Bem vindo a calculadora de salário !')
valor_hora =  float(input('Digite o valor da sua hora de trabalho: '))
horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas neste mês: '))
salario = horas_trabalhadas*valor_hora
print('Seu salário é R$ %0.2f'  %salario)