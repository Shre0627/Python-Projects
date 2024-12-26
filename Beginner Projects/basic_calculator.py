# Shreya Jamnadas
# September 8, 2024
# Creating a Basic Calculator using user input, loops, if statements, functions, and arrays - this calculator only calculates with a single operator
# Next Steps: Program the calculator to use multiple operators

def calc(arr, type):
    value = 0
    if type == "+":
        for x in arr:
            value += x
        return value
    elif type == "-":
        for x in arr:
            firstEle = arr[0]
            if x == firstEle:
                value = x
                continue
            value -= x
        return value
    elif type == "*":
        for x in arr:
            value = 1
            value *= x
        return value
    elif type == "/":
        for x in arr:
            firstEle = arr[0]
            if x == firstEle:
                value= x
                continue
            value /= x
        return value   
    print("Result "+str(value))   

operationType = input("What operation would you like to use? Addition (+), Substraction (-), Multiplication (*), or Division (/) - use symbols: ")
while True:
    if operationType == "+" or operationType == "-" or operationType == "*" or operationType == "/":
        break
    else:
        print("Invalid Answer")
        operationType = input("What operation would you like to use? Addition (+), Substraction (-), Multiplication (*), or Division (/) - use symbols: ")

calcQ = input("Input the numbers in a list (with spaces in between each number): ")
numbers = [] # creating an empty array list

# for loop to iterate through each element in String
for x in calcQ:
    if isinstance(x, (int, float)): # checking if x is a number or not
        numbers.append(float(x)) 

calc(numbers, operationType)