class Streaming:
    def __init__(self, nome, preco_mensal):
        self.nome = nome
        self.preco_mensal = preco_mensal

    def mostrar_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Preço Mensal: {self.preco_mensal}')


class Netflix(Streaming):
    def __init__(self, nome, preco_mensal, numero_de_series):
        super().__init__(nome, preco_mensal)
        self.numero_de_series = numero_de_series

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f'Número de Séries: {self.numero_de_series}')


class Spotify(Streaming):
    def __init__(self, nome, preco_mensal, numero_de_musicas):
        super().__init__(nome, preco_mensal)
        self.numero_de_musicas = numero_de_musicas

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f'Número de músicas: {self.numero_de_musicas}')


netflix = Netflix("Netflix", 39.90, 5000)
spotify = Spotify("Spotify", 11.99, 7000000)

netflix.mostrar_informacoes()
print("--------------------")
spotify.mostrar_informacoes()
