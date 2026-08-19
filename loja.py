class Cliente:
    def __init__(self, nome, cpf, dataNascimento, saldo, credito):
        self.__nome = nome
        self.__cpf = cpf
        self.__dataNascimento = dataNascimento
        self.__saldo = saldo
        self.__credito = credito

    def extrato(self):
        print(f"\nCliente: {self.__nome}")
        print(f"CPF: {self.__cpf}")
        print(f"Saldo: R$ {self.__saldo:.2f}")
        print(f"Crédito: R$ {self.__credito:.2f}")

    def adicionar_credito(self, valor):
        if valor <= 0:
            print("Valor inválido.")
        else:
            self.__credito += valor
            print(f"Crédito adicionado: R$ {valor:.2f}")

    def compra_permitida(self, valor):
        valor_disponivel = self.__saldo + self.__credito
        return valor <= valor_disponivel

    def comprar_carro(self, valor):
        if valor <= 0:
            print("Valor da compra inválido.")
            return

        if self.compra_permitida(valor):
            if self.__credito >= valor:
                self.__credito -= valor
            else:
                restante = valor - self.__credito
                self.__credito = 0
                self.__saldo -= restante

            print("Compra realizada com sucesso!")
        else:
            print("Saldo e crédito insuficientes.")

    @property
    def nome(self):
        return self.__nome

    @property
    def saldo(self):
        return self.__saldo

    @property
    def credito(self):
        return self.__credito

    @property
    def cpf(self):
        return self.__cpf


# CLASSE PAI
class Carro:
    def __init__(self, ano, modelo, quilometragem):
        self.__ano = ano
        self.__modelo = modelo
        self.__quilometragem = quilometragem

    @property
    def ano(self):
        return self.__ano

    @property
    def modelo(self):
        return self.__modelo

    @property
    def quilometragem(self):
        return self.__quilometragem

    def mostrar_dados(self):
        print(f"Ano: {self.__ano}")
        print(f"Modelo: {self.__modelo}")
        print(f"Quilometragem: {self.__quilometragem} km")

    # Método especial/built-in __str__
    def __str__(self):
        return f"{self.__modelo} - {self.__ano}"


# CLASSE FILHA
class CarroVendido(Carro):

    def __init__(self, ano, modelo, quilometragem, valor_venda):
        super().__init__(ano, modelo, quilometragem)
        self.__valor_venda = valor_venda

    def gerar_credito(self, cliente):
        cliente.adicionar_credito(self.__valor_venda)

        print(f"\nCarro vendido: {self.modelo}")
        print(f"Crédito gerado: R$ {self.__valor_venda:.2f}")

    @property
    def valor_venda(self):
        return self.__valor_venda


# CLASSE FILHA
class CarroNovo(Carro):

    def __init__(self, ano, modelo, quilometragem, valor_novo):
        super().__init__(ano, modelo, quilometragem)
        self.__valor_novo = valor_novo

    def vender(self, cliente):
        print(f"\nCarro escolhido: {self.modelo}")
        print(f"Valor: R$ {self.__valor_novo:.2f}")

        cliente.comprar_carro(self.__valor_novo)

    @property
    def valor_novo(self):
        return self.__valor_novo

    @staticmethod
    def nome_loja():
        return "Clovis-Car"


# PROGRAMA PRINCIPAL

cliente1 = Cliente(
    "Gregory",
    "123.456.789-00",
    "10/05/2008",
    15000,
    5000
)

carro_usado = CarroVendido(
    2020,
    "Honda Civic",
    50000,
    30000
)

carro_novo = CarroNovo(
    2025,
    "Toyota Corolla",
    0,
    45000
)

# Mostrando informações do cliente
cliente1.extrato()

# Cliente vende seu carro e recebe crédito
carro_usado.gerar_credito(cliente1)

# Mostrando o novo extrato
cliente1.extrato()

# Mostrando informações do carro
print("\nInformações do carro:")
carro_novo.mostrar_dados()

# Usando o método __str__
print(f"\nCarro: {carro_novo}")

# Verificando se o objeto pertence à classe Carro
print("\nÉ um carro?", isinstance(carro_novo, Carro))

# Comprando o carro
carro_novo.vender(cliente1)

# Extrato final
cliente1.extrato()

# Método estático
print(f"\nLoja: {CarroNovo.nome_loja()}")
    
