class Usuario:
    def __init__(self, nome, nivel_acesso):
        self.__nome = nome
        self.__nivel_acesso = nivel_acesso

    def get_nivel_acesso(self):
        return self.__nivel_acesso

    @property
    def nome(self):
        return self.__nome

class SistemaSeguranca:
    @staticmethod
    def verificar_acesso(usuario, nivel_requerido):
        if usuario.get_nivel_acesso() >= nivel_requerido:
            print(f"Acesso concedido a {usuario.nome}.")
        else:
            print(f"Acesso negado a {usuario.nome}.")

# Exemplo de uso:
usuario1 = Usuario("Ana", 3)
usuario2 = Usuario("Pedro", 1)
SistemaSeguranca.verificar_acesso(usuario1, 2)  # Acesso concedido
SistemaSeguranca.verificar_acesso(usuario2, 2)  # Acesso negado
