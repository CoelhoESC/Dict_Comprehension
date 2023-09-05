"""
Compreensão de dict
Similiar a Lista comprehension
"""
Lista = [('chave', 'valor'), ('chave2', 'valor2')]
# d1 = dict(Lista)
d1 = {x: y for x, y in Lista}
print(d1)

# Funções de str
d2 = {x.upper(): y.lower() for x, y in Lista}
print(d2)

# Posso usar operadores aritmeticas
d3 = {x: y * 2 for x, y in Lista}  # --> Duplicando
print(d3)

# Usando dict comprehension para fazer um set (set comprehension)
d4 = {x for x in range(5)}
print(d4, type(d4))

# Posso fazer um dict com range, tendo F' string
d5 = {f'Chave_{x}': y ** 2 for x, y in enumerate(range(5))}  # --> com enumerate
print(d5)

d6 = {f'Chave_{x}': x ** 2 for x in range(5)}
print(d6)

d7 = {f'Chave_{x}': x ** 2 for x in range(10) if x % 2 == 0}  # --> todas os valores divisivel por 2
print(d7)
