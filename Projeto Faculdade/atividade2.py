nome = []
idade = []

for i in range(3):
    pessoas = input("Digite seu nome: ")
    old = int(input("Digite sua idade: "))
    nome.append(pessoas)
    idade.append(old)

soma_idade = sum(idade)
media_idade = soma_idade  / len(idade)

maior_idade = max(idade)
indice = idade.index(maior_idade)
nome_maior_idade = nome[indice]


print(f'idade mais alta: {maior_idade}')
print(f'Nome da pessoa mais Velha é :{nome_maior_idade}')
print(f'A médias das idades é: {media_idade}')
