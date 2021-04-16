def divisor(d):
    i = 1
    print("The divisors of " + str(d) + " are: ")
    while i <= d:
        if (d % i == 0):
            print(i)
        i += 1
def getNumber(prompt):
    userNum = int(input(prompt))
    return userNum

input = getNumber("Enter a number to see the divisors of it: ")
divisor(input)
