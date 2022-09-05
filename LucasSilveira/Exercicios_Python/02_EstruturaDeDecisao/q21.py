print('=================================================')
print('Caixa Eletrônico')
print('=================================================')

def conta_cedulas(valor):

        nota100 = valor // 100
        nota50 = (valor % 100) // 50
        nota10 = ((valor % 100) % 50) // 10
        nota1 = (((valor % 100) % 50) % 10) // 1
        print(f"Com o saque de {valor} você vai receber: ")
        print (f"{nota100} de notas de 100") if nota100 != 0 else ""
        print (f"{nota50} de notas de 50") if nota50 != 0 else ""
        print (f"{nota10} de notas de 10") if nota10 != 0 else ""
        print (f"{nota1} de notas de 1")  if nota1 != 0 else ""



saque = 0
while not (saque >= 10 and saque <= 600):
    saque = int(input('Digite o valor do saque:'))
    if saque >= 10 and saque <= 600:
        conta_cedulas(saque)        
    else:
        print('Valor Inválido ! Digite um valor entre 10 e 600')


