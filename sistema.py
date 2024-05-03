class Funcionario:
    def __init__(self, nome, id, salario):
        self.__nome = nome
        self.__id = id
        self.__salario = salario

    def atualizar_salario(self, novo_salario):
        if novo_salario > self.__salario:
            self.__salario = novo_salario
            print(f"Salário atualizado para R${self.__salario:.2f}")
        else:
            print("O novo salário deve ser maior que o salário atual.")

    def exibir_info(self):
        return f"ID: {self.__id}, Nome: {self.__nome}, Salário: R${self.__salario:.2f}"

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f"Funcionário {funcionario.exibir_info()} adicionado ao departamento {self.nome}.")

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario.exibir_info())

# Exemplo de uso:
depto = Departamento("TI")
func1 = Funcionario("João", 1, 5000)
func2 = Funcionario("Maria", 2, 6000)
depto.adicionar_funcionario(func1)
depto.adicionar_funcionario(func2)
depto.listar_funcionarios()
