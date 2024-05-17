
class Planta:
    def __init__(self, nome, altura, tipo):
        self.nome = nome
        self.altura = altura
        self.tipo = tipo

    def crescer(self, cm):
        self.altura += cm
        print(f'A planta {self.nome} cresceu {cm} cm.')

    def mostrar_info(self):
        print(f'Nome: {self.nome}')
        print(f'Altura: {self.altura}')
        print(f'Tipo: {self.tipo}')


planta1 = Planta("Caju", 60, "Andromonoica")
planta1.mostrar_info()
planta1.crescer(20)
planta1.mostrar_info()
