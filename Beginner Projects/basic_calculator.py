# Shreya Jamnadas
# September 8, 2024
# Creating a Basic Calculator using user input, loops, and if statements
# Next Steps: Creating a Basic Calculator using Functions

# Creating do while loops for user input
# asking for operation type 
while True:
    operationType = input("What is the operation you want to use? (ex: Addition, Subtraction, Multiplication, or Division): ")
    if operationType.lower() == "addition" or operationType.lower() == "subtraction" or operationType.lower() == "multiplication" or operationType.lower() == "division":
        break
    else:
        print("Invalid Answer!")
        continue

#asking for numbers
numbers = [] #creating an empty array/list
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
#adding num1 and num2 into list numbers
numbers.append(float(num1)) 
numbers.append(float(num2))
while True:
    finish = input("Would you like to enter another number?: ")
    if finish.lower() == "no":
        break
    elif finish.lower() == "yes":
        num3 = input("Enter a number: ")
        numbers.append(float(num3))
        continue

# Calculate values depending on the operation
if operationType.lower() == "addition":
    result = 0
    for x in numbers: #for loops for arrays - according to python tho this is not an array it is a list (numbers) but can be considered as an array
        result += x
elif operationType.lower() == "multiplication":
    result = 1
    for x in numbers:
        result *= x
elif operationType.lower() == "subtraction":
    result = numbers[0]
    for x in numbers:
        result -= x
        if result == 0:
            result = numbers[0]
            continue
elif operationType.lower() == "division":
    result = numbers[0]
    for x in numbers:
        result /= x
        if result == 1:
            result = numbers[0]
            continue

print("Answer: "+str(result))
