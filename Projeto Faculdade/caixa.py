caixa = []



while True:
    print('1 - adicionar venda')
    print('2 - valor total do dia')
    print('3 - limpar caixa')
    print('4 - sair')

    opcao = input('Escolha uma opção: ')

    if (opcao == '1'):
        try:
            valor =  float(input('digite um valor:'))
            caixa.append(valor)
            print('valor adicionado')
        except ValueError:
            print('valor invalido')
    
    elif (opcao == '2'):
        
        print(f' valor total: {sum(caixa):.2f}')
    
    elif (opcao == '3'):
        caixa.clear()
        print('caixa limpo')

    elif (opcao == '4'):
        break
    else:
        print('opção inválida')