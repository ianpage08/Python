# o dicionario é uma coleção de pares chave-valor
# onde cada chave é única e mapeada para um valor específico.
# os dicionarios são mutaveis, ou seja, posso adicionar, remover e alterar os valores do dicionario
# bem diferentes do set, range, # e frozenset que são imutaveis
#  ele tem uma especie de indetificador # que é a chave, e o valor é o que eu quero armazenar

meu_dicionario = {
    
    1: 'Python',
    2: 'Java',
    3: 'C++',
    4: 'JavaScript',
    5: 'Ruby',
} 


# eu posso criar um dicionario dentro de outro dicionario
meu_dicionario_aninhado = {
    'Python': {
        'nome': 'Python',
        'tipo': 'Linguagem de programação',
        'paradigma': 'Multiparadigma',
        'criador': 'Guido van Rossum',
        'ano_criacao': 1991
    },
    'Java': {
        'nome': 'Java',
        'tipo': 'Linguagem de programação',
        'paradigma': 'Orientada a objetos',
        'criador': 'James Gosling',
        'ano_criacao': 1995
    }
}

#para tranformar uma lista em dicionario eu utilizo o metodo dict()
minha_lista = [('Python', 'Linguagem de programação'), ('Java', 'Linguagem de programação')]
meu_dicionario_a_partir_de_uma_lista = dict(minha_lista)
print(meu_dicionario_a_partir_de_uma_lista)
print(type(meu_dicionario_a_partir_de_uma_lista))  # Exibe o tipo do dicionário criado a partir da lista


# Exibe o dicionário uso o iterador items() 
for chave, valor in meu_dicionario.items():
    print(f'A chave é{chave}:e o Valor é {valor}')  # Itera sobre o dicionário e exibe cada chave e seu valor correspondente


# Uso de Get para acessar valores
print(meu_dicionario.get(1))  # Acessa o valor associado à chave 1
print(meu_dicionario.get(6, 'chave não encontrada'))  # Acessa o valor associado à chave 6, retornando uma mensagem se a chave não existir

# para eu receber o valor de uma chave
print(f'utilizando a [chaves] eu pego o valor da chave e não preciso utilizar o get {meu_dicionario[2]}'  )

# para eu pegar o tamanho utilizo o len()
print(f'O tamanho do dicionario é {len(meu_dicionario)} para o tamanho eu pego a chave e valor para contar 1')  # Exibe o tamanho do dicionário

#o metodo keys() retorna todas as chaves do dicionario
print(meu_dicionario.keys())  # Exibe todas as chaves do dicionário

# metodo clear() para limpar o dicionario
meu_dicionario.clear()  # Limpa o dicionário, removendo todos os pares chave-valor
print(meu_dicionario)  # Exibe o dicionário após ser limpo, que agora estará vazio