class Conta:
    def __init__(self, numero : int, titular : str, saldo : float, limite : float):
        """
        funão que constroi um ojeto do tipo conta
        :param numero: int
        :param titular: str
        :param saldo: float
        :param limite: float
        """
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        print("Construindo objeto!")

    def extrair(self) -> None:
        """
        funcao que mostra o que tem na conta
        :return:none
        """
        print(f"O saldo do {self.titular} é {self.get_saldo()}")

    def depositar(self, valor:float) -> None:
        """
        funcao que adiciona o valor na conta
        :param valor: float
        :return: none
        """
        self.__saldo += valor
        print(f"O saldo atual é {self.get_saldo()}")

    def sacar(self, valor) -> None:
        """
        funcao que tira dinheiro disponivel na conta
        :param valor: float
        :return: none
        """
        if self.__verificar_saque(valor):
            self.__saldo -= valor
        else:
            print(f"o valor {valor} passou do limite")

    def transferir(self, valor : float, destino) -> None:
        """

        :param valor: float
        :param destino: conta
        :return: none
        """
        self.sacar(valor)
        destino.depositar(valor)

    def get_saldo(self):
        return self.__saldo
    #
    # def set_limite(self, limite : float):
    #     self.__limite = limite


    @property
    def titular(self):
        return self.__titular.upper()

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor : float):
        if valor <= 1.1 * self.__limite:
            self.__limite = valor

        else:
            print("Limite acima de 10% - consulte um gerente")

    @property
    def saldo(self):
        return self.__saldo

    def __verificar_saque(self, valor : float) -> None:
        if valor <= self.limite + self.__saldo:
            return True
        else:
            return False


if __name__ == "__main__":

    conta = Conta(numero=123, titular="keven", saldo=230.34, limite= 2222.54)
    conta_2 = Conta(122, "Maria", 34.43, 45.45)
    conta.limite = 600

    print(conta.sacar(30.34), conta.depositar(120.00), conta.transferir(20.00, conta_2),  conta.__dict__ )
    conta.sacar(100)

# self é referencia que sabe encontrar o objeto construido em memoria