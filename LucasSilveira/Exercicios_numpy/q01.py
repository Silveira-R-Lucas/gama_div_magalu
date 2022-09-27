import numpy as np

# primeiro exercicio 

primeiro_array = np.zeros([6,6])

print(primeiro_array)

#segundo exercicio

segundo_array = np.full([4,4],4)

primeiro_array[1:5, -5:-1] = segundo_array

print(primeiro_array)

#terceiro exercicio

terceiro_array = np.full([2,2],2)

primeiro_array[2:4, -4:-2] = terceiro_array

print(primeiro_array)

#quarto exercicio

quarto_array = np.random.randint(0,2,[6,6])

print(quarto_array)

primeiro_array -= quarto_array

print(primeiro_array)
