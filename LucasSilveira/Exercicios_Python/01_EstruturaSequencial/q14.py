print('Olá Pescador! Vamos calcular o peso excedido e o valor da multa...')
peso = float(input('Quantos quilos pescou hoje ? :'))
excesso = peso -50 
multa = excesso *4

if excesso > 0:
    print(f'O peso excedido foi {excesso:.3f}kgs e a multa é de R$ {multa:.2f}')
else :
    print('A pesagem está dentro dos regulamentos, tenha um bom dia ! =)')