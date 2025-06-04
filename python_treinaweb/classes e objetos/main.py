import carro, moto
# Importa as classes Carro e Moto do módulo carro e moto respectivamente.
bugatti = carro.Carro(2, "azul", "bugatti", 2023, "gasolina", 1000, 50, False)


bugatti.tipo()
bugatti.cor_carro()
bugatti.ano_carro()
bugatti.abastecer(20)  
bugatti.ligar()
bugatti.acelerar(200)

cb300 = moto.Moto("esportiva", "preto", "CB300", 2023, "gasolina", 50, 10, False)

cb300.tipo_moto()
print(cb300.is_ligado)
cb300.ligar()
print(cb300.is_ligado)

