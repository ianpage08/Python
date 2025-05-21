from functools import reduce

notas = []

for i in range(4):
    i = None
    nota = float(input("Digite a nota: "))
    notas.append(nota)

soma = reduce(lambda x, y: x + y, notas)
media = soma / len(notas)
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")