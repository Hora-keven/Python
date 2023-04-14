#Jogo da forca
vida = 6
def dicas():
    palavras = ["Carro", "maçã"]
    print("Qual palavra você vai querer?  ")
    print("[0]\n[1]")
    usuario1 = int(input("escolha uma opção: "))
    for x in range(0, 7):
        if usuario1 == 0:
            print("A palavra escolhida tem 5 letras")
            print("Dica: Para maiores de 18!")
            pessoa = str(input("Digite uma letra: ")).upper()

            if pessoa == palavras[0][0]:
                print("você acertou uma letra C____")
                continue
            if pessoa == palavras[0][1]:
                print("Você acertou uma letra CA___")





dicas()