class Veiculo:
    def __init__(self, quantidade_rodas, capacidade_tanque):
        self._quantidade_rodas = quantidade_rodas
        self._capacidade_tanque = capacidade_tanque

    def get_quantidade_rodas(self):
        return self._quantidade_rodas

    def set_quantidade_rodas(self, quantidade_rodas):
        self._quantidade_rodas = quantidade_rodas

    def get_capacidade_tanque(self):
        return self._capacidade_tanque

    def set_capacidade_tanque(self, capacidade_tanque):
        self._capacidade_tanque = capacidade_tanque

    def exibir_info(self):
        print(f"Quantidade de rodas: {self._quantidade_rodas}")
        print(f"Capacidade do tanque: {self._capacidade_tanque} litros")


class Carro(Veiculo):
    def __init__(self, quantidade_rodas, capacidade_tanque, numero_portas):
        super().__init__(quantidade_rodas, capacidade_tanque)
        self._numero_portas = numero_portas

    def get_numero_portas(self):
        return self._numero_portas

    def set_numero_portas(self, numero_portas):
        self._numero_portas = numero_portas

    def dirigir(self):
        print("Dirigindo o carro...")


class Bicicleta(Veiculo):
    def __init__(self, quantidade_rodas, capacidade_tanque, tipo_terreno):
        super().__init__(quantidade_rodas, capacidade_tanque)
        self._tipo_terreno = tipo_terreno

    def get_tipo_terreno(self):
        return self._tipo_terreno

    def set_tipo_terreno(self, tipo_terreno):
        self._tipo_terreno = tipo_terreno

    def pedalar(self):
        print("Pedalando a bicicleta...")


carro = Carro(4, 60, 4)
print(f"Carro:{carro.get_numero_portas()} portas")
print(f"Capacidade do tanque: {carro.get_capacidade_tanque()} litros")
carro.dirigir()

bicicleta = Bicicleta(2, 0, "urbano")
print(f"Bicicleta: Para terreno {bicicleta.get_tipo_terreno()}")
print(f"Quantidade de rodas: {bicicleta.get_quantidade_rodas()}")
print(f"Capacidade do tanque: {bicicleta.get_capacidade_tanque()} litros")
bicicleta.pedalar()
