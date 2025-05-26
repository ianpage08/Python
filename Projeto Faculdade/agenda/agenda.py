

while True:
    
    print('1 - Acessar agenda 1')
    print('2 - Acessar agenda 2')
    print('3 - Sair')
    opcao = input('Escolha uma opção:')
    if (opcao == '1'):
        arquivo = 'agenda1.txt'

    elif(opcao == '2'):
        arquivo = 'agenda2.txt'
    
    elif (opcao == '3'):
        print('Saindo...')
        break
    else:
        print('Opção inválida')
        continue


    while True:
        
        print('1 - Adicionar contato na agenda ')
        print('2 - Listar Contatos Agenda ')
        print('3 - buscar nome Agenda ')
        print('4 - deletar contato Agenda ')
        print('5 - Voltar para menu principal')
        escolha = input('Escolha uma opção:')

        if (escolha == '1'):
            nome = input('Digite o nome do contato:')
            telefone = input('Digite o telefone do contato:')

            with open(file=arquivo, mode='a', encoding='utf8') as escrever:
                escrever.write(f'{nome},{telefone}\n')
                print('Contato adicionado com sucesso!')
            

            
        elif (escolha == '2'):
            print('Lista de Contatos')
            
            try:
                
                with open(file=arquivo, mode='r', encoding='utf8') as ler:
                    agenda1 = ler.read()
                    print(f'Contatos Adicionados {agenda1}')

            except FileNotFoundError:
                print('Arquivo não encontrado')
        elif (escolha == '3'):
            buscar = input('Digite o nome do contato:')
            try:
                with open(file=arquivo, mode='r', encoding='utf8') as ler:
                    encontrados = [linhas for linhas in ler.readlines() if (buscar.lower() in linhas.lower())]
                    if (encontrados):
                        print('Contatos Encontrados')
                        for linhas in encontrados:
                            print(linhas.strip())
                    else:
                        print('Contato não encontrado')
            except FileNotFoundError:
                print('Arquivo não encontrado')
        
        elif (escolha == '4'):
            deletar = input('Digite o nome do contato:')
            try:
                with open(file=arquivo, mode='r', encoding='utf8') as ler:
                    linhas = ler.readlines()
                with open(file=arquivo, mode='w', encoding='utf8') as escrever:
                    for linha in linhas:
                        if (deletar.lower() not in linha.lower()):
                            escrever.write(linha)
                print('Contato deletado com sucesso!')
            except FileNotFoundError:
                print('Arquivo não encontrado')
        elif (escolha == '5'):
            print('Voltando para o menu principal...')
            break
        else:
            print('Opção inválida')
            continue
        

        
            
            

