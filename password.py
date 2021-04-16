import random

def getLength(message):
    passLen = int(input(message))
    return passLen
def genPassword(length):
    word = ""
    for len(length):
        word += random.randint(32,126)
    print(word)

plength = getLength("Enter desired password length: ")
genPassword(plength)


