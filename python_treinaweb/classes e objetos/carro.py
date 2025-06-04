import veiculo
class Carro(veiculo.Veiculo):
    def __init__(self, qtd_portas, cor, modelo, ano, tp_combustivel, potencia, qtd_combustivel, is_ligado):
        # Importa a classe Veiculo para herdar seus atributos e métodos. "super().__init__()"
        super().__init__(cor, modelo, ano, tp_combustivel, potencia, qtd_combustivel, is_ligado)
        self.qtd_portas = qtd_portas
        """Construtor da classe Carro que inicializa os atributos do carro e chama o construtor da classe Veiculo."""
        self.qtd_portas = qtd_portas
    
    def abastecer(self, qtd_combustivel):
        pass

