# dicionários são dados mutáveis e o seu simbolo é chaves {}

dados = dict()
dados = {'first_name':'Everton', 'last_name':'Camargo', 'age':34}
dados2 = {'first_name':'Pedro', 'last_name':'Ramos', 'age':24}

#del dados['age']

print(dados.keys())
print(dados.values())
print(dados.items())

for k in dados.keys():
    print(k)

for v in dados.values():
    print(v)

for k, v in dados.items():
    print(f'o {k} é {v}')

nomes = list()

nomes.append(dados)
nomes.append(dados2)

print(nomes)

for n in nomes:
    for k, v in n.items():
        print(f'o key é {k} e o valor é {v}')




