print('=================================================')
print('''Promoção Açougues Tabajara ! 
                    Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

(Apenas 1 tipo de carne por cliente, quantidade ilimitada)
''')
print('=================================================')

item = ''
kilos = '' 
opcoes = ['F', 'A', 'P']
opcoes_pagamento = ['C', 'D', 'P']
desconto = 0
forma_de_pagamento = ''
total = 0
sacola_de_compras = {}

while item not in opcoes:
    item = input('Qual peça gostaria de levar hoje ? (F- filé duplo, A- Alcatra, P- picanha, X- Sair)').upper()

    if item == 'X':
        break
    elif item in opcoes:
        while type(kilos) == str:
            kilos = input('Quantos kgs ? (Digite apenas números): ')       
            if kilos.isdigit() == False:
                print('Entrada Inválida')
            else:
                kilos = float(kilos)
    else:
            print('Entrada Inválida')

if item == 'F' :
    item = 'File Duplo'
    if kilos < 5:
        total = kilos * 4.90
    elif kilos >= 5:
        total = kilos * 5.80
if item == 'P' :
    item = 'Picanha'
    if kilos < 5:
        total = kilos * 6.90
    elif kilos >= 5:
        total = kilos * 7.80
if item == 'A' :
    item = 'Alcatra'
    if kilos < 5:
        total = kilos * 5.90
    elif kilos >= 5:
        total = kilos * 6.80
     
sacola_de_compras[item] = kilos

while forma_de_pagamento not in opcoes_pagamento:
    forma_de_pagamento = input('Qual a forma de pagamento? (C- cartão, D- dinheiro, P- pix)').upper()
    if forma_de_pagamento in opcoes_pagamento:
        if forma_de_pagamento == 'C':
            desconto = 0.05
    else:
        print('Entrada Inválida')

if forma_de_pagamento == 'C':
    forma_de_pagamento = 'Cartão'
elif forma_de_pagamento == 'D':
    forma_de_pagamento = 'Dinheiro' 
elif forma_de_pagamento == 'P':
    forma_de_pagamento = 'Pix' 


print(f'''
        =================================================
        Nota Fiscal
        =================================================
        Item                  kgs                  R$
        {item}             {kilos:.2f}             {total:.2f}
        =================================================
        Descontos                             {(total*desconto):.2f}
        Tipo de pagamento                     {forma_de_pagamento}
        =================================================
        TOTAL                                 R${total-(total*desconto):.2f}''')

    

