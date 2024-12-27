# Shreya Jamnadas
# September 8, 2024
# Creating a Basic Calculator using user input, loops, if statements, functions, list, match statements, and try and catch 
# Limitation: This calculator only calculates with a single operator
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

while True:
    try:
        operationType = input("What operation would you like to use? Addition (+), Substraction (-), Multiplication (*), or Division (/) - use symbols: ")
        operationType = operationType.strip()
        assert operationType == "+" or operationType == "-" or operationType == "*" or operationType == "/", "Invalid Input! Must be +, -, /, or *"
        break # if condition is met
    except AssertionError as e:
        print(f"{e}")            

numbers = []
while True:
    calcQ = input("Input the numbers in a list (with space in between each number): ")
    numbers = calcQ.split(" ") # putting values in between the spaces in a list
    # checking if all values are a number
    try:
        numbers = [float(x) for x in numbers] # casting each element in the list to a float
        break # if condition is met
    except Exception:
        print("Invalid Input of Values. Please input numbers only")

answer = calc(numbers, operationType)
print("Result: "+str(answer))
        