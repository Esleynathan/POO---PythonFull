class Pessoas:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
    def logar_sistema(self):
        print(f'{self.nome} esta logando no sistema.')

p1 = Pessoas('Ésley', 20, '141.194.137-12')
p2 = Pessoas('Nathan', 40, '141.194.137-12')

p1.logar_sistema()
p2.logar_sistema()
