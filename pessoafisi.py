from main import keven

class pessoajuri(keven):
    def __init__(self, nome, idade, cnpj):
        super().__init__(nome, idade)
        self.cnpj = cnpj

    def getcnpj(self):
        return self.cnpj
    def setcnpj(self, cnpj):
        self.cnpj = cnpj