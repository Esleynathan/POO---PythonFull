class Pessoas:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def retorna_nome(self):
        return self.nome

    def logar_sistema(self):
        print(f'{self.retorna_nome()} Está logando no sistema')

p1 = Pessoas('Ésley Nathan', 21, '14190413712')
p2 = Pessoas('Nathan', 25, '14190413721')

p2.logar_sistema()