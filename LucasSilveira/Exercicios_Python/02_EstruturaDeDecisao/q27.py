print('=================================================')
print('Hortifruti da Tia Neide')
print('=================================================')

fruta = ''
kilos = ''
preco = {}
opcoes = ['mg','mc','s']
sacola_de_compras = {}
desconto = 0
totalkgs = 0

print('Seja muito Bem Vindo !')
print('')
print('Vamos Iniciar a compra.')
print('')

while fruta != 'x':
    fruta = ''
    kilos = ''
    while fruta not in opcoes:
        fruta = input('Que fruta gostaria de levar hoje ? (MG- morango, MC- maçã, x- sair)').lower()
        if fruta == 'x':
            break
        elif fruta in opcoes:
            while type(kilos) == str:
                kilos = input('Quantos kgs ? (Digite apenas números): ')       
                if kilos.isdigit() == False:
                    print('Entrada Inválida')
                else:
                    kilos = float(kilos)
                    if fruta in sacola_de_compras:
                        sacola_de_compras[fruta] += kilos 
                    else: 
                        sacola_de_compras[fruta] = kilos
        else:
            print('Entrada Inválida')
            
    while fruta not in 'sx':
        fruta = ''
        fruta = input('Gostaria de comprar mais alguma coisa? (S- sim, X- sair)').lower()
        print('') if fruta in 'sx' else print('Entrada Inválida')


def pagamento(hash,valor):
    totalkgs = 0
    desconto = 0

    if 'mg' in hash:
        hash['Morango'] = hash['mg']
        del hash['mg']
        if hash['Morango'] < 5:
                valor['Morango'] = hash['Morango'] * 2.50
        elif hash['Morango'] >= 5:
                valor['Morango'] = hash['Morango'] * 2.20

    if 'mc' in hash:
        hash['Maca'] = hash['mc']
        del hash['mc']
        if hash['Maca'] < 5:
                valor['Maca'] = hash['Maca'] * 1.80
        elif hash['Maca'] >= 5:
                valor['Maca'] = hash['Maca'] * 1.50
    
    for x in hash:
        totalkgs += hash[x]
    
    if totalkgs > 8 or sum(valor.values()) > 25:
        desconto = sum(valor.values()) * 0.1

    precototal = sum(valor.values())

    print('''
        =================================================
        Nota Fiscal
        =================================================
        Item(s)          kgs          R$''')

    for key, value in sacola_de_compras.items():
            print('''
        {:<15} {:<15} {:<15.2f}'''.format(key, value, valor[key]))

    print(f'''
        =================================================
        Total                               R${precototal:.2f}
        Desconto                            R${desconto:.2f}
        =================================================
        Valor a pagar                       R${(precototal-desconto):.2f}
        =================================================''')



    
pagamento(sacola_de_compras,preco)


    









    



