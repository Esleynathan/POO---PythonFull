# class Vendedor:    
#     def falar(self):
#         print('Estou falando')
#     def andar(self):
#         print('Estou andando')
#     def vender(self):
#         print('Estou vendendo')

# class Cliente:    
#     def falar(self):
#         print('Estou falando')
#     def andar(self):
#         print('Estou andando')    
#     def comprar(self):
#         print('Estou comprando')

class Pessoa:
    def falar(self):
        print('Estou falando')
    
    def andar(self):
        print('Estou falando')

class Vendedor(Pessoa):
    def vender(self):
        print ('Estou vendendo')

class Cliente(Pessoa):
    def comprar(self):
        print('Estou comprando')

c1 = Cliente()        
c2 = Vendedor()


c1.andar()
c1.falar()
c1.comprar()

c2.andar()
c2.falar()
c2.vender()
