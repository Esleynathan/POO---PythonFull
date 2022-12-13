# class Pessoa:
#     def falar(self):
#         print('Estou falando')
    
#     def andar(self):
#         print('Estou andando')

# class Cliente(Pessoa):
#     def comprar(self):
#         print('Estou comprando')

#     #Sobrepondo o falar de pessoas.    
#     def falar(self):
#         super().falar()
#         print('Estou gritando')

# class Vendedor(Pessoa):
#     def vender(self):
#         print ('Estou vendendo')            

# c1 = Cliente()        
# c2 = Vendedor()

# c1.andar()
# c1.falar()
# c1.comprar()

# c2.andar()
# c2.falar()
# c2.vender()

class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Cliente(Pessoa):
   def __init__(self, id_cliente, nome, cpf):
        super().__init__(nome, cpf)
        self.id_cliente = id_cliente

class Vendedor(Pessoa):
   def __init__(self, id_vendedor, nome, cpf):
        super().__init__(nome, cpf)
        self.id_vendedor = id_vendedor

c1 = Cliente(2,'Ésley','141904137-12')
c2 = Vendedor(5,'Nathan','000.000.000-00')

print(c1.id_cliente)
print(c1.nome)
print(c1.cpf)
print('================')
print(c2.id_vendedor)
print(c2.nome)
print(c2.cpf)