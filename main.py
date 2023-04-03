class keven:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade

    def setnome(self, nome):
        self.nome = nome

    def setidade(self, idade):
        self.idade = idade
        
    def getnome(self):
        return self.nome

    def getidade(self):
        return self.idade