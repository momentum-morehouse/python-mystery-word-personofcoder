from random import randint


def robot_jones(text_file):
    with open(text_file) as file:
        wordsmith = file.read().splitlines()
    #print(f.readlines())
    #print(len(wordsmith))
    z = randint(0, 235885)
    #print(z)
    randomword = wordsmith[z]
    print(randomword)
    return randomword

robot_jones("words.txt")

def user_guess():
    guess = (input("Pick a word: "))
    return (guess)