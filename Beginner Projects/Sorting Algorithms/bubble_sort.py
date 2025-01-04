# Shreya Jamnadas
# January 3, 2025
# Coding the Bubble Sort Algorithm by Scratch using loops and nested loops, conditional statements, try and catch, and lists
# Nest Steps: Implement Merge Sort Algorithm

while True:
    values = input("Enter numbers seperated by a comma: ")
    numbers = values.split(",") # list of numbers
    try:
        numbers = [int(x) for x in numbers]
        break
    except Exception:
        print("Invalid Inputs. Please input all integers!")

for index in range(len(numbers)):
    for index2 in range(index+1, len(numbers)):
        if numbers[index] > numbers[index2]:
                temp = numbers[index]
                numbers[index] = numbers[index2]
                numbers[index2] = temp

print(numbers)