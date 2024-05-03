class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_informacoes(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}')

# Exemplo de uso:
meu_carro = Carro('Toyota', 'Corolla')
meu_carro.exibir_informacoes()


