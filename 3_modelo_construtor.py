class Pessoas:
    def __init__(self, nome, idade, cpf):
        print(f'{nome} | {idade} | {cpf}')


    def logar_sistema(self):
        print(f'Estou logando no sistema.')

p1 = Pessoas('Ésley Nathan', 21, '14190413712')
p2 = Pessoas('Ésley', 25, '111.123.123-12')
p3 = Pessoas('Nathan', 30, '321.313.312-30')