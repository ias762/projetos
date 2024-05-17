class Filmes:
    def __init__(self, titulo, duracao, classificacao):
        self.__titulo = titulo
        self.__duracao = duracao
        self.__classificacao = classificacao

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_duracao(self):
        return self.__duracao

    def set_duracao(self, duracao):
        if duracao > 0:
            self.__duracao = duracao
        else:
            print("A duracao não pode ser negativa.")

    def get_classificacao(self):
        return self.__classificacao

    def set_classificacao(self, classificacao):
        self.__classificacao = classificacao

    def mostrar_informacoes(self):
        print(f'Título: {self.__titulo}')
        print(f'Duração: {self.__duracao}')
        print(f'Classificação: {self.__classificacao}')


filme = Filmes("Interestellar", 148, "PG-13")
filme.mostrar_informacoes()

filme.set_titulo("Exterminador do Futuro")
filme.set_duracao(180)
filme.set_classificacao("PG-15")

filme.mostrar_informacoes()
