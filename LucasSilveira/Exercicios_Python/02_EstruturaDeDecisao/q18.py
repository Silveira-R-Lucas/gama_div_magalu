from datetime import datetime
print('=================================================')
data = input('Digite a data que gostaria de pesquisar coloque a data no formato (dd/mm/aaaa): ')
print('=================================================')

def data_valida(período):
    try:
        datetime.strptime(período, "%d/%m/%Y")
        print('Data Válida')
    except ValueError:
        print('Data Inválida')

data_valida(data)

    
        