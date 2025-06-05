class MeuIterator:
    def __init__(self, max=0): # Construtor que recebe o valor máximo
        self.max = max # Atributo que armazena o valor máximo
        
        
    def __iter__(self): # Método que retorna o próprio iterador
        self.atual = 0 # Atributo que armazena o valor atual do iterador
        return self # Retorna o próprio iterador
    
    def __next__(self): 
        if self.atual < self.max: # Verifica se o valor atual é menor que o valor máximo
            resultado = 2 ** self.atual # Calcula valor elevado a 2 na potência do valor atual
            self.atual += 1 # Incrementa o valor atual
            return resultado # Retorna o valor calculado
        else: 
            raise StopIteration # Lança uma exceção para indicar que não há mais elementos para iterar
        
for i in MeuIterator(10): # Cria um iterador com o valor máximo 10
    print(i) # Imprime os valores do iterador, que são potências de 2 de 0 a 9