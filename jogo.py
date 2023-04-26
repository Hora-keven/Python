import random

from jogocaraacara import Jogo

jogo = Jogo("keven")
jogo.add_dicas('o mais lindo', "gatão", "lindo", "salvador","canta de mais")
print(jogo.dicas)

jogo2 = Jogo("Maria")
jogo2.add_dicas("Minha vó", "a mais linda", "melhor pessoa", "aaaaaaa", "kssksksksk")
print(jogo2.dicas)

jogo3 = Jogo("Corsi")
jogo3.add_dicas("Surdo", "o mais fei", "melhor da bosch", "aaaaaaa", "kssksksksk")
print(jogo3.dicas)

while True:
    print(jogo3.inicio_jogo)



