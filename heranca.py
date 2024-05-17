class Embarcacao:
  def __init__(self, nome, capacidade):
    self.nome = nome
    self.capacidade = capacidade

  def mostrar_informacoes(self):
    print(f'Nome: {self.nome}')
    print(f'Capacidade: {self.capacidade} pessoas.')

class Navio(Embarcacao):
  def __init__(self, nome, capacidade, tipo_carga):
    super().__init__(nome, capacidade)
    self.tipo_carga = tipo_carga

  def mostrar_informacoes(self):
    super().mostrar_informacoes()
    print(f'Tipo de Carga: {self.tipo_carga}')

class Barco(Embarcacao):
  def __init__(self, nome, capacidade, comprimento):
    super().__init__(nome, capacidade)
    self.comprimento = comprimento

  def mostrar_informacoes(self):
    super().mostrar_informacoes()
    print(f'Comprimento: {self.comprimento} metros.')

navio = Navio("Titanic", 3000, "Passageiros")
barco = Barco("Mosquito", 4, 2.5)

navio.mostrar_informacoes()
print("-----------------")
barco.mostrar_informacoes()

