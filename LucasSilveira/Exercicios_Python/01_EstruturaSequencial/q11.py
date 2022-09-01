print('Bem vindo a calculadora de números inteiros e reais !')
int1 =  int(input('Digite o primeiro número inteiro (positivo ou negativo): '))
int2 =  int(input('Digite o segundo número inteiro: '))
real1 = float(input('Digite um número real (use ponto no lugar da vírgula): '))


produto1 = int1 * (int2/2)
soma_produto1 = (int1 * 3) + real1
cubo = real1**3

print("o produto do dobro do primeiro com metade do segundo é =", produto1)
print("a soma do triplo do primeiro com o terceiro é =", soma_produto1)
print("o terceiro elevado ao cubo é =", cubo)