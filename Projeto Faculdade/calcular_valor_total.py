caixa_fechado = []
caixa_aberto = []


while True:
    add = input('valor da venda: ')
    if (add == '' or add == 0):
        break

    try:
        add = float(add)
        caixa_aberto.append(add)
        caixa_fechado = sum(caixa_aberto)
        print(f'Valor Total: R${caixa_fechado:.2f}')

    except ValueError:
        print('Por favor digite um valor válido')
