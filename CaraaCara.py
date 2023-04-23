import random
import usuariocaraacara
class Jogo:
    def __init__(self, nome : str):
        self.nomes = nome

    @property
    def nome(self):
        return self.nomes

    @nome.setter
    def nome(self, nome):
        self.nomes = nome


    def lugar_sorteado(self)-> str :
        """
        Função que sorteia o lugar e já dá a dica
        :return: str
        """

        Maranhao = ["Lençóis freáticos",
                    "Pálacio dos Leões",
                    "Parque Nacional Chapada das mesas",
                    "Catedral Metropolitana Nossa Senhora da Vitória",
                    "São Luis"
                    ]

        Bahia = ["Elevador lacerda",
                 "Basilica do Senhor do Bonfim",
                 "Mercado Modelo",
                 "Parque Nacional Chapada da Diamantina",
                 "Salvador"]

        lista = [Maranhao, Bahia]

        lugar_sorteado = random.choice(lista)
        sorteio = random.randint(0, 4)
        if lugar_sorteado == lista[1]:
            print("Dica: ", Bahia[sorteio])
            return "Bahia"
        elif lugar_sorteado == lista[0]:
            print("Dica: ",Maranhao[sorteio])
            return "Maranhao"


    @property
    def pessoas(self) -> str:
        """
        Função que retorna as pessoas
        :return: str
        """
        return self.nomes

    @pessoas.setter
    def pessoas(self, pessoa : str) -> None:
        """
        Função que atribui valor para nomes
        :param pessoa:
        :return: None
        """
        self.nomes = pessoa

    def pessoa_sorteada(self) -> str:
        """
        Função que sorteia a pessoa já cpm a dica
        :return: str
        """
        Keven = ["O mais lindo",
                    "Cabelo cacheado",
                    "Veio de Salvador",
                    "A pessoa mais da hora",
                    "Faz aniversário em outubro"
                    ]

        Manuela = ["Cabelo cachead",
                 "Faz faculdade no IF",
                 "Mora em uma cidade pequena",
                 "Esse mês faz 19 anos",
                 "Melhor front-end"]

        lista = [Keven, Manuela]

        pessoa_sorteada = random.choice(lista)
        sorteio = random.randint(0, 4)
        if pessoa_sorteada == lista[0]:
            print("Dica: ", Keven[sorteio])
            return "Keven"
        elif pessoa_sorteada == lista[1]:
            print("Dica: ", Manuela[sorteio])
            return "Manuela"


    def objeto_sorteado(self) -> str:
        """
        Função que sorteia o objeto já com a dica
        :return: str
        """
        Lapis = ["Serve para desenhar",
                 "Serve para escrever",
                 "Tem de cor",
                 "Se apontar de mais fica pequeno",
                 "Faber castell é o melhor"]

        Tenis = ["Têm várias cores",
                 "Pisa em lugares e em coisas",
                 "Algumas marcas é bem caro",
                 "Alguns são confortáveis",
                 "Senão cuidar fica com chulé"]

        lista = [Lapis, Tenis]
        objeto_sorteado = random.choice(lista)
        sorteio = random.randint(0, 4)
        if objeto_sorteado == lista[1]:
            print(Lapis[sorteio])
            return "Lapis"
        elif objeto_sorteado == lista[0]:
            print(Tenis[sorteio])
            return "Tenis"



































