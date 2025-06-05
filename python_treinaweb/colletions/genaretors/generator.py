def eleva_2(max=0):
    """Gera potências de 2 até o valor máximo especificado."""
    atual = 0

    while atual < max:# Verifica se o valor atual é menor que o valor máximo
        resultado = 2 ** atual
        atual += 1
        yield resultado

print(eleva_2(10))  # Exibe o objeto gerador

for i in eleva_2(10):
    print(i)  # Imprime os valores gerados, que são potências de 2 de 0 a 9


# com o genarator, não é necessário criar uma classe com métodos especiais como __iter__ e __next__
# O gerador é uma função que utiliza a palavra-chave yield para produzir valores sob demanda.
# assim só precisando fazer a logica de geração de valores, sem a necessidade de criar uma classe inteira.
# Isso torna o código mais simples e legível, além de economizar memória, pois os valores são gerados conforme necessário.