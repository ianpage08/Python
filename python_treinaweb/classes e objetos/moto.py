import veiculo

class Moto(veiculo.Veiculo):
    def __init__(self, tipo, cor, modelo, ano, tp_combustivel, potencia, qtd_combustivel, is_ligado):
        # Importa a classe Veiculo para herdar seus atributos e métodos. "super().__init__()"
        super().__init__(cor, modelo, ano, tp_combustivel, potencia, qtd_combustivel, is_ligado)
        self.tipo = tipo
        """Construtor da classe Moto que inicializa os atributos da moto e chama o construtor da classe Veiculo."""
    
    def tipo_moto(self):
        print(f"Tipo: {self.tipo}")
    
    def ligar(self):
        """Método para ligar a moto. Se já estiver ligada, informa que já está ligada."""
        if self.is_ligado:
            print("Moto já está ligada")
        else:
            print("A Moto foi ligada")
            self.is_ligado = True
            
    def abastecer(self):
        pass