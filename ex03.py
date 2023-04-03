import random
def subtra(number, life):
    man = int(input('Input your bet: '))
    sub = number - man
    subusu = life - sub
    return subusu


if __name__ == '__main__':
    number = random.randint(1, 100)
    life = 50
    subusu = subtra(number, life)

    #print("You olny have {} of life".format(subtra())