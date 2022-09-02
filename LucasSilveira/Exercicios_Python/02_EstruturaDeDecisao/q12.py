print('''

===============================
Organizações Tabajara
===============================

vamos calcular o seu salário. ''')

valor_hora = float(input('Digite o valor da sua hora de trabalho: '))
horas_mes = float(input('Digite a quantidade de horas trabalhadas neste mês: '))




def salario(valor_hr,quantidade_hr):
    bruto = valor_hr * quantidade_hr

    if bruto <= 900:
            ir = 0
    elif bruto > 900 and bruto <= 1500:
            ir = 0.05
    elif bruto > 1500 and bruto <= 2500:
            ir = 0.10
    else:
            ir = 0.2

    sindicato = 0.03
    fgts = 0.11
    inss = 0.1
    descontos = bruto*ir + bruto*inss + bruto*sindicato
    liquido = bruto - descontos
    print(f'''
        ===========================================================
        Salário Bruto                   
                                            R$ {bruto:0.2f}
        ___________________________________________________________
        
        (-) IR ({ir*100}%)              
                                            R$ {bruto*ir:0.2f}  
        ___________________________________________________________
        
        (-) INSS ({inss*100}%)          
                                            R$ {bruto*inss:0.2f}
        ___________________________________________________________
        
        (-) Sindicato ({sindicato*100}%)
                                            R$ {bruto*sindicato:0.2f}
        ___________________________________________________________
        
        FGTS ({fgts*100}%)              
                                            R$ {bruto*fgts:0.2f}
        ___________________________________________________________
        
        Total de descontos              
                                            R$ {descontos:0.2f}
        ___________________________________________________________
        
        Salário Liquido                 
                                            R$ {liquido:0.2f}
        ___________________________________________________________
        ===========================================================
        ''')

salario(valor_hora,horas_mes)


