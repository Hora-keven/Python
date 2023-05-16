from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import banco


class Bot:
    def __init__(self):
        self.navegador = webdriver.Chrome()
        self.navegador.get("https://www.zoom.com.br")
        self.navegador.maximize_window()
        self.samsung()
        self.iphone()
        self.motorola()
        self.xiaomi()
        self.multilaser()
        self.remove_banco_dados()
        self.add_banco_dados()

    def samsung(self) -> None:
        """
        Função que pega os celulares da Samsung
        :return: None
        """
        self.navegador.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/input").click()
        self.navegador.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/input").send_keys("celular samsung")
        self.navegador.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/button").click()
        sleep(5)

        self.lista_samsung = []
        self.valor_samsung = []

        for i in range(6):
            var = self.navegador.find_element(By.XPATH, f"/html/body/div[1]/div[1]/div/div[2]/div[3]/div[{i+1}]/a/div[2]/div[2]/div[1]/div[1]/h2").text.split()
            tira_espaco = "".join(var[0:5])
            self.lista_samsung.append(tira_espaco)
            var_valor = self.navegador.find_element(By.XPATH, f"/html/body/div[1]/div[1]/div/div[2]/div[3]/div[{i+1}]/a/div[2]/div[2]/div[2]/p[1]").text.split()

            tira_espaco_valor = "".join(var_valor[0:4])
            self.valor_samsung.append(tira_espaco_valor)

        for i in range(4):
            var1 = self.navegador.find_element(By.XPATH, f"/html/body/div[1]/div[1]/div/div[2]/div[3]/div[{i+9}]/a/div[2]/div[2]/div[1]/div[1]/h2").text.split()
            tira_espaco1 = "".join(var1[0:5])
            self.lista_samsung.append(tira_espaco1)
            var_valor1 = self.navegador.find_element(By.XPATH, f"/html/body/div[1]/div[1]/div/div[2]/div[3]/div[{i+9}]/a/div[2]/div[2]/div[2]/p[1]").text.split()
            tira_espaco_valor1 = "".join(var_valor1[0:4])
            self.valor_samsung.append(tira_espaco_valor1)

    def iphone(self) -> None:
        """
        Função que pega os celulares Iphone
        :return:None
        """

        self.navegador.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div/div[2]/nav/ul/li[1]/div").click()
        self.navegador.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div/div[2]/nav/ul/li[1]/div/nav/ul/li[2]/a").click()
        self.navegador.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div/div[2]/nav/ul/li[1]/div/nav/ul/li[2]/div/div/a[1]").click()
        sleep(1)
        self.iphone_celular = []
        self.iphone_valor = []

        for i in range(6):
            var = self.navegador.find_element(By.XPATH, f"/html/body/div[1]/div[1]/div/div[2]/div[3]/div[{i+1}]/a/div[2]/div[2]/div[1]/div[1]/h2").text.split()
            tira_espaco = "".join(var[0:5])
            self.iphone_celular.append(tira_espaco)
            var_valor = self.navegador.find_element(By.XPATH, f"/html/body/div[1]/div[1]/div/div[2]/div[3]/div[{i+1}]/a/div[2]/div[2]/div[2]/p[1]" ).text.split()
            tira_espaco_valor = "".join(var_valor[0:4])
            self.iphone_valor.append(tira_espaco_valor)

        for i in range(4):
            var1 = self.navegador.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[2]/div[3]/div[{i+9}]/a/div[2]/div[2]/div[1]/div[1]/h2").text.split()
            tira_espaco1 = "".join(var1[0:5])
            self.iphone_celular.append(tira_espaco1)
            var_valor1 = self.navegador.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[2]/div[3]/div[{i+9}]/a/div[2]/div[2]/div[2]/p[1]" ).text.split()
            tira_espaco_valor1 = "".join(var_valor1[0:4])
            self.iphone_valor.append(tira_espaco_valor1)


    def motorola(self) -> None:
        """
        Função que pega os celulares Motorola
        :return: None
        """

        self.navegador.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div/div[2]/nav/ul/li[1]/div").click()
        self.navegador.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div/div[2]/nav/ul/li[1]/div/nav/ul/li[2]/a").click()
        self.navegador.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div/div[2]/nav/ul/li[1]/div/nav/ul/li[2]/div/div/a[9]").click()
        self.motorola_celular = []
        self.motorola_valor = []

        for i in range(6):
            var = self.navegador.find_element(By.XPATH,
                                              f"/html/body/div[1]/div/div/div[2]/div[3]/div[{i+1}]/a/div[2]/div[2]/div[1]/div[1]/h2").text.split()
            tira_espaco = "".join(var[0:5])
            self.motorola_celular.append(tira_espaco)
            var_valor = self.navegador.find_element(By.XPATH,
                                                    f"/html/body/div[1]/div/div/div[2]/div[3]/div[{i+1}]/a/div[2]/div[2]/div[2]/p[1]").text.split()
            tira_espaco_valor = "".join(var_valor[0:4])
            self.motorola_valor.append(tira_espaco_valor)

        for i in range(4):
            var1 = self.navegador.find_element(By.XPATH,
                                               f"/html/body/div[1]/div/div/div[2]/div[3]/div[{i+9}]/a/div[2]/div[2]/div[1]/div[1]/h2").text.split()
            tira_espaco1 = "".join(var1[0:5])
            self.motorola_celular.append(tira_espaco1)
            var_valor1 = self.navegador.find_element(By.XPATH,
                                                     f"/html/body/div[1]/div/div/div[2]/div[3]/div[{i+9}]/a/div[2]/div[2]/div[2]/p[1]").text.split()
            tira_espaco_valor1 = "".join(var_valor1[0:4])
            self.motorola_valor.append(tira_espaco_valor1)


    def xiaomi(self) -> None:
        """
        Função que pega os celulares Xiaomi
        :return: None
        """
        self.navegador.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div/div[2]/nav/ul/li[1]/div").click()
        self.navegador.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div/div[2]/nav/ul/li[1]/div/nav/ul/li[2]/a").click()
        self.navegador.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div/div[2]/nav/ul/li[1]/div/nav/ul/li[2]/div/div/a[11]").click()

        self.xiaomi_celular = []
        self.xiaomi_valor = []

        for i in range(6):
            var = self.navegador.find_element(By.XPATH,
                                              f"/html/body/div[1]/div/div/div[2]/div[3]/div[{i+1}]/a/div[2]/div[2]/div[1]/div[1]/h2").text.split()
            tira_espaco = "".join(var[0:5])
            self.xiaomi_celular.append(tira_espaco)
            var_valor = self.navegador.find_element(By.XPATH,
                                                    f"/html/body/div[1]/div/div/div[2]/div[3]/div[{i+1}]/a/div[2]/div[2]/div[2]/p[1]").text.split()
            tira_espaco_valor = "".join(var_valor[0:4])
            self.xiaomi_valor.append(tira_espaco_valor)

        for i in range(4):
            var1 = self.navegador.find_element(By.XPATH,
                                               f"/html/body/div[1]/div/div/div[2]/div[3]/div[{i+9}]/a/div[2]/div[2]/div[1]/div[1]/h2").text.split()
            tira_espaco1 = "".join(var1[0:5])
            self.xiaomi_celular.append(tira_espaco1)
            var_valor1 = self.navegador.find_element(By.XPATH,
                                                     f"/html/body/div[1]/div/div/div[2]/div[3]/div[{i+9}]/a/div[2]/div[2]/div[2]/p[1]").text.split()
            tira_espaco_valor1 = "".join(var_valor1[0:4])
            self.xiaomi_valor.append(tira_espaco_valor1)

    def multilaser(self) -> None:
        """
        Fução que pega os celulares da Multilaser
        :return:None
        """
        self.navegador.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/input").click()
        self.navegador.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/input").send_keys("celular multilaser")
        sleep(5)
        self.navegador.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/button").click()
        sleep(5)

        self.multi_celular = []
        self.multi_valor = []

        for i in range(6):
            var = self.navegador.find_element(By.XPATH,
                                              f"/html/body/div[1]/div[1]/div/div[2]/div[3]/div[{i+1}]/a/div[2]/div[2]/div[1]/div[1]/h2").text.split()
            tira_espaco = "".join(var[0:5])
            self.multi_celular.append(tira_espaco)
            var_valor = self.navegador.find_element(By.XPATH,
                                                    f"/html/body/div[1]/div[1]/div/div[2]/div[3]/div[{i+1}]/a/div[2]/div[2]/div[2]/p[1]").text.split()
            tira_espaco_valor = "".join(var_valor[0:4])
            self.multi_valor.append(tira_espaco_valor)

        for i in range(4):
            var1 = self.navegador.find_element(By.XPATH,
                                               f"/html/body/div[1]/div[1]/div/div[2]/div[3]/div[{i+9}]/a/div[2]/div[2]/div[1]/div[1]/h2").text.split()
            tira_espaco1 = "".join(var1[0:5])
            self.multi_celular.append(tira_espaco1)
            var_valor1 = self.navegador.find_element(By.XPATH,
                                                     f"/html/body/div[1]/div[1]/div/div[2]/div[3]/div[{i+9}]/a/div[2]/div[2]/div[2]/p[1]").text.split()
            tira_espaco_valor1 = "".join(var_valor1[0:4])
            self.multi_valor.append(tira_espaco_valor1)

    def add_banco_dados(self) -> None:
        """
        Função que adiciona no banco de dados todos os celulares
        :return: None
        """

        for i in range(len(self.lista_samsung)):
            banco.cursor.execute(f"INSERT INTO celulares VALUES ('Samsung','{self.lista_samsung[i]}','{self.valor_samsung[i]}')")
            banco.cursor.execute(f"INSERT INTO celulares VALUES ('Iphone', '{self.iphone_celular[i]}', '{self.iphone_valor[i]}')")
            banco.cursor.execute(f"INSERT INTO celulares VALUES ('Motorola', '{self.motorola_celular[i]}', '{self.motorola_valor[i]}')")
            banco.cursor.execute(f"INSERT INTO celulares VALUES ('Xiaomi', '{self.xiaomi_celular[i]}', '{self.xiaomi_valor[i]}')")
            banco.cursor.execute(f"INSERT INTO celulares VALUES ('Multilaser', '{self.multi_celular[i]}', '{self.multi_valor[i]}')")
            banco.banco.commit()
    def remove_banco_dados(self) -> None:
        """
        Função que remove os dados antigos do banco
        :return: None
        """
        banco.cursor.execute("DELETE FROM celulares ")
        banco.banco.commit()
