import abc 

class Veiculo(abc.ABC):
    """Esse é a classe carro que possui atributos e métodos para manipular as informações de um carro."""
    def __init__(self, cor , modelo, ano, tp_combustivel, potencia, qtd_combustivel, is_ligado):
        self.__cor = cor
        self.__modelo = modelo
        self.__ano = ano
        self.__tp_combustivel = tp_combustivel
        self.__potencia = potencia
        self.__qtd_combustivel = qtd_combustivel
        self.__is_ligado = is_ligado
        """"Construtor da classe Carro que inicializa os atributos do carro."""
    @abc.abstractmethod
    def abastecer(self, qtd_combustivel ):
        """Método para abastecer o carro com uma quantidade de combustível especificada."""
        self.__qtd_combustivel += qtd_combustivel
        print(f"Abastecido com {qtd_combustivel} litros. Total agora é {self.__qtd_combustivel} litros.")
        
    def ligar(self):
        """Método para ligar o carro. Se já estiver ligado, informa que já está ligado."""
        if self.__is_ligado:
            print("Veiculo já está ligado")
        else:
            print("O Veiculo foi ligado")
            self.__is_ligado = True
        
    def desligar(self):
        """Método para desligar o carro. Se já estiver desligado, informa que já está desligado."""
        if self.__is_ligado == False:
            print("O veiculo já está  desligado")
        else:
            self.__is_ligado = False    
        
    def tipo(self):
        print(f"Modelo: {self.__modelo}")

    def cor_carro(self):
        print(f"Cor: {self.__cor}")

    def ano_carro(self):
        print(f"Ano: {self.__ano}")

    def acelerar(self, velocidade):
        """Método para acelerar o carro a uma velocidade especificada. Se o carro não estiver ligado, informa que não é possível acelerar."""
        if self.__is_ligado == True:
            print(f"Acelerando a {velocidade} km/h")
        else:
            print("veiculo está desligado. Não é possível acelerar.")
        