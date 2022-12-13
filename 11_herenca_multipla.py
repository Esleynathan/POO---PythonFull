class Animal:
        def andar(self):
                print('Estou andando como um animal')

        def correr(self):
                print('Estou correndo')

        def pular(self):
                print('Estou pulando')

class Felino(Animal):
        def felino(self):
                print('Eu sou um felino')                

class Cachorro(Animal):
        def latir(self):
                print('Estou latindo')

class Gato(Felino):
        def miar(self):
                print('Estou miando')

Juan = Gato()

Juan.andar()
Juan.felino()
Juan.miar()

print('\n=============\n')

Eva = Cachorro()
Eva.latir()