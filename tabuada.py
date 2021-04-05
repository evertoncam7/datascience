# Faça um programa onde o usuário digita o número e o programa retorna a tabuada inteira.

numero = int(input('Digite a tabuada?'))
for i in range(1, 11):
    print('{} x {:2} = {:2}'.format(numero, i, numero*i))

print('-' * 20)

# Agora faça um programa que mostra todas as tabuadas de 1 a 10

for ii in range(1, 11):
    for iii in range(1, 11):
        print('{} x {:2} = {:2}'.format(ii, iii, ii*iii));
    print('=' * 20)

