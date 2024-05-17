

class Funcionarios:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_nome(self):
        return self.nome

    def exibir_salario(self):
        return self.salario


class Gerente(Funcionarios):
    def __init__(self, nome, salario, area):
        super().__init__(nome, salario)
        self.area = area

    def exibir_area(self):
        return self.area


class Programador(Funcionarios):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def exibir_linguagem(self):
        return self.linguagem


class Analista(Funcionarios):
    def __init__(self, nome, salario, nivel):
        super().__init__(nome, salario)
        self.nivel = nivel

    def exibir_nivel(self):
        return self.nivel


funcionario1 = Funcionarios("Iago", 3000)
print("Funcionario:", funcionario1.exibir_nome())
print("Salario:", funcionario1.exibir_salario())

gerente1 = Gerente("Maria", 5000, "TI")
print("\nGerente:", gerente1.exibir_nome())
print("Salario:", gerente1.exibir_salario())
print("Area:", gerente1.exibir_area())

programador1 = Programador("Fernanda", 8000, "Python")
print("\nProgramador:", programador1.exibir_nome())
print("Salario:", programador1.exibir_salario())
print("Linguagem:", programador1.exibir_linguagem())

analista1 = Analista("Fábio", 10000, "Sênior")
print("\nAnalista:", analista1.exibir_nome())
print("Salario:", analista1.exibir_salario())
print("Nivel:", analista1.exibir_nivel())
