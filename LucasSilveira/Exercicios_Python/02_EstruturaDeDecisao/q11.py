print('''

===============================
Organizações Tabajara
===============================

Recebemos ajuste nos salários.''')

salario_anterior = float(input('Para Descobrir o salário com aumento, digite o valor do seu salário (substitua a vírgula pelo ponto): '))

def reajuste(salario):
    if salario <= 280:
            percentual = 0.2
    elif salario > 280 and salario < 700:
            percentual = 0.15
    elif salario > 700 and salario < 1500:
            percentual = 0.10
    else:
            percentual = 0.05
        
    salario_depois = salario * (percentual +1)
    aumento =  salario_depois - salario 

    print(f'''
        Seu salário antes do reajuste R$ {salario:0.2f}
        Percentual de aumento aplicado {percentual*100:0.0f} %
        Valor do aumento R$ {aumento:0.2f}
        Novo salário, após aumento R$ {salario_depois:0.2f}''')

reajuste(salario_anterior)


