lista_simples_inteiros = [1, 7, 3, 9, 10, 5, 3 , 4] # Lista simples de inteiros
lista_simples_inteiros.append(6)  # Adiciona o elemento 6 ao final da lista

lista_simples_string = ["a", "b", "c", "d", "e"]   # Lista de strings
lista_simples_string.append("f")  # Adiciona o elemento "f" ao final da lista

lista_simples_mesclados = [1, "a", 2.5, True] # Lista mesclada de diferentes tipos
lista_simples_mesclados.append(None)  # Adiciona o elemento None ao final da lista

nested_list = [[1, 2], [3, 4], [5, 6], ['Ola munda'], ['a', 'b']]  # Lista aninhada
nested_list.append([7, 8])  # Adiciona uma nova lista aninhada

print("Lista simples de inteiros:", lista_simples_inteiros)
print("Lista simples de strings:", lista_simples_string)
print("Lista mesclada:", lista_simples_mesclados)
print("Lista aninhada:", nested_list)

# metodo LEN() desmostra o tamanho da lista
print("Tamanho da lista de inteiros:", len(lista_simples_inteiros)) # exibe o tamanho da lista de inteiros

# O metodo Insert() insere um elemento em uma posição específica
lista_simples_string.insert(2, 'OI')  # Insere o número 10 na posição 2
print("Lista simples de strings após inserção:", lista_simples_string)

# metodo sort() ordena a lista
lista_simples_inteiros.sort()  # Ordena a lista de inteiros
print("Lista simples de inteiros ordenada:", lista_simples_inteiros)

#metodo Count() conta o número de ocorrências de um elemento na lista
count_3 = lista_simples_inteiros.count(3)  # Conta quantas vezes o número 3 aparece na lista
print("Número de ocorrências do número 3:", count_3)