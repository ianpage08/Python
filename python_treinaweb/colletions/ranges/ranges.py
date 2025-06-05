#  a tres forma de criar ranges
# range() - Cria um objeto range que representa uma sequência de números
# range(start, stop) - Cria um objeto range que representa uma sequência de números de start até stop-1
# range(start, stop, step) - Cria um objeto range que representa uma sequência de números de start até stop-1 com um passo especificado por step
# a contagem sempre vai ser -1 do valor final, ou seja, se eu colocar range(0, 10) o valor final vai ser 9
#pois a contagem e feita a partir do 0, e o valor final é exclusivo.
range_simples = range(10)  # Cria um range de 0 a 9
print(range_simples)  # Exibe o objeto range

for i in range_simples:  # Itera sobre o range simples
    print(i)  # Imprime os valores de 0 a 9
range_comecando_em_6 = range(6,10) # Cria um range de 6 a 9
print(range_comecando_em_6)  # Exibe o objeto range
for i in range_comecando_em_6:  # Itera sobre o range começando em 6
    print(i)  # Imprime os valores de 6 a 9
range_comecando_em_4_com_passo_2 = range(4,20,2)  # Cria um range de 4 a 18 com passo 2
print(range_comecando_em_4_com_passo_2)  # Exibe o objeto range
for i in range_comecando_em_4_com_passo_2:  # Itera sobre o range começando em 4 com passo 2
    print(i)  # Imprime os valores de 4 a 18 com passo 2