n = 0
while n < 10:
    print('Everton Camargo')
    n = n + 1
print('Fim')

n = 'n'
while n != 's':
    n = str(input('Escreva uma letra'))
print('Fim')

# while é usado quando não sabemos o fim de um processo.


# f strings, nova atualização

nome = 'Everton Ton'
valor = 19
print(f'Meu nome é {nome}')
print(f'Foi perdido {valor:.2f}')
