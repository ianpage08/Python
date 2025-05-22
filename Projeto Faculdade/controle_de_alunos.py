alunos_notas = [] 


while True:
    print('1 - adicionar aluno e notas')
    print('2 - listar alunos e notas')
    print('3 - Alunos aprovados')
    print('4 - sair')
    opcao = input('Escolha uma opção: ')
    
    
    if (opcao == '1'):
        nome = input('nome: ')
        nota1 = float(input('nota1: '))
        nota2 = float(input('nota2: '))
        alunos_notas.append({'nome': nome, 'nota1': nota1, 'nota2': nota2})
    elif (opcao == '2'):
        print(alunos_notas)
    
    elif (opcao == '3'):
        for aluno in alunos_notas:
            nome = aluno['nome']
            nota1 = aluno['nota1']
            nota2 = aluno['nota2']
            media =  (nota1 + nota2) / 2
            if (media >= 5):
                
                print(f'{aluno["nome"]} está aprovado, com Média {media:.2f}')
            else:
                print(f'{aluno["nome"]} está reprovado, com média {media:.2f}')
    elif (opcao == '4'):
        break
    else:
        print('Opção inválida')