nome = []
idade = []

for i in range(3):
    nomes = input("Digite seu nome: ")
    idades = int(input("Digite sua idade: "))
    nome.append(nomes)
    idade.append(idades)

soma_idade = sum(idade)
media_idade = soma_idade  / len(idade)

maior_idade = max(idade)
indice = idades.index(maior_idade)
nome_maior_idade = nome[indice]


print(maior_idade)
print(nome_maior_idade)
print(media_idade)
