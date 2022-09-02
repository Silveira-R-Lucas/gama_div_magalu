vogais = ['A', 'E', 'I', 'O', 'U']

letra = input(' Digite uma letra : ')

if not letra.upper().isalpha():
    print('Desculpe =( não entendi o que você disse, reinicie o programa...')
elif letra.upper().isalpha() and letra.upper() in vogais:
    print('Você digitou uma vogal !')
else:
    print('Você digitou uma consoante !')