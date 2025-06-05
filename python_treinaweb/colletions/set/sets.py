#sets são  coleções de elementos únicos e não ordenados, ou seja, não permitem duplicatas e não mantêm a ordem dos elementos.
# Eles são úteis quando você precisa garantir que não haja elementos duplicados em uma coleção.
# Sets são mutáveis, o que significa que você pode adicionar ou remover elementos após a criação do set.

# Exemplo de criação de um set
meu_set = {'Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'Python'}
print(meu_set)  # Exibe o set
# Exemplo Dicionario para não confundir com set
#meu_dicionario = {'Python': 'Linguagem de programação', 'Java': 'Linguagem de programação', 'C++': 'Linguagem de programação'}
# o set é um dicionario sem chaves, ou seja, não tem ordem
print(type(meu_set))  # Exibe o tipo do set

#outro explo de criação de um set
outro_set = set(['Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'Python'])
print(outro_set)  # Exibe o outro set
# Verifica se o set é igual ao outro set
print(meu_set == outro_set)  # Exibe True, pois os sets são iguais  
print(type(outro_set))  # Exibe o tipo do outro set


meu_set.add('C#')  # Adiciona um novo elemento ao set
print(meu_set)  # Exibe o set após adicionar o novo elemento

meu_set.remove('C++')  # Remove um elemento do set
print(meu_set)  # Exibe o set após remover o elemento

meu_set.update({'PHP', 'Go'})  # Adiciona múltiplos elementos ao set
print(meu_set)  # Exibe o set após adicionar múltiplos elementos

meu_set.discard('JavaScript')  # Remove um elemento do set, mas não gera erro se o elemento não existir
print(meu_set)  # Exibe o set após descartar o elemento


print(meu_set | outro_set)  # União dos dois sets, exibe todos os elementos únicos de ambos
print(meu_set & outro_set)  # Interseção dos dois sets, exibe os elementos comuns a ambos
print(meu_set - outro_set)  # Diferença dos dois sets, exibe os elementos que estão em meu_set, mas não em outro_set





