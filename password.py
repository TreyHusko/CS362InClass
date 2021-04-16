import random

def getLength(message):
    passLen = int(input(message))
    return passLen
def genPassword(length):
    word = ""
    i = 0
    while i <=length:
        word += random.randint(32,126)
        i += 1
    print(word)

plength = getLength("Enter desired password length: ")
genPassword(plength)


