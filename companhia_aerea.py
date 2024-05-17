class Aviao:
    def __init__(self, modelo, capacidade, companhia):
        self.modelo = modelo
        self.capacidade = capacidade
        self.companhia = companhia

    def decolar(self):
        print(f'O avião {self.modelo} da companhia {
              self.companhia} está decolando.')

    def aterrisar(self):
        print(f'O avião {self.modelo} da companhia {
              self.companhia} está aterrissando.')

    def mostrar_informacoes(self):
        print(f'Modelo: {self.modelo}')
        print(f'Capacidade: {self.capacidade}')
        print(f'Companhia: {self.companhia}')


aviao1 = Aviao("Boeing 737 MAX", 200, "GOL")
aviao1.mostrar_informacoes()
aviao1.decolar()
aviao1.aterrisar()
