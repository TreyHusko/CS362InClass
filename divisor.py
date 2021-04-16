def divisor(d):
    i = 1
    while i <= d:
        if (d % i == 0):
            print(i)
        i += 1
    
def getNumber(prompt):
    userNum = int(input(prompt))
    return userNum
