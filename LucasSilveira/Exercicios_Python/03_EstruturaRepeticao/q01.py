nota = int(input('Nota: '))
if nota >= 0 and nota <= 10:
    print('valor válido')
else:
    while not(nota >= 0 and nota <= 10):
        print('valor inválido')
        nota = int(input('Nota: '))
        print('valor válido')