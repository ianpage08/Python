my_list = [1,2,3,4,5,6]

for item in my_list:
    print(item)

iter_Exemple = iter(my_list)
print(next(iter_Exemple))

def gen():
    n = 1 
    print('esse  meu numero 1')
    yield n

    n += 1
    print('esse  meu numero 2')
    yield n

    n += 1
    print('esse  meu numero 3')
    yield n

