import random

def getLength(message):
    passLen = int(input(message))
    return passLen
def genPassword(length):
    word = ""
    i = 1
    while i <=length:
        char = random.randint(32,126)
        word += chr(char)
        i += 1
    return word

plength = getLength("Enter desired password length: ")
password = genPassword(plength)
print("Your generated password is " + str(password))


