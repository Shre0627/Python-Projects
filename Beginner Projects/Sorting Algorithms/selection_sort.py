# Shreya Jamnadas
# January 3, 2025
# Coding the Selection Sort Algorithm by Scratch using loops and nested loops, conditional statements, try and catch, lists

while True:
    values = input("Enter numbers seperated by a comma: ")
    numbers = values.split(",") # list of numbers
    try:
        numbers = [int(x) for x in numbers]
        break
    except Exception:
        print("Invalid Inputs. Please input all integers!")

# nested for loop
for index in range(len(numbers)):
    for index2 in range(len(numbers)-1, index, -1):
        if numbers[index] > numbers[index2]:
            temp = numbers[index]
            numbers[index] = numbers[index2]
            numbers[index2] = temp

print(numbers)