# tuplas são imutáveis, ou seja, não podem ser alteradas após a criação
# tuplas são mais rápidas que listas, pois não precisam de memória extra para armazenar informações adicionais

minha_tupla = ('Python', 'Java', 'C++', 'JavaScript', 'Ruby','Python' )
print(minha_tupla)
print(type(minha_tupla))

#metodo count
print(minha_tupla.count('Python'))  # Conta quantas vezes 'Python' aparece na tupla

#metodo index
print(minha_tupla.index('Java'))  # Retorna o índice da primeira ocorrência de 'Java'

#metodo len
print(len(minha_tupla))  # Retorna o número de elementos na tupla

# eu posso cotatenar tuplas, mas não posso alterar os valores
tupla2 = ('C#', 'PHP')

print(minha_tupla + tupla2)  # Concatena duas tuplas