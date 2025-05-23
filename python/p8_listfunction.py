numbers = [10, 20, 40, 50]

numbers.append(60)
print("After Append:", numbers)

numbers.extend([70, 80, 90])
print("After Extend:", numbers)

numbers.insert(2, 30)
print("After Insert:", numbers)

numbers.remove(20)
print("After Remove:", numbers)

popped_element = numbers.pop()
print("Popped Element:", popped_element)
print("After Pop:", numbers)

index = numbers.index(40)
print("Index of 40:", index)

count = numbers.count(20)
print("Count of 20:", count)

numbers.sort()
print("After Sorting:", numbers)

numbers.reverse()
print("After Reversing:", numbers)

new_list = numbers.copy()
print("Copied list:", new_list)

numbers.clear()
print("After Clearing:", numbers)
print("New list:", new_list)
