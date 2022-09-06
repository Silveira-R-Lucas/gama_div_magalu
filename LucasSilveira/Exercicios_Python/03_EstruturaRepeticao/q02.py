nome = input('Usuário: ')
senha = input('Senha: ')
while senha == nome:
    print('A senha não pode ser igual ao nome do usuário!')
    senha = input('Senha: ')

print('Informações foram cadastradas com sucesso!')