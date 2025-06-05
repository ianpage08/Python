lista_simples_inteiros = [1, 7, 3, 9, 10, 5, 3 , 4] # Lista simples de inteiros 
lista_simples_inteiros.sort()  # Ordena a lista de forma crescente
meu_iter = iter(lista_simples_inteiros)  # Cria um iterador a partir da lista


print(next(meu_iter))  # Obtém o primeiro elemento do iterador
print(next(meu_iter))  # Obtém o segundo elemento do iterador