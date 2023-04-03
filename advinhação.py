import random
import os
from threading import Timer


def sorteado():
    numero = random.randint(1, 101)
    return numero


def jogo():
    sorteio = sorteado()
    vida = 50

    for i in range(1, 5):
        aposta = int(input("Digite sua aposta: "))
        tempo1()
        if aposta == sorteio:
            print("\033[34mVocê acertou o numero sorteado!\033[m")
            tempo("\033[33mPARABÉNS!!\033[m")
            break
        else:
            difrenca = aposta - sorteio
            vida = vida - abs(difrenca)
            abs(vida)
            print(f"\033[31mVocê errou o numero sorteado! tente de novo, vida: {vida}!\033[m")
            if vida <= 0:
                print("\033[31mSUAS CHANCES ACABARAM!\033[m")
                break

def inicio():
    print("-"*10, "\033[36mSEJA BEM VINDO!\033[m","-"*10)
    print("\033[32mVOCÊ TEM 50 DE VIDA, SE VOCÊ ERRAR VOCÊ PERDE!\033[m\n"
          "----\033[36mVOCÊ TEM 5 CHANCES PARA JOGAR!\033[m----\n")


def tempo(mensagem="\n\033[41mSeu tempo chegou ao fim!\033[m"):
    print(mensagem)
    pid = os.getpid()
    os.kill(pid, 0)


def tempo1():
    tempo_contando = Timer(15.0, tempo)
    tempo_contando.start()


inicio()
jogo()