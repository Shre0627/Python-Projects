# Shreya Jamnadas
# September 8, 2024
# Creating a Basic Calculator using user input, loops, if statements, functions, list, and match statements - this calculator only calculates with a single operator
# Next Steps: Program the calculator to use multiple operators

def calc(arr, type):
    match type:
        case "+": 
            value = 0
            for x in arr:
                value += x
            return value
        case "-": 
            for x in arr:
                firstEle = arr[0]
                if x == firstEle:
                    value = x
                    continue
                value -= x
            return value
        case "*":
            value = 1
            for x in arr:
                value *= x
            return value
        case "/":
            for x in arr:
                firstEle = arr[0]
                if x == firstEle:
                    value = x
                    continue
                value /= x
            return value  

operationType = input("What operation would you like to use? Addition (+), Substraction (-), Multiplication (*), or Division (/) - use symbols: ")
operationType = operationType.strip()
while True:
    if operationType == "+" or operationType == "-" or operationType == "*" or operationType == "/":
        break
    else:
        print("Invalid Answer")
        operationType = input("What operation would you like to use? Addition (+), Substraction (-), Multiplication (*), or Division (/) - use symbols: ")
        operationType = operationType.strip()

calcQ = input("Input the numbers in a list (with space in between each number): ")
numbers = calcQ.split(" ")
numbers = [float(x) for x in numbers]
answer = calc(numbers, operationType)
print("Result: "+str(answer))