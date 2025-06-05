lista_simples_inteiros = [1, 7, 3, 9, 10, 5, 3 , 4] # Lista simples de inteiros
lista_simples_inteiros.sort()  # Ordena a lista de inteiros
nova_lista_2 = []  # Cria uma nova lista para armazenar os quadrados

for i in lista_simples_inteiros:

    nova_lista_2.append(i * i)  # Adiciona o quadrado do elemento ao final da lista

print("Lista simples de inteiros após adição dos quadrados:", nova_lista_2)

nova_lista_3 = [i * i for i in lista_simples_inteiros]  # Compreensão de lista para criar nova lista com quadrados
print("Lista simples de inteiros após adição dos quadrados com compreensão de lista:", nova_lista_3)