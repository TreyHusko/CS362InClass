def calc(a, b):
    sum = a + b
    diff = a - b 
    multiply = a * b 
    divide = a / b

    resultsNum = [sum, diff, multiply, divide]
    total = 0
    for num in resultsNum:
        total += num
    print("The total is " + str(total))
calc(6, 3)
