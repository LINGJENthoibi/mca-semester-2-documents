#Find max and min from the given list without using functions
numbers = [5 ,2 ,8 ,1 ,9]

min_value = numbers[0]

for num in numbers:
    if num < min_value:
        min_value = num
print("Minimum vlaue is:", min_value)

max_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num
print("Maximum vlaue is:", max_value)        
