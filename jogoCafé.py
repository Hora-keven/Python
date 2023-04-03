import random
from threading import Timer
import os


def inicio():
    print("-----=----=-\033[36mJOGO DA FORCA\033[m---=-----=--")
    print("    \033[33mVOCÊ TEM 6 CHANCES PARA JOGAR!\033[m")
    print("--=--==-=---=--\033[36mBOM JOGO!\033[m-==-=--=---=-")
    adicionando()


def sorteado():

    sorteio = random.randint(0, len(palavras) - 1)
    return sorteio


def traco():
    for i in range(len(traco_oculto)):
        print(traco_oculto[i], end=" ")


def jogo(vida):
    errado = []
    letra_colocada = []
    while True:
        print()
        print( dica)
        traco()
        usuario = str(input("\nDigite uma letra: "))

        if usuario not in palavra_sorteada:
            errado.append(usuario)
            print(f"Letras que você errou \033[41m{errado}\033[m",end=" ")
            vida -= 1
            print(f'voce tem {vida} de vida')
            if vida <= 0:
                print("SUA VIDA CABOU, TENTE NOVAMENTE DEPOIS!")
                break

        if usuario in palavra_sorteada:
            letra_colocada.append(usuario)
            print('-' * 35)
            print(f"Você acertou uma letra, essa(s) é (são) a(s) Letra(s) que você acertou! \033[44m\033[30m{letra_colocada}\033[m")
            print('-' * 35)

            if usuario in palavra_sorteada:
                for i in range(len(palavra_sorteada)):
                    if usuario == palavra_sorteada[i]:
                        traco_oculto[i] = usuario

        if '_' not in traco_oculto:
            tempo("\033[36mPARABENS! VOCE ACERTOU!!!\033[m")
            break


def adicionando():
    global palavra_sorteada, dica, traco_oculto

    while True:
        usu = str(input("\033[33mVocê quer adicionar palavra? [S/N]\033[m ")).upper()
        if usu == 'S':
            usu1 = str(input("\033[36mDigite a palavra: \033[m"))
            palavras.append(usu1)
            usu2 = str(input("\033[33mQual a dica dessa palavra?: \033[m"))
            dicas.append(usu2)
            if usu == 'S':
                sorte = sorteado()
                dica = dicas[sorte]
                palavra_sorteada = palavras[sorte]
        else:
            print("\033[36mContinunado...\033[m")
            break


def tempo(mensagem="\n\033[41mSeu tempo chegou ao fim!\033[m"):
    print(mensagem)
    pid = os.getpid()
    os.kill(pid, 0)


def tempo1():
    tempo_contando = Timer(5.0, tempo)
    tempo_contando.start()


dicas = ["\033[33mDica: A palavra tem 8 letras, animal amado por todos\033[m ",
         "\033[36mDica: A palavra tem 4 letras, animal amado por todos\033[m"]
palavras = ["cachorro", 'gato']

inicio()

sorte = sorteado()
dica = dicas[sorte]
palavra_sorteada = palavras[sorte]
traco_oculto = ['_'] * len(palavra_sorteada)

jogo(6)
