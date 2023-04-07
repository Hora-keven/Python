import random


def inicio():
    print('-='*21)
    print("     SEJA BEM-VINDO AO JOGO DA VELHA")
    print("VOCÊ VAI ESCOLHER PEDRA, PAPEL OU TESOURA.")
    print('-='*21, '\n')

def sorteio():
    numero = random.randint(0, 2)
    return numero


def sorteio_computador():
    lista = ['pedra', 'papel', 'tesoura']
    sorteado = lista[sorteio()]
    return sorteado


def jogo():

    computador = sorteio_computador()
    usuario_escolhe = int(input("Qual a sua aposta?\n[1]Pedra\n[2]Tesoura\n[3]Papel\n"))

    if usuario_escolhe == 1 and computador == 'tesoura':
        print("Você ganhou!!")
        print(f'O computador colocou {computador}')

    elif usuario_escolhe == 2 and computador == 'papel':
        print("Você ganhou!!")
        print(f'O computador colocou {computador}')

    elif usuario_escolhe == 3 and computador == 'pedra':
        print("Você ganhou!! ")
        print(f'O computador colocou {computador}')

    elif computador == 'tesoura' and usuario_escolhe == 3:
        print("O computador ganhou!")
        print(f"Eu coloquei {computador}")

    elif computador == 'pedra' and usuario_escolhe == 2:
        print('O computador ganhou!!')
        print(f"Eu coloquei {computador}")

    elif computador == 'papel' and usuario_escolhe == 1:
        print("Computador ganhou!!")
        print(f"Eu coloquei {computador}")

    elif computador == 'pedra' and usuario_escolhe == 1:
        print("Houve um empate!")

    elif computador == 'tesoura' and usuario_escolhe == 2:
        print("Houve um empate!")
    elif computador == 'papel' and usuario_escolhe == 3:
        print('Houve um empate!')


inicio()
jogo()



