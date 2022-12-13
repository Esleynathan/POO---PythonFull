class Pessoas:
    possui_olho = True
    possui_boca = True
    raca = "Ser humano"
    pernas = 2

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def retorna_nome(self):
        return self.nome

    def logar_sistema(self):
        print(f'{self.retorna_nome()} Está logando no sistema')

    @classmethod
    def andar(cls):
        cls.possui_boca = False

#p1 = Pessoas('Ésley Nathan', 21)
#p2 = Pessoas('Nathan', 40)

print(Pessoas.possui_boca)

Pessoas.andar()

print(Pessoas.possui_boca)